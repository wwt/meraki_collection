# Ansible Collection - wwt.meraki

This collection of Ansible roles is used for configuring a variety of Meraki devices and has been tested with the following:

* Meraki MX68 Firewall
* Meraki MR44 Access Point
* Meraki MV2 Camera
* Meraki MT30 Sensor

The following roles are included in this collection:

* claim_meraki - Role to claim Meraki Orders, Licenses, and Devices into the Meraki Dashboard
* configure_meraki_mr - Role to configure Meraki MR Access Points
* configure_meraki_mt - Role to configure Meraki MT Sensors
* configure_meraki_mv - Role to configure Meraki MV Security Cameras
* configure_meraki_mx - Role to configure Meraki MX Firewalls
* manage_meraki_network - Role to configure Meraki networks and claim devices into network inventory

## Common Variables

> :warning: The following variables are common and required for most of the roles:

```yaml
dashboard_base_url: https://api.meraki.com/api/v1
auth_key: <YOUR-DASHBOARD-API-KEY>
```

## Contributors

Nick Thompson <https://github.com/nsthompson>
