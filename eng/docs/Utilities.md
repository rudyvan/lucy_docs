<!--s_name_utilities-->
# Utilities

<!--e_name_utilities-->

<!--s_role_utilities-->
<!--e_role_utilities-->

<!--s_descr_utilities-->
Dictionary of utilities with a designated thingscontroller to manage

<!--e_descr_utilities-->


## Summary

__THIS MODULE IS EXPERIMENTAL AND NEED SIGNIFICANT IMPROVEMENT__

It is important to know your daily consumption of water, gas and electricity and link with a specialized company to get the best price in real time.
Also when abnormal situations happen, such as water usage of high electricity usage when on holidays is an important alert situation.

I tried with camera's and utility meter recognition but the result was not stable or good enough.

Currently i am experimenting with [june energy](https://june.energy/en), as they have a specialized device for reading meters with a camera.

Everything has been prepared in Lucy to define utilities and meters, see the example below.

Besides meter reading, it is also possible to estimate gas consumption if you use gas for cooking, for heating and for household warm water.
How?  Just put a temperature sensor at the exhaust so that you can measure how long each consumer has been working and if you know when one is the only one working, you can measure the consumption per minute and use that as a given.

This module should also be used for solar and wind energy management.

Much to do and to improve!


<!--s_tbl_utilities-->
## List of [properties](Properties.md) for __Utilities__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | items | *Utility | - | True | dict of utility items | 
  | notifications | ['daily_cost', 'monthly_cost', 'weekly_cost', 'yearly_cost'] | True | - | notifications, see [__Notifier__](Notifier.md) | 
  | role_me | {tc} | False | - | role_me of 'Utilities', adds <utilities> to the roles of the specified tc | 

## List of [Notifications](Notifier.md) for  __Utilities__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | daily_cost | daily cost reporting | 
  | monthly_cost | monthly cost reporting | 
  | weekly_cost | weekly cost reporting | 
  | yearly_cost | yearly cost reporting | 
<!--e_tbl_utilities-->


<!--s_name_utility-->
# Utility

<!--e_name_utility-->

<!--s_descr_utility-->
An utility description with meters, sensors, costs, scenes

<!--e_descr_utility-->

<!--s_tbl_utility-->
## List of [properties](Properties.md) for __Utility__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | description | str | True | - | free text to identify your utility, will be used in reports and notifications | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | nodes | ['Meter', 'Fake_meter'] | True | True | nodes in the utility topology where meters are placed to measure usage. To measure intensity in the nodes, use method_things attribute of the meter to add sensors | 
  | scenes | dict | True | - | scenes that can be called in effect scenarios | 
  | sensors | *Sensor | True | - | sensors measuring the utility intensity such as power (watts) for electricity or °C of heated water, preferably use sensors as method_things attached to the meters as they are embedded into the nodes concept | 
  | storage | *Utility_storage | True | - | a tank or battery type storage for storage of utility | 
  | topology | valid_list | False | - | topology is either 'network' (such as electricity) or 'pipe' (such as water) | 
  | unit | dict | False | - | by default it defines the unit for meters, but you can also specify the unit for the sensors, see the examples of what is possible | 
<!--e_tbl_utility-->

<!--s_name_utility_storage-->
# Utility_storage

<!--e_name_utility_storage-->

<!--s_descr_utility_storage-->
An utility storage such as a battery or a water tank

<!--e_descr_utility_storage-->

<!--s_tbl_utility_storage-->
## List of [properties](Properties.md) for __Utility_storage__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | description | str | True | - | free text to identify your utility storage, will be used in reports and notifications | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | occupancy | *Sensor | False | - | occupancy of the storage in % | 
  | size | float | False | - | size of the storage in the utility base unit | 
<!--e_tbl_utility_storage-->

