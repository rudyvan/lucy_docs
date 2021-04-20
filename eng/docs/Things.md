# Devices / Things

Devices ("things" in the speak of iot) exits in many type and forms, and are built from basic concepts such as binary (2 states), digital (consecutive discreet states) or analog (infinite between 2 ranges).

## Available Devices

Below are some of the devices currently available, and many more will be added in the future.

  | Device Name | Derived from | Parameters | Description |
  | --- | --- | --- | --- |
  | __[Raspi](Things_controllers.md)__  | -  | ip, io_dev, color="", roles=None, [properties](Properties.md)=None | A raspberry pi |
  | __[Arduino](Things_controllers.md)__| Raspi | ip, color="", roles=None | an Arduino with Ethernet shield resembling a Raspi with piface |
  | __[Ubuntu](Things_controllers.md)__ | Raspi | ip, io_dev, color="",roles=None, [properties](Properties.md)=None | any computer with ubuntu or debian linux version |
  | __[Vera](Vera_driver.md)__         | Gateway | ip, color="" | Vera controller for zwave and btle devices / scenes |
  | __[Hue](Hue_driver.md)__           | Gateway | ip, color="" | an Philips Hue bridge to control lights |
  | __[Ikea](Ikea_driver.md)__         | Gateway | ip, secret, color="" | Ikea tradfri gateway to control lights |
  | __[Daikin](Daikin_driver.md)__     | Gateway | ip, f_rate,f_dir, color="",roles=None, [properties](Properties.md)=None | daikin room air controller |
  | __[Somfy](Somfy_driver.md)__       | Gateway | ip,  color="",roles=None, [properties](Properties.md)=None | somfy bridge controller |
  | __[Niko](Niko_driver.md)__         | Gateway | ip,  color="",roles=None, [properties](Properties.md)=None | niko bus controller |
  | __[lutron](Lutron_driver.md)__     | Gateway | ip,  color="",roles=None, [properties](Properties.md)=None | lutron bus controller |
  | __[knx](Knx_driver.md)__           | Gateway | ip,  color="",roles=None, [properties](Properties.md)=None | knx ip bus controller |
  | __[modbus](Modbus_driver.md)__     | Gateway | ip,  color="",roles=None, [properties](Properties.md)=None | RS485 modbus controller |
  | __[Camera](Camera.md)__ | -  |  file_ID, ip, port, user,	member_of=[], [properties](Properties.md)=None | an ip camera |
  | __[ping](Network_controller.md)__ | obj.Digital_input | ip, ip_action=0, spec_func=None, [properties](Properties.md)=None | ip_action=-1 (no ping), 0 (ping), 1 (ping and if lost then internet alarm) |
  | __[Sonos](Sonos.md)__ | - | ip, sonos_type, zone_controller=True, ping=True, [properties](Properties.md)=None | sonos speaker |
  | __[Clim_SW](Climate.md)__ | obj.Digital_output | [path](Path.md), i_make=None, temp_sensor=None, active=1, [properties](Properties.md)=None, [value_logic](value_logic.md)=None, climate_system='' | climate switch with an optional temp sensor   |
  | __[Clim_SP](Climate.md)__ | obj.Analog_output | [path](Path.md), i_make=None, threshold=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None, climate_system='' | climate set point   | 
  | __[Door](Door.md)__ | obj.Digital_input | [path](Path.md), active=1, duration=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | a door definition |
  | __[Window](Door.md)__ | Door |  [path](Path.md), active=1, duration=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | a window definition  |
  | __[Win_cover](Door.md)__ | obj.Analog_output |  [path](Path.md), [properties](Properties.md)=None, [value_logic](value_logic.md)=None | a window cover definition such as a sunscreen or a roller shutter, down=0, up=100%  |
  | __[Irr](Irrigation.md)__ | obj.Digital_output |  [path](Path.md), time_run=0, active=1, duration=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | an irrigation point |
  | __Input__ | obj.Digital_input |  [path](Path.md), active=1, duration=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | basic input item | 
  | __Button__ | Input |  [path](Path.md), active=1, duration=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | a digital input device |
  | __Switch__ | Input |  [path](Path.md), active=1, duration=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | a digital input device |
  | __Sensor_switch__ | Input |  [path](Path.md), active=1, duration=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | a digital input device activated by reading a sensor value |
  | __Optical__ | Input | [path](Path.md), active=1, duration=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | a digital input device |
  | __[Mail](Mailbox_alert.md)__ | Input |  [path](Path.md), active=1, duration=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | | 
  | __[Fire_detector](Security.md)__ | Input |  [path](Path.md), active=0, duration=0, [properties](Properties.md)=None | fire detector, active when signal is gone  |
  | __[Alarm_detector](Security.md)__ | Input |  [path](Path.md), active=0, duration=0, detector_type=None, [properties](Properties.md)=None, security_system='' | alarm detector any type, active when signal is gone | 
  | __Output__ | obj.Digital_output |  [path](Path.md), active=1, duration=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | basic output item | 
  | __[Alarm_siren](Security.md)__ | Output |  [path](Path.md), active=1, [properties](Properties.md)=None, security_system='' | a siren device |
  | __[Light](Light_manager.md)__ | Output |  [path](Path.md), active=1, duration=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | digital light |
  | __Dimmer__ | obj.Analog_output | [path](Path.md), duration=0, [properties](Properties.md)=None, threshold=0, [value_logic](value_logic.md)=None  | default is "led", unless type in [properties](Properties.md) is set to "rgb" |
  | __Sensor__ | obj.Analog_input |  [path](Path.md), [properties](Properties.md)=None, [value_logic](value_logic.md)=None | basic sensor device, the [path](Path.md) determines the type of sensor |
  | __Fake_sensor__ | obj.Analog_input |  [path](Path.md), [properties](Properties.md)=None, [value_logic](value_logic.md)=None | calculated sensor device, the [path](Path.md) determines the type of sensor |
  | __[Virtual](Virtual.md)__ | obj.Digital_output |  to_do, active=1, duration=0, parameters=None, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | internal signal device | 
  | __[Virtual_R](Virtual.md)__ | obj.Digital_range | to_do, digital_range=None, description_r=None, active=1, duration=0, parameters=None, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | internal signal device |
  | __[Event](Event.md)__ | obj.Digital_input |  to_do, parameters=None, active=1, duration=0, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | internal program sketch |
  | __[Utility_meter](Utility.md)__ | obj.String | 	role_me, ean, vid, cam_roi, cntr_format, unit, value, [properties](Properties.md)=None | utility meter such as gas, water, power  |
  | __[Meter](Utility.md)__ | obj.Analog_input | 	unit, value, [properties](Properties.md)=None | utility meter such as gas, water, power  |
  | __[Fake_meter](Utility.md)__ | obj.Analog_input | 	unit, value, [properties](Properties.md)=None | utility meter such as gas, water, power  |
  | __[Beacon_instance](Btle_driver.md)__ | obj.Analog_input |  room, option, b_i_name, [properties](Properties.md)=None | the manifestation of a beacon on a gateway |
  | __[Beacon](Btle_driver.md)__ | -  |  what_is, uuid, major, minor, [properties](Properties.md)=None | definition parameters of a beacon |
  | __[Access_beacon](Btle_driver.md)__ | Beacon |  what_is, rights, uuid, major, minor, [properties](Properties.md)=None | beacon used for access purposes |
  | __[Access](Access.md)__ | -  |  who_is, what_do, rights, [properties](Properties.md)=None | access rights for a person |
  | __Str_device__ | obj.String |  [path](Path.md), [properties](Properties.md)=None, [value_logic](value_logic.md)=None | basic string item |
  | __[Access_point](Access.md)__ | Str_device |  [path](Path.md), direction, [properties](Properties.md)=None, [value_logic](value_logic.md)=None | access registration device |
  | __[Vera_cmd](Vera_driver.md)__ | - | vera_type, vera_pars, notify | one vera device mapping |

