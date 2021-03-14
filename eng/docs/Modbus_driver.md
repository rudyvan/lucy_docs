<!--s_name-->
# Modbus_driver

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
is the driver for Modbus

<!--e_descr-->

Several devices work with a modbus interface and therefore a simple modbus implementation is provided with the open source 
library from https://minimalmodbus.readthedocs.io/en

An example device is the modbus version of a din rail smart energy meter for single and three phase electrical systems from Eastron.

![EASTRON SDM630 V2 100A](eastron_sdm630.jpg)

through the modbus driver it is possible to extract the fields of this device and use the result in lucy.

The mapping from modbus devices to lucy things has to be defined in a file:

<!--s_insert_{"prj_parser":"app_obj.conf","sections":["MODBUS"],"vars":["devices"]}-->

from app_obj.conf:
```python3
[MODBUS]

devices={
	"EASTRON_SDM630V2": {
	"name": "Eastron SDM630V2",
	"data_points": [
	{ "modbus_addr": 0x00, "name": "L1_V", "description": "L1 Line to Neutral (V)", "type": "float", "th": "Sensor", "unit":"V"},
	{ "modbus_addr": 0x02, "name": "L2_V", "description": "L2 Line to Neutral (V)", "type": "float", "th": "Sensor", "unit":"V" },
	{ "modbus_addr": 0x04, "name": "L3_V", "description": "L3 Line to Neutral (V)", "type": "float", "th": "Sensor", "unit":"V" },
	
	{ "modbus_addr": 0xC8, "name": "L1L2_V", "description": "L1 Line to L2 (V)", "type": "float", "th": "Sensor", "unit":"V" },
	{ "modbus_addr": 0xCA, "name": "L2L3_V", "description": "L2 Line to L3 (V)", "type": "float", "th": "Sensor", "unit":"V" },
	{ "modbus_addr": 0xCC, "name": "L3L1_V", "description": "L3 Line to L1 (V)", "type": "float", "th": "Sensor", "unit":"V" },
	
	{ "modbus_addr": 0x06, "name": "L1_A", "description": "L1 Current (A)", "type": "float", "th": "Sensor", "unit":"A" },
	{ "modbus_addr": 0x08, "name": "L2_A", "description": "L2 Current (A)", "type": "float", "th": "Sensor", "unit":"A" },
	{ "modbus_addr": 0x0A, "name": "L3_A", "description": "L3 Current (A)", "type": "float", "th": "Sensor", "unit":"A" },
	{ "modbus_addr": 0xE0, "name": "N_A", "description": "Neutral Current (A)", "type": "float", "th": "Sensor", "unit":"A" },
	
	{ "modbus_addr": 0x0C, "name": "L1_W", "description": "L1 Power (W)", "type": "float", "th": "Sensor", "unit":"W" },
	{ "modbus_addr": 0x0E, "name": "L2_W", "description": "L2 Power (W)", "type": "float", "th": "Sensor", "unit":"W" },
	{ "modbus_addr": 0x10, "name": "L3_W", "description": "L3 Power (W)", "type": "float", "th": "Sensor", "unit":"W" },
	
	{ "modbus_addr": 0x12, "name": "L1_VA", "description": "L1 Volt Amps (VA)", "type": "float", "th": "Sensor", "unit":"VA" },
	{ "modbus_addr": 0x14, "name": "L2_VA", "description": "L2 Volt Amps (VA)", "type": "float", "th": "Sensor", "unit":"VA" },
	{ "modbus_addr": 0x16, "name": "L3_VA", "description": "L3 Volt Amps (VA)", "type": "float", "th": "Sensor", "unit":"VA" },
	
	{ "modbus_addr": 0x34, "name": "Tot_W", "description": "Total System Power (W)", "type": "float", "th": "Sensor", "unit":"W" },
	{ "modbus_addr": 0x38, "name": "Tot_VA", "description": "Total System Volt Amps (VA)", "type": "float", "th": "Sensor", "unit":"VA" },
	{ "modbus_addr": 0x0156, "name": "Tot_kWh", "description": "Total Energy (kWh)", "type": "float", "th": "Sensor", "unit":"kWh" },
	{ "modbus_addr": 0x46, "name": "LineFrequency_Hz", "description": "Line frequency (Hz)", "type": "float", "th": "Sensor", "unit":"Hz" },
	
	{ "modbus_addr": 0x48, "name": "EnergyImported_kWh", "description": "Energy Imported Accumulated (kWh)", "type": "float", "th": "Sensor", "unit":"kWh" },
	{ "modbus_addr": 0x4A, "name": "EnergyExported_kWh", "description": "Energy Exported Accumulated (kWh)", "type": "float", "th": "Sensor", "unit":"kWh" },
	
	{ "modbus_addr": 0x54, "name": "N_MAX_A", "description": "Neutral Maximum Current (A)", "type": "float", "th": "Sensor", "unit":"A" },
	{ "modbus_addr": 0x0108, "name": "L1_MAX_A", "description": "L1 Maximum Current (A)", "type": "float", "th": "Sensor", "unit":"A" },
	{ "modbus_addr": 0x010A, "name": "L2_MAX_A", "description": "L2 Maximum Current (A)", "type": "float", "th": "Sensor", "unit":"A" },
	{ "modbus_addr": 0x010C, "name": "L3_MAX_A", "description": "L3 Maximum Current (A)", "type": "float", "th": "Sensor", "unit":"A" }
	]
	}}

```

