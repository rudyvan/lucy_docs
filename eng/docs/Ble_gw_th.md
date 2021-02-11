<!--s_name-->
# Ble_gw_th

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
is an internal generated thing for every beacon for every gateway to hold the rssi value or zero when lost

<!--e_descr-->

<!--s_tbl-->
## List of [properties](Properties.md) for __Ble_gw_th__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | duration | int | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | play | tuple:virtual_tuples | True | - | the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on' | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | threshold | float | False | - | the minimum value that an analog input must change before the value is considered changed | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 

## List of [copy_things] for  __Ble_gw_th__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl-->

