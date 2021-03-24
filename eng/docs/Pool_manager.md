<!--s_name-->
# Pool_manager

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
This is the app for swimpool management

<!--e_descr-->

<!--s_tbl-->
## List of [properties](Properties.md) for __Pool_manager__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | comfort_control | dict | True | True | energy control for heating or cooling the pool | 
  | comfort_settings | dict | True | - | comfort target settings for the pool | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | lights | ['Dimmer', 'Output', 'Light', 'Color_light', 'Dim_light', 'Motor'] | True | True | light decoration, lights, dimable lights or color lights | 
  | role_me | {tc} | False | - | role_me of 'Pool_manager', adds <pool> to the roles of the specified tc | 
  | sensors | ['Sensor'] | True | True | Sensors for Temperature, Humidity, Chloride, pH, etc.. | 
  | usage_meters | *Meter | True | True | utility usage of water, electricity and pool consumables | 
<!--e_tbl-->