## Typical Device Parameters:
 
  | parameter	  | occurs where   | what is |
  | ---           | ---            | --- |
  | __color__     | raspi devices  | one of the console color codes "black","red","green","brown","blue","magenta","cyan","white","underscore" and is used for display purposes only |
  | __active__    | binary devices | is high the active state (active=1) or low (active=0).  Door and Windows have an active state when they are closed | 
  | __threshold__ | analog devices | is how much the value has to change before it triggers a logging or communications message to a controlling raspberry |
  | __duration__  | binary devices | is the time that an input device has to be high or low before that input accept the value and for outputs it is the time the output will stay active before it returns inactive automatically |

* * *

# Basic Device Types
  
The basic device items are presented now in more detail, and importantly the basic [properties](Properties.md) that they pass on to their offspring.

## 'Output' Thing

<!--s_descr_o-->
Output description, works also for the derived classes

<!--e_descr_o-->

<!--s_tbl_o-->
## List of [properties](Properties.md) for __Output__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | active | valid_set_int | False | - | designate the active state for a binary thing, either 0 or 1 | 
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | descr_01 | list-2 | False | - | description for a binary thing when payload value is 0 or 1 | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | method_things | ['activate_button', 'de_activate_button', 'is_on', 'on_off_relay', 'toggle_button'] | False | - | special methods of this thing, mostly realised through things | 
  | my_assistant | bool | True | - | a flag if voice (alexa) can activate this thing | 
  | notifications | ['active', 'app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'inactive', 'notify_binary+', 'payload_no'] | True | - | the notifications for outputs, see [__Notifier__](Notifier.md) | 
  | path | str, str_list | False | - | path to the specific hardware element | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 
  | where2find | str | True | - | where to find in the room or place | 

## List of [Notifications](Notifier.md) for  __Output__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is non zero | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | inactive | when payload is zero | 
  | notify_binary+ | extra notifications that apply to all binary type things | 
  | payload_no | the requested payload is refused | 

## List of [copy_things] for  __Output__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 

## List of [method_things] for  __Output__:

  | Method Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | activate_button | ['Button'] | {'descr': 'activates the output if inactive', 'short': 'activate_button'} | 
  | de_activate_button | ['Button'] | {'descr': 'deactivates the output if active', 'short': 'de_activate_button'} | 
  | is_on | Input | {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'} | 
  | on_off_relay | ['Output', 'Light'] | {'descr': 'deactivates the output if active', 'short': 'de_activate_button'} | 
  | toggle_button | ['Button'] | {'descr': 'is an input to toggle the output state', 'short': 'toggle_button'} | 
<!--e_tbl_o-->

* * *

## 'Input' Thing

<!--s_descr_i-->
Input description, works also for the derived classes

<!--e_descr_i-->

<!--s_tbl_i-->
## List of [properties](Properties.md) for __Input__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | active | valid_set_int | False | - | designate the active state for a binary thing, either 0 or 1 | 
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | descr_01 | list-2 | False | - | description for a binary thing when payload value is 0 or 1 | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'inactive', 'notify_binary+', 'payload_no'] | True | - | the notifications for inputs, see [__Notifier__](Notifier.md) | 
  | path | str, str_list | False | - | path to the specific hardware element | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 
  | where2find | str | True | - | where to find in the room or place | 

## List of [Notifications](Notifier.md) for  __Input__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is non zero | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | inactive | when payload is zero | 
  | notify_binary+ | extra notifications that apply to all binary type things | 
  | payload_no | the requested payload is refused | 

## List of [copy_things] for  __Input__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_i-->

* * *

## 'Sensor' Thing

<!--s_descr_s-->
Any temperature sensor

<!--e_descr_s-->

<!--s_tbl_s-->
## List of [properties](Properties.md) for __Sensor__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | descr | str | False | - | free description field for this thing | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | high | float | True | - | - | 
  | i_read | str | False | - | the type of data that this sensor reads | 
  | icon | str | True | - | icon file for this element | 
  | low | float | True | - | - | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'deicing', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'freezing', 'high', 'inactive', 'low', 'negative', 'normal', 'notify_analog+', 'payload_no', 'positive'] | True | - | the notifications for Sensors, see [__Notifier__](Notifier.md) | 
  | path | str, str_list | False | - | path to the specific hardware element | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | threshold | float | False | - | the minimum % that an analog input must change before the value is considered changed | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 
  | where2find | str | True | - | where to find in the room or place | 

