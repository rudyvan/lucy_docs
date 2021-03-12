<!--s_name-->
# Site_tasker

<!--e_name-->

<!--s_role-->
<!--e_role-->

## Summary

<!--s_descr-->
the app that allows certain roles to assume a multi site role

<!--e_descr-->

The site tasker receives a list of the sites this things_controller will assume and reads every site, parses the config files and loads all the objects in memory.
Data from other things_controllers will be processed as if there was only one site in scope, easily switching between the different sites.

Also timers and reports are site specific and will run as they are necessary.

With these possibilities, you could design one deployer or forensics role things_controller, applied to a large set of sites.
All having the same base code, no replication or redundant scripts.

This module is work in progress..

<!--s_tbl-->
## List of [properties](Properties.md) for __Site_tasker__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | role_me | {tc} | True | - | role_me of 'Site_tasker', adds <system> to the roles of the specified tc | 
<!--e_tbl-->