<!--e_insert-->

For each such modbus device such a mapping is expected.

To specify a modbus device, one need to define a driver and a thingscontroller such as in the example below:

<!--s_insert_{"tree":["(o:Modbus_driver)","(dk:garden).*(o:Things_controllers)"]}-->

from project.py tree:['(o:Modbus_driver)', '(dk:garden).*(o:Things_controllers)']
```python3
# --> project.py :<dk:project,o:Project,kw:drivers,lp:8,o:Modbus_driver>

from lucy_app import *

Modbus_driver(
    notifications = {
            "modbus_parsing":Mail(subject='Modbus Parsing{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='modbus', files2mail=None, ceiling=None)},
    role_me = "imac-lucy")

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:garden,o:Place,kw:contents,lp:1,o:Things_controllers>

from lucy_app import *

Things_controllers(items = {
            "PI-Garden":Raspi(hw_gws = ["unipi:8,14"],path = "ip:192.168.15.55"),
            "PI-Gate":Raspi(hw_gws = ["unipi:16,14"],path = "ip:192.168.15.121"),
            "PI-Pool":Raspi(hw_gws = ["unipi:16,14"],path = "ip:192.168.15.194"),
            "PI-Soccer":Raspi(hw_gws = ["unipi:6,6"],path = "ip:192.168.15.78"),
            "pool_energy":Modbus(path = "usb:PI-Pool,RS485,1,EASTRON_SDM630V2,Tot_kWh+Tot_W")})

```

<!--e_insert-->




<!--s_tbl-->
## List of [properties](Properties.md) for __Modbus_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | notifications | ['modbus_parsing'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 
  | role_me | {tc} | False | - | role_me of 'Modbus_driver', adds <modbus_drv> to the roles of the specified tc | 

## List of [Notifications](Notifier.md) for  __Modbus_driver__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | modbus_parsing | when this report runs | 

## List of [Errors/Warnings](Error_Warn.md) for  __Modbus_driver__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_mb_bad | !!Modbus {} does not access : {} |  
  | err_mb_dev | !!Modbus {} has {} not in {} |  
  | err_mb_ns | !!Modbus {} not yet supported |  
  | err_mb_type | !!Modbus {} is <{}> type but should be {} |  
<!--e_tbl-->

## Modbus parsing report

* * * 
* * * 

<!--s_insert_{"role":"modbus_drv","suffix":"modbus"}-->


[imac-lucy_modbus.html](imac-lucy_modbus.html)

<!DOCTYPE html><html><body><h1>Modbus Analyzed -> imac-lucy_modbus.html  2021/03/13 09:59:04</h1><h2>Modbus Discovery & Things Match</h2><table><thead><tr><th>mb:name/device</th><th>mb:path</th><th>myproject.py/place</th><th>myproject.py/name</th><th>Analysis</th></tr></thead><tbody><tr><td style='background-color:cyan;text-align:center' colspan='5'>*** modbus 1 defined</td></tr><tr><td>pool_energy</td><td>usb:PI-Pool,RS485,1,EASTRON_SDM630V2,Tot_kWh+Tot_W</td><td>garden</td><td>pool_energy^Tot_kWh</td><td>ok:match</td></tr><tr><td>pool_energy</td><td>usb:PI-Pool,RS485,1,EASTRON_SDM630V2,Tot_kWh+Tot_W</td><td>garden</td><td>pool_energy^Tot_W</td><td>ok:match</td></tr></tbody></table></body></html>
<!--e_insert-->

* * * 
* * * 