## List of [Notifications](Notifier.md) for  __Sensor__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is non zero | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | deicing | temperature becomes positive | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | freezing | temperature becomes below zero | 
  | high | when payload reaches high | 
  | inactive | when payload is zero | 
  | low | when payload reaches low | 
  | negative | when payload reaches negative, coming from a positive payload | 
  | normal | when payload becomes lower than high or higher than low | 
  | notify_analog+ | extra notifications that apply to all analog type things | 
  | payload_no | the requested payload is refused | 
  | positive | when payload reaches positive or zero coming from a negative payload | 
<!--e_tbl_s-->

## 'Environment Sensor' Thing

<!--s_descr_es-->
Any environment sensor measuring '%H','Lux','mmB','dP°C','CO2','CO'

<!--e_descr_es-->

<!--s_tbl_es-->
## List of [properties](Properties.md) for __Env_sensor__:

  | Attribute | Representation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | check_event | Event | True | - | see the description on events, the temp_check event exists to check sensor values, see [__Event__](Event.md) | 
  | nty_all | ['app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'high', 'low', 'normal', 'payload_no'] | True | - | the notifications for Environment Sensors, see [__notifier__](Notifier.md) | 

## List of [Notifications](Notifier.md) for  __Env_sensor__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | app_done |  | 
  | app_start |  | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | high |  | 
  | low |  | 
  | normal |  | 
  | payload_no | the requested payload is refused | 
<!--e_tbl_es-->

* * *

## 'Sensor_switch' Thing

<!--s_descr_s_sw-->
An Input switch which is activated by something such as a high temperature like a thermostat

<!--e_descr_s_sw-->

<!--s_tbl_s_sw-->
## List of [properties](Properties.md) for __Sensor_switch__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | active | valid_set_int | False | - | designate the active state for a binary thing, either 0 or 1 | 
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | descr_01 | list-2 | False | - | description for a binary thing when payload value is 0 or 1 | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | i_read | str | False | - | the type of data that this sensor reads | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'inactive', 'notify_binary+', 'payload_no'] | True | - | the notifications for inputs, see [__Notifier__](Notifier.md) | 
  | path | str, str_list | False | - | path to the specific hardware element | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 
  | where2find | str | True | - | where to find in the room or place | 

