"""
Ansible lookup plugin to fetch data from the Meraki Dashboard

Written by Nick Thompson (@nsthompson)
Copyright (C) 2024 World Wide Technology
All Rights Reserved
"""

from __future__ import (
    absolute_import,
    division,
    print_function
)
from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display
from ansible.module_utils.six import raise_from

__metaclass__ = type  # pylint: disable=C0103

DOCUMENTATION = r"""
  name: fetch
  author: Nick Thompson (@nsthompson) <nick.thompson@wwt.com>
  version_added: "1.1.0"
  short_description: Fetch data from the Meraki API
  description:
      - This lookup returns the requested data from the Meraki Dashboard API
  options:
    _terms:
      description:
        - Requested Data to be Fetched
      type: string
      required: True
    meraki_api_key:
      description:
        - Meraki API Key
      type: string
      required: True
    org_name:
      description:
        - Meraki Organization Name
      type: string
      required: True
    network_name:
      description:
        - Meraki Network Name
      type: string
      required: False
  notes:
    - Returns fetched information
"""


try:
    import meraki
except ImportError as import_exception:
    MERAKI_IMPORT_EXCEPTION = import_exception
else:
    MERAKI_IMPORT_EXCEPTION = None

display = Display()


class Fetch():
    """
    Class to fetch data from the Meraki Dashboard API
    """
    def __init__(self, **kwargs):
        """
        __init__ looks up the meraki org ID as it is used
        by all subsequent dashboard API calls

        Requires:
            org_name
            meraki_api_key

        Raises:
            AnsibleError: Raises an error if the org is not found.
        """
        self.kwargs = kwargs

        meraki_api_key = self.kwargs.get("meraki_api_key")
        org_name = self.kwargs.get("org_name")

        if ((org_name is None) or (meraki_api_key is None)):
            raise AnsibleError(
                'org_name and meraki_api_key are required.'
            )
        self.dashboard = meraki.DashboardAPI(meraki_api_key, suppress_logging=True)
        display.vvvv(
            "Looking for available Meraki organizations..."
        )
        organizations = self.dashboard.organizations.getOrganizations()
        display.vvvv(f'Looking for Meraki Organization: {org_name}')

        organization_id = None
        for org in organizations:
            if org.get("name") == org_name:
                organization_id = org.get("id")
                break

        if organization_id is not None:
            self.organization_id = organization_id
        else:
            raise AnsibleError(
                f'organization with name "{org_name}" cannot be found.'
            )

    def org_id(self):
        """Method to get Meraki Organization ID by Name

        Requires:
            organization_id

        Returns:
            list: List of Org IDs
        """
        organization_id = self.organization_id
        results = [organization_id]
        return results

    def network_id(self):
        """
        Method to get Meraki Network ID by Name

        Requires:
            organization_id
            network_name

        Returns:
            list: List of Network IDs
        """
        organization_id = self.organization_id
        network_name = self.kwargs.get("network_name")

        if network_name is None:
            raise AnsibleError(
                'network_name is required.'
            )

        results = []

        if network_name is not None:
            display.vvvv(f'Looking for Meraki Network: {network_name}')
            networks = self.dashboard.organizations.getOrganizationNetworks(
                organization_id,
                total_pages='all'
            )

            for network in networks:
                if network.get("name") == network_name:
                    network_id = network.get("id")
                    break

            if network_id is not None:
                results.append(network_id)
            else:
                raise AnsibleError(
                    f'network with name "{network_name}" cannot be found.'
                )

        return results

    def network_devices(self):
        """
        Method to get Meraki Network Devices by Network Name

        Requires:
            organization_id
            network_name

        Returns:
            list: List of Network Devices by SN
        """
        organization_id = self.organization_id
        network_name = self.kwargs.get("network_name")

        if network_name is None:
            raise AnsibleError(
                'network_name is required.'
            )

        results = []

        if network_name is not None:
            display.vvvv(f'Looking for Meraki Network: {network_name}')
            networks = self.dashboard.organizations.getOrganizationNetworks(
                organization_id,
                total_pages='all'
            )

            for network in networks:
                if network.get("name") == network_name:
                    network_id = network.get("id")
                    break

            if network_id is not None:
                display.vvvv(
                    f'Querying network devices on network ID: {network_id}'
                )
                network_devices = self.dashboard.networks.getNetworkDevices(
                    network_id
                )
                for device in network_devices:
                    serial = device.get("serial")
                    if serial is not None:
                        results.append(serial)
            else:
                raise AnsibleError(
                    f'network with name "{network_name}" cannot be found.'
                )

        return results


class LookupModule(LookupBase):  # pylint: disable=C0115

    def run(self, terms, variables=None, **kwargs):
        if MERAKI_IMPORT_EXCEPTION:
            raise_from(
                AnsibleError("meraki sdk must be installed to use this plugin"),
                MERAKI_IMPORT_EXCEPTION
            )

        results = []

        try:
            # Connect to Meraki Dashboard API
            fetch = Fetch(**kwargs)

            for term in terms:
                func = getattr(fetch, term)
                results = func()

        except Exception as e:
            raise AnsibleError(e) from e

        return results
