# wwt\.meraki Release Notes

**Topics**

- <a href="#v1-1-3">v1\.1\.3</a>
    - <a href="#bugfixes">Bugfixes</a>
- <a href="#v1-1-2">v1\.1\.2</a>
    - <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#bugfixes-1">Bugfixes</a>
- <a href="#v1-1-1">v1\.1\.1</a>
    - <a href="#minor-changes">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide-1">Breaking Changes / Porting Guide</a>
- <a href="#v1-1-0">v1\.1\.0</a>
    - <a href="#release-summary">Release Summary</a>
    - <a href="#new-plugins">New Plugins</a>
        - <a href="#lookup">Lookup</a>

<a id="v1-1-3"></a>
## v1\.1\.3

<a id="bugfixes"></a>
### Bugfixes

* configure\_meraki\_mx \- Fixed VLAN provisioning to match requirements with cisco\.meraki collection version 2\.18\.1

<a id="v1-1-2"></a>
## v1\.1\.2

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

* manage\_meraki\_network \- updated data model so that tags are now a list

<a id="bugfixes-1"></a>
### Bugfixes

* configure\_meraki\_mt \- fixed conditional preventing lookup dictionary creation
* configure\_meraki\_mx \- fixed VLAN provisioning and updates due to VLAN 1 already existing
* manage\_meraki\_network \- fixed device provisioning to include name and tags

<a id="v1-1-1"></a>
## v1\.1\.1

<a id="minor-changes"></a>
### Minor Changes

* configure\_meraki\_mv \- Updated data handling for MQTT configuration with camera sense\.

<a id="breaking-changes--porting-guide-1"></a>
### Breaking Changes / Porting Guide

* configure\_meraki\_mr \- Data model updated to support migration to latest cisco\.meraki certified collection\.
* configure\_meraki\_mt \- Data model updated to support migration to latest cisco\.meraki certified collection\.
* configure\_meraki\_mv \- Data model updated to support migration to latest cisco\.meraki certified collection\.
* configure\_meraki\_mx \- Data model updated to support migration to latest cisco\.meraki certified collection\.

<a id="v1-1-0"></a>
## v1\.1\.0

<a id="release-summary"></a>
### Release Summary

This release includes updates to support the certified cisco\.meraki content collection\.

<a id="new-plugins"></a>
### New Plugins

<a id="lookup"></a>
#### Lookup

* wwt\.meraki\.fetch \- Fetch data from the Meraki API\.