## List of [Notifications](Notifier.md) for  __Sensor_switch__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is non zero | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | inactive | when payload is zero | 
  | notify_binary+ | extra notifications that apply to all binary type things | 
  | payload_no | the requested payload is refused | 

## List of [copy_things] for  __Sensor_switch__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_s_sw-->

* * *

## 'Str_device' Thing

<!--s_descr_str-->
Str_device, a device containing text

<!--e_descr_str-->

<!--s_tbl_str-->
## List of [properties](Properties.md) for __Str_device__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Str_device']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Str_device']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['app_done', 'app_start', 'disable_off', 'disable_on', 'empty', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'letters', 'notify+', 'numbers', 'payload_no'] | True | - | the notifications for Str_devices, see [__Notifier__](Notifier.md) | 
  | path | str | False | - | path to the specific hardware element | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 

## List of [Notifications](Notifier.md) for  __Str_device__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | empty | string is empty | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | letters | string is all letters | 
  | notify+ | extra notifications | 
  | numbers | string is only numbers | 
  | payload_no | the requested payload is refused | 

## List of [copy_things] for  __Str_device__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Str_device'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Str_device'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_str-->

## 'Wind_speed' Thing

<!--s_descr_wsp-->
Wind speed meter device

<!--e_descr_wsp-->

