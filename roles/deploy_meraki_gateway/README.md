`deploy_meraki_gateway`
=========

This role encapsulates the common steps for configuring the Meraki MX Gateway.

Requirements
------------



Role Variables
--------------

`org_name` or `org_id`

`net_name` or `net_id`

Environment Variable `MERAKI_KEY` or `auth_key` which includes your Meraki Dashboard API key.


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

GPL3

Author Information
------------------

Jeff Andiorio - WWT

Nick Thompson - WWT
