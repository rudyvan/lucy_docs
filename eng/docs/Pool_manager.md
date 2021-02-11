<!--s_name-->
# pool_manager

<!--e_name-->

<!--s_role-->
The role_me attribute assigns the role __pool__ to the things_controller that is mentioned.

<!--e_role-->

<!--s_descr-->
TBI/This is the control interface to an indoor or outdoor swimming pool

<!--e_descr-->

<!--s_tbl-->
## List of [properties](Properties.md) for __pool_manager__:

  | Attribute | Representation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | pool_closed_winter | Virtual | True | - | virtual which states a long term disable of the pool, heating will work only if temp below pool_temp_min | 
  | pool_heater | Motor | True | True | several pool heaters | 
  | pool_lights | Light | True | True | pool lights | 
  | pool_night_mode | Virtual | True | - | virtual to state that pool house is currently closed as in night mode | 
  | pool_pump | Output | False | True | output switch to the pump | 
  | pool_temp | Sensor | False | True | pool temp is a list of sensors, the temp is averaged over all of them | 
  | pool_temp_max | int | True | - | this is considered the max temperature, a warning will be issued | 
  | pool_temp_min | int | True | - | this is considered the min temperature, a warning will be issued | 
  | pool_temp_optimal | int | True | - | below this temp, the heaters will kick in | 
  | pump_in_temp | Sensor | False | - | temperature sensor before the pump | 
<!--e_tbl-->