<!--s_tbl_wsp-->
## List of [properties](Properties.md) for __Wind_speed__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | descr | str | False | - | free description field for this thing | 
  | edges_per_rev | int | False | - | number of edges per turn | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | high_speed_factor | float | False | - | high speed wind factor | 
  | icon | str | True | - | icon file for this element | 
  | low_speed_factor | float | False | - | low speed wind factor | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | method_things | ['wind_gust'] | False | - | special methods of this thing, mostly realised through things | 
  | notifications | ['high_wind', 'wind_fresh_breeze', 'wind_hurricane', 'wind_moderate_breeze', 'wind_storm', 'wind_strong', 'wind_strong_breeze', 'wind_very_strong', 'wind_violent_storm'] | True | - | the notifications for Wind_speed, see [__Notifier__](Notifier.md) | 
  | path | str | False | - | path to the specific hardware element | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 

## List of [Notifications](Notifier.md) for  __Wind_speed__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | high_wind | wind 60 km/h | 
  | wind_fresh_breeze | wind 38 km/h | 
  | wind_hurricane | wind > 120 km/h | 
  | wind_moderate_breeze | wind 28 km/h | 
  | wind_storm | wind 100 km/h | 
  | wind_strong | wind 74 km/h | 
  | wind_strong_breeze | wind 50 km/h | 
  | wind_very_strong | wind 88 km/h | 
  | wind_violent_storm | wind 117 km/h | 

## List of [method_things] for  __Wind_speed__:

  | Method Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | wind_gust | Wind_gust | {'descr': 'the wind_gust is the highest wind in a 4 second measurement whereby the wind_speed is the average of last 5 measurements', 'short': 'wind_gust'} | 
<!--e_tbl_wsp-->

## 'Wind_gust' Thing

<!--s_descr__wgst-->
Wind speed meter device

<!--e_descr_wgst-->

<!--s_tbl_wgst-->
## List of [properties](Properties.md) for __Wind_gust__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | i_read | str | True | - | the type of data that this sensor reads | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['high_wind', 'wind_fresh_breeze', 'wind_hurricane', 'wind_moderate_breeze', 'wind_storm', 'wind_strong', 'wind_strong_breeze', 'wind_very_strong', 'wind_violent_storm'] | True | - | the notifications for Wind_speed, see [__Notifier__](Notifier.md) | 
  | play | tuple:virtual_tuples | True | - | the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on' | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | threshold | float | False | - | the minimum % that an analog input must change before the value is considered changed | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 

## List of [Notifications](Notifier.md) for  __Wind_gust__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | high_wind | wind 60 km/h | 
  | wind_fresh_breeze | wind 38 km/h | 
  | wind_hurricane | wind > 120 km/h | 
  | wind_moderate_breeze | wind 28 km/h | 
  | wind_storm | wind 100 km/h | 
  | wind_strong | wind 74 km/h | 
  | wind_strong_breeze | wind 50 km/h | 
  | wind_very_strong | wind 88 km/h | 
  | wind_violent_storm | wind 117 km/h | 

## List of [copy_things] for  __Wind_gust__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_wgst-->

## 'Rain_gauge' Thing

<!--s_descr_wsrg-->
Rain gauge meter device

<!--e_descr_wsrg-->

<!--s_tbl_wsrg-->
## List of [properties](Properties.md) for __Rain_gauge__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | mm_per_rev | float | False | - | mm rain per revolve | 
  | notifications | ['rain_flooding', 'rain_lot', 'rain_nice', 'rain_tickle'] | True | - | the notifications for Rain_gauge, see [__Notifier__](Notifier.md) | 
  | path | str | False | - | path to the specific hardware element | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 

## List of [Notifications](Notifier.md) for  __Rain_gauge__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | rain_flooding | > 10mm/m2 of rain | 
  | rain_lot | > 5mm/m2 of rain | 
  | rain_nice | > 2mm/m2 of rain | 
  | rain_tickle | > 1mm/m2 rain | 

