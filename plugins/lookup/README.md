# Ansible Lookup Plugins

## Description - wwt.meraki.fetch

This plugin is used to query the Meraki Dashboard API for the requested information

### Using this Plugin

The plugin is used by passing a `term` which correlates to the method called to retreive information.

#### Examples

Use `wwt.meraki.fetch` to query the organizationId of a given Organization

```yaml
---
- name: Configure Meraki Network
  cisco.meraki.networks:
    meraki_api_key: "{{ auth_key }}"
    state: "{{ network.state }}"
    organizationId: "{{ lookup('wwt.meraki.fetch', 'org_id', org_name=network.organization, meraki_api_key=auth_key) }}"
    name: "{{ network.name }}"
    productTypes: "{{ network.type }}"
    timeZone: "{{ network.timezone }}"
    tags: "{{ network.tags }}"
```

Use `wwt.meraki.fetch` to query the networkId of a given Network Name and Organization

```yaml
---
- name: Claim Devices
  cisco.meraki.networks_devices_claim:
    meraki_api_key: "{{ auth_key }}"
    networkId: "{{ lookup('wwt.meraki.fetch', 'network_id', org_name=network.organization, meraki_api_key=auth_key, network_name=network.name) }}"
    serials: "{{ add_present_devices }}"
  when: add_present_devices is defined
```

Use `wwt.meraki.fetch` to query the device serial numbers belonging to a given network Name and Organization

```yaml
---
 - name: Look for existing network devices
   ansible.builtin.set_fact:
     device_serials: "{{ query('wwt.meraki.fetch', 'network_devices', network_name=network.name, org_name=network.organization, meraki_api_key=auth_key) }}"
```

Use `wwt.meraki.fetch` to query for a specific device serial number belong to a given network Name and Organization

```yaml
- name: Query Device Serial Number for {{ appliance.name }}
  ansible.builtin.set_fact:
    device_serial: "{{ lookup('wwt.meraki.fetch', 'network_devices', org_name=meraki_mx_configuration.network.organization, meraki_api_key=auth_key, network_name=meraki_mx_configuration.network.name, device_name=appliance.name) }}"
```

## Contributors

Nick Thompson <https://github.com/nsthompson>