## List of [copy_things] for  __Rain_gauge__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_wsrg-->

## 'Meter' Thing

<!--s_descr_wsm-->
Meter to register utility usage or flow

<!--e_descr_wsm-->

<!--s_tbl_wsm-->
## List of [properties](Properties.md) for __Meter__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect | valid_list | False | - | effect of utility measured, + for adding, - for reducing and +- or -+ for a hybrid node where it can add or reduce | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | i_read | str | False | - | type of utility measured | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | method_things | ['fake_sensor', 'minus_meter', 'plus_meter', 'sensor'] | True | - | special methods of this thing, mostly realised through things | 
  | notifications | ['app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'notify+', 'payload_no', 'sum_day>{d}', 'sum_hour>{h}', 'sum_min>{m}', 'sum_month>{M}', 'sum_month[]>{M}', 'sum_now>{cur_state}', 'sum_week>{w}', 'sum_weekday[]>{d}', 'sum_year>{y}'] | True | - | the notifications for Meter, see [__Notifier__](Notifier.md) | 
  | path | str, str_list | False | - | path to the specific hardware element | 
  | place | str | True | - | place/room where the meter can be found, must be one of the places/rooms or an parse error is given | 
  | rate | dict | True | - | rate per effect and per unit to determine utility usage cost, can be a dict specifying different rates during the day or for weekdays | 
  | rate_fictive | dict | True | - | fictive rate per effect and per unit to determine utility usage cost, can be a dict specifying different rates during the day or for weekdays.  An example is a fictive rate for hot domestic water, the cost of water and heating is already in other utilities, but calculating and printing the cost of heated water on itself can provide useful information. | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | threshold | float | False | - | the minimum % that an analog input must change before the value is considered changed | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 
  | where2find | str | True | - | description of the physical location where the meter can be found | 

## List of [Notifications](Notifier.md) for  __Meter__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | notify+ | extra notifications | 
  | payload_no | the requested payload is refused | 
  | sum_day>{d} | if the current day sum is above (>), below (<) or equal (=) to d | 
  | sum_hour>{h} | if the sum of the last hour ago is above (>), below (<) or equal (=) to h | 
  | sum_min>{m} | if the sum of the last minute ago is above (>), below (<) or equal (=) to m | 
  | sum_month>{M} | if the current month sum is above (>), below (<) or equal (=) to M | 
  | sum_month[]>{M} | if the current month is in [..] and the sum is above (>), below (<) or equal (=) to M | 
  | sum_now>{cur_state} | if the current meter level is > cur_state | 
  | sum_week>{w} | if the current week sum is above (>), below (<) or equal (=) to w | 
  | sum_weekday[]>{d} | if the current week day position (monday=1) in [] and that day sum is above (>), below (<) or equal (=) to d | 
  | sum_year>{y} | if the current year sum is above (>), below (<) or equal (=) to y | 

## List of [copy_things] for  __Meter__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 

## List of [method_things] for  __Meter__:

  | Method Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | fake_sensor | Fake_sensor | {'descr': 'virtual sensor associated with the meter, such as power for an electricity meter or temperature for heated water', 'short': 'fake_sensor'} | 
  | minus_meter | Meter | {'descr': 'a sub meter registering all minus effects, such as an export electricity meter or an outbound liquid flow', 'short': 'plus_meter'} | 
  | plus_meter | Meter | {'descr': 'a sub meter registering all plus effects, such as an import electricity meter or an inbound liquid flow', 'short': 'plus_meter'} | 
  | sensor | Sensor | {'descr': 'the sensor associated with the meter, such as power for an electricity meter or temperature for heated water', 'short': 'sensor'} | 
<!--e_tbl_wsm-->

## 'Alarm_detector' Thing

<!--s_descr_ad-->
Alarm_detector description

<!--e_descr_ad-->

<!--s_tbl_ad-->
## List of [properties](Properties.md) for __Alarm_detector__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | active | valid_set_int | False | - | designate the active state for a binary thing, either 0 or 1 | 
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | descr_01 | list-2 | False | - | description for a binary thing when payload value is 0 or 1 | 
  | detector_type | valid_list | False | - | is the detector type such as burglar, tamper, alarm,.. | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'inactive', 'notify_binary+', 'payload_no'] | True | - | the notifications for inputs, see [__Notifier__](Notifier.md) | 
  | path | str, str_list | False | - | path to the specific hardware element | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 
  | where2find | str | True | - | where to find in the room or place | 

## List of [Notifications](Notifier.md) for  __Alarm_detector__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is non zero | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | inactive | when payload is zero | 
  | notify_binary+ | extra notifications that apply to all binary type things | 
  | payload_no | the requested payload is refused | 

## List of [copy_things] for  __Alarm_detector__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_ad-->
 
## 'Fire_detector' Thing

<!--s_descr_fd-->
Input description, works also for the derived classes

<!--e_descr_fd-->

<!--s_tbl_fd-->
## List of [properties](Properties.md) for __Fire_detector__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | active | valid_set_int | False | - | designate the active state for a binary thing, either 0 or 1 | 
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | descr_01 | list-2 | False | - | description for a binary thing when payload value is 0 or 1 | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'inactive', 'notify_binary+', 'payload_no'] | True | - | the notifications for inputs, see [__Notifier__](Notifier.md) | 
  | path | str, str_list | False | - | path to the specific hardware element | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 
  | where2find | str | True | - | where to find in the room or place | 

## List of [Notifications](Notifier.md) for  __Fire_detector__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is non zero | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | inactive | when payload is zero | 
  | notify_binary+ | extra notifications that apply to all binary type things | 
  | payload_no | the requested payload is refused | 

## List of [copy_things] for  __Fire_detector__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_fd-->
 
## 'Button' Thing

<!--s_descr_bt-->
Input description, works also for the derived classes

<!--e_descr_bt-->

<!--s_tbl_bt-->
## List of [properties](Properties.md) for __Button__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | active | valid_set_int | False | - | designate the active state for a binary thing, either 0 or 1 | 
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | descr_01 | list-2 | False | - | description for a binary thing when payload value is 0 or 1 | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'inactive', 'notify_binary+', 'payload_no'] | True | - | the notifications for inputs, see [__Notifier__](Notifier.md) | 
  | path | str, str_list | False | - | path to the specific hardware element | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 
  | where2find | str | True | - | where to find in the room or place | 

## List of [Notifications](Notifier.md) for  __Button__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is non zero | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | inactive | when payload is zero | 
  | notify_binary+ | extra notifications that apply to all binary type things | 
  | payload_no | the requested payload is refused | 

## List of [copy_things] for  __Button__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_bt-->
 
## 'Optical' Thing

<!--s_descr_op-->
Input description, works also for the derived classes

<!--e_descr_op-->

<!--s_tbl_op-->
## List of [properties](Properties.md) for __Optical__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | active | valid_set_int | False | - | designate the active state for a binary thing, either 0 or 1 | 
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | descr_01 | list-2 | False | - | description for a binary thing when payload value is 0 or 1 | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'inactive', 'notify_binary+', 'payload_no'] | True | - | the notifications for inputs, see [__Notifier__](Notifier.md) | 
  | path | str, str_list | False | - | path to the specific hardware element | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 
  | where2find | str | True | - | where to find in the room or place | 

## List of [Notifications](Notifier.md) for  __Optical__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is non zero | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | inactive | when payload is zero | 
  | notify_binary+ | extra notifications that apply to all binary type things | 
  | payload_no | the requested payload is refused | 

## List of [copy_things] for  __Optical__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_op-->
 
## 'Switch' Thing

<!--s_descr_sw-->
Input description, works also for the derived classes

<!--e_descr_sw-->

<!--s_tbl_sw-->
## List of [properties](Properties.md) for __Switch__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | active | valid_set_int | False | - | designate the active state for a binary thing, either 0 or 1 | 
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | descr_01 | list-2 | False | - | description for a binary thing when payload value is 0 or 1 | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'inactive', 'notify_binary+', 'payload_no'] | True | - | the notifications for inputs, see [__Notifier__](Notifier.md) | 
  | path | str, str_list | False | - | path to the specific hardware element | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 
  | where2find | str | True | - | where to find in the room or place | 

## List of [Notifications](Notifier.md) for  __Switch__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is non zero | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | inactive | when payload is zero | 
  | notify_binary+ | extra notifications that apply to all binary type things | 
  | payload_no | the requested payload is refused | 

## List of [copy_things] for  __Switch__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_sw-->

## List of notification types

### notify+

<!--s_insert_{"prj_parser":"class_doc.conf","section":"MORE+","var":"notify"}-->

from class_doc.conf:
```python3
[MORE+]

notify={
	"app_done":"when a things_app completes",
	"app_start":"when a things_app starts",
	"disable_off":"when all of the disable conditions fail",
	"disable_on":"when one of the disable conditions succeed",
	"enable_off":"when one of the enable conditions fail",
	"enable_on":"when all the enable conditions succeed",
	"freeze_off":"all of the freeze conditions fail",
	"freeze_on":"one of the freeze conditions succeed",
	"payload_no":"the requested payload is refused"}

```

<!--e_insert-->


### notify_analog+

<!--s_insert_{"prj_parser":"class_doc.conf","section":"MORE+","var":"notify_analog"}-->

from class_doc.conf:
```python3
[MORE+]

notify_analog={
	"app_done":"when a things_app completes",
	"app_start":"when a things_app starts",
	"disable_off":"when all of the disable conditions fail",
	"disable_on":"when one of the disable conditions succeed",
	"enable_off":"when one of the enable conditions fail",
	"enable_on":"when all the enable conditions succeed",
	"freeze_off":"all of the freeze conditions fail",
	"freeze_on":"one of the freeze conditions succeed",
	"payload_no":"the requested payload is refused",
	"high":"when payload reaches high",
	"low":"when payload reaches low",
	"normal":"when payload becomes lower than high or higher than low",
	"active":"when payload is non zero",
	"inactive":"when payload is zero",
	"deicing":"temperature becomes positive",
	"freezing":"temperature becomes below zero",
	"positive":"when payload reaches positive or zero coming from a negative payload",
	"negative":"when payload reaches negative, coming from a positive payload"}

```

<!--e_insert-->


### notify_binary+

<!--s_insert_{"prj_parser":"class_doc.conf","section":"MORE+","var":"notify_binary"}-->

from class_doc.conf:
```python3
[MORE+]

notify_binary={
	"app_done":"when a things_app completes",
	"app_start":"when a things_app starts",
	"disable_off":"when all of the disable conditions fail",
	"disable_on":"when one of the disable conditions succeed",
	"enable_off":"when one of the enable conditions fail",
	"enable_on":"when all the enable conditions succeed",
	"freeze_off":"all of the freeze conditions fail",
	"freeze_on":"one of the freeze conditions succeed",
	"payload_no":"the requested payload is refused",
	"active":"when payload is non zero",
	"inactive":"when payload is zero"}

```

<!--e_insert-->


* * *
* * *
# Parsing Reporting Example

Detailed device reporting is generated by every raspberry when the program starts, but comes emailed  from the deployer.

See below for an example of the extend of the reporting that is available.

see the section ```Per Raspberry/Arduino/ZWAVE, Physical IO Items```

see the section ```Statistics Classes and Statistics Options``` almost at the end.

* * *
* * *

<!--s_insert_{"role":"deploy","suffix":"ref"}-->


[imac-lucy_ref.html](imac-lucy_ref.html)
<!DOCTYPE html><html><body><h1>Report_ref -> imac-lucy_ref.html  2021/02/07 11:25:57</h1>

<!--e_insert-->

* * *
* * *

