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
	{ "modbus_addr": 0x38, "name": "Tot_VA", "description": "Total System Volt Amps (VA)", "type": "float", "th": "Meter", "unit":"VA" },
	{ "modbus_addr": 0x0156, "name": "Tot_kWh", "description": "Total Energy (kWh)", "type": "float", "th": "Meter", "unit":"kWh", "cum": True },
	{ "modbus_addr": 0x46, "name": "LineFrequency_Hz", "description": "Line frequency (Hz)", "type": "float", "th": "Sensor", "unit":"Hz" },
	
	{ "modbus_addr": 0x48, "name": "EnergyImported_kWh", "description": "Energy Imported Accumulated (kWh)", "type": "float", "th": "Meter", "unit":"kWh", "cum": True },
	{ "modbus_addr": 0x4A, "name": "EnergyExported_kWh", "description": "Energy Exported Accumulated (kWh)", "type": "float", "th": "Meter", "unit":"kWh", "cum": True },
	
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
            "modbus_forensics":Mail(subject='Modbus Forensics{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='modbus_forensics', files2mail=None, ceiling=None),
            "modbus_parsing":Mail(subject='Modbus Parsing{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='modbus', files2mail=None, ceiling=None)},
    role_me = "PI-Energy")

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:garden,o:Place,kw:contents,lp:1,o:Things_controllers>

from lucy_app import *

Things_controllers(items = {
            "PI-Garden":Raspi(hw_gws = ["unipi:8,14"],path = "ip:192.168.15.55"),
            "PI-Gate":Raspi(hw_gws = ["unipi:16,14"],path = "ip:192.168.15.121"),
            "PI-Soccer":Raspi(hw_gws = ["unipi:6,6"],path = "ip:192.168.15.78")})

```

<!--e_insert-->




<!--s_tbl-->
## List of [properties](Properties.md) for __Modbus_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | notifications | ['modbus_forensics', 'modbus_parsing'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 
  | role_me | {tc} | False | - | role_me of 'Modbus_driver', adds <modbus_drv> to the roles of the specified tc | 

## List of [Notifications](Notifier.md) for  __Modbus_driver__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | modbus_forensics | this report runs at then end of the day to list all modbus modbus thingscontrollers data | 
  | modbus_parsing | this report runs when parsing of modbus thingscontrollers is complete | 

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


[PI-Energy_modbus.html](PI-Energy_modbus.html)

<!DOCTYPE html><html><body><h1>Modbus Analyzed -> PI-Energy_modbus.html  2021/03/28 18:29:00</h1><h2>Modbus Discovery & Things Match</h2><table><thead><tr><th>mb:name/device</th><th>mb:path</th><th>myproject.py/place</th><th>myproject.py/name</th><th>Analysis</th></tr></thead><tbody><tr><td style='background-color:cyan;text-align:center' colspan='5'>*** modbus 3 defined</td></tr><tr><td>main_energy</td><td>usb:PI-Energy,RS485,1,EASTRON_SDM630V2,Tot_kWh+Tot_W</td><td>-</td><td>electricity^mains_power^sensor</td><td>ok:match</td></tr><tr><td>main_energy</td><td>usb:PI-Energy,RS485,1,EASTRON_SDM630V2,Tot_kWh+Tot_W</td><td>-</td><td>electricity^mains_power</td><td>ok:match</td></tr><tr><td>solar_energy</td><td>usb:PI-Energy,RS485,2,EASTRON_SDM630V2,Tot_kWh+Tot_W</td><td>-</td><td>electricity^solar_power^sensor</td><td>ok:match</td></tr><tr><td>solar_energy</td><td>usb:PI-Energy,RS485,2,EASTRON_SDM630V2,Tot_kWh+Tot_W</td><td>-</td><td>electricity^solar_power</td><td>ok:match</td></tr><tr><td>car_energy</td><td>usb:PI-Energy,RS485,3,EASTRON_SDM630V2,Tot_kWh+Tot_W</td><td>-</td><td>electricity^car_charger^sensor</td><td>ok:match</td></tr><tr><td>car_energy</td><td>usb:PI-Energy,RS485,3,EASTRON_SDM630V2,Tot_kWh+Tot_W</td><td>-</td><td>electricity^car_charger</td><td>ok:match</td></tr></tbody></table></body></html>
<!--e_insert-->

* * * 
* * * 
## Modbus forensics report

* * * 
* * * 

<!--s_insert_{"role":"modbus_drv","suffix":"modbus_forensics"}-->


[PI-Energy_modbus_forensics.html](PI-Energy_modbus_forensics.html)

<!DOCTYPE html><html><body><h1>Modbus_forensics -> PI-Energy_modbus_forensics.html  2021/03/29 00:01:30</h1><h2>Modbus Forensics</h2><table><thead><tr><th>field</th><th>description</th><th>val</th><th style='text-align:center'>today</th><th style='text-align:center'>lowest &lt;--&gt; highest</th><th style='text-align:center'>low/high_when</th></tr></thead><tbody><tr><td style='background-color:cyan;text-align:center' colspan='6'>Modbus: &lt;main_energy&gt;</td></tr><tr><td>EnergyExported_kWh</td><td>Energy Exported Accumulated (kWh)</td><td>17.16 kWh</td><td style='text-align:center'>8.36 kWh</td><td style='text-align:center'>8.80 .. 17.16</td><td style='text-align:center'>18:29 / 00:01</td></tr><tr><td>EnergyImported_kWh</td><td>Energy Imported Accumulated (kWh)</td><td>0.02 kWh</td><td style='text-align:center'>0.00 kWh</td><td style='text-align:center'>0.02 .. 0.02</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L1L2_V</td><td>L1 Line to L2 (V)</td><td>404.24 V</td><td style='text-align:center'>-</td><td style='text-align:center'>390.82 .. 409.19</td><td style='text-align:center'>18:51 / 23:47</td></tr><tr><td>L1_A</td><td>L1 Current (A)</td><td>2.67 A</td><td style='text-align:center'>-</td><td style='text-align:center'>2.16 .. 17.00</td><td style='text-align:center'>18:30 / 19:14</td></tr><tr><td>L1_MAX_A</td><td>L1 Maximum Current (A)</td><td>3.58 A</td><td style='text-align:center'>-</td><td style='text-align:center'>2.75 .. 3.58</td><td style='text-align:center'>18:29 / 20:12</td></tr><tr><td>L1_V</td><td>L1 Line to Neutral (V)</td><td>228.84 V</td><td style='text-align:center'>-</td><td style='text-align:center'>220.36 .. 236.70</td><td style='text-align:center'>21:38 / 20:18</td></tr><tr><td>L1_VA</td><td>L1 Volt Amps (VA)</td><td>612.45 VA</td><td style='text-align:center'>-</td><td style='text-align:center'>498.61 .. 3803.50</td><td style='text-align:center'>18:29 / 19:14</td></tr><tr><td>L1_W</td><td>L1 Power (W)</td><td>-509.99 W</td><td style='text-align:center'>-</td><td style='text-align:center'>-3789.43 .. -420.59</td><td style='text-align:center'>19:14 / 18:29</td></tr><tr><td>L2L3_V</td><td>L2 Line to L3 (V)</td><td>410.38 V</td><td style='text-align:center'>-</td><td style='text-align:center'>390.79 .. 415.33</td><td style='text-align:center'>19:23 / 23:42</td></tr><tr><td>L2_A</td><td>L2 Current (A)</td><td>1.91 A</td><td style='text-align:center'>-</td><td style='text-align:center'>1.07 .. 8.84</td><td style='text-align:center'>18:34 / 21:04</td></tr><tr><td>L2_MAX_A</td><td>L2 Maximum Current (A)</td><td>2.30 A</td><td style='text-align:center'>-</td><td style='text-align:center'>1.40 .. 2.30</td><td style='text-align:center'>18:29 / 20:28</td></tr><tr><td>L2_V</td><td>L2 Line to Neutral (V)</td><td>237.92 V</td><td style='text-align:center'>-</td><td style='text-align:center'>222.11 .. 241.77</td><td style='text-align:center'>18:30 / 23:45</td></tr><tr><td>L2_VA</td><td>L2 Volt Amps (VA)</td><td>456.14 VA</td><td style='text-align:center'>-</td><td style='text-align:center'>246.65 .. 2025.54</td><td style='text-align:center'>18:34 / 21:04</td></tr><tr><td>L2_W</td><td>L2 Power (W)</td><td>-205.63 W</td><td style='text-align:center'>-</td><td style='text-align:center'>-2018.52 .. -58.42</td><td style='text-align:center'>21:04 / 18:32</td></tr><tr><td>L3L1_V</td><td>L3 Line to L1 (V)</td><td>402.70 V</td><td style='text-align:center'>-</td><td style='text-align:center'>387.45 .. 407.04</td><td style='text-align:center'>19:14 / 23:39</td></tr><tr><td>L3_A</td><td>L3 Current (A)</td><td>2.96 A</td><td style='text-align:center'>-</td><td style='text-align:center'>2.60 .. 8.23</td><td style='text-align:center'>19:38 / 18:48</td></tr><tr><td>L3_MAX_A</td><td>L3 Maximum Current (A)</td><td>4.46 A</td><td style='text-align:center'>-</td><td style='text-align:center'>4.46 .. 4.46</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L3_V</td><td>L3 Line to Neutral (V)</td><td>236.09 V</td><td style='text-align:center'>-</td><td style='text-align:center'>221.37 .. 239.22</td><td style='text-align:center'>19:23 / 23:22</td></tr><tr><td>L3_VA</td><td>L3 Volt Amps (VA)</td><td>717.49 VA</td><td style='text-align:center'>-</td><td style='text-align:center'>587.46 .. 2846.00</td><td style='text-align:center'>19:38 / 22:08</td></tr><tr><td>L3_W</td><td>L3 Power (W)</td><td>-532.82 W</td><td style='text-align:center'>-</td><td style='text-align:center'>-2572.15 .. -473.85</td><td style='text-align:center'>22:08 / 19:38</td></tr><tr><td>LineFrequency_Hz</td><td>Line frequency (Hz)</td><td>49.91 Hz</td><td style='text-align:center'>-</td><td style='text-align:center'>49.81 .. 50.00</td><td style='text-align:center'>23:02 / 19:02</td></tr><tr><td>N_A</td><td>Neutral Current (A)</td><td>0.93 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.22 .. 14.29</td><td style='text-align:center'>19:39 / 19:15</td></tr><tr><td>N_MAX_A</td><td>Neutral Maximum Current (A)</td><td>-1381.89 A</td><td style='text-align:center'>-</td><td style='text-align:center'>-1724.35 .. -1350.42</td><td style='text-align:center'>20:12 / 19:11</td></tr><tr><td>Tot_VA</td><td>Total System Volt Amps (VA)</td><td>1760.62 VA</td><td style='text-align:center'>-</td><td style='text-align:center'>1434.18 .. 5003.57</td><td style='text-align:center'>18:34 / 19:14</td></tr><tr><td>Tot_W</td><td>Total System Power (W)</td><td>-1251.57 W</td><td style='text-align:center'>-</td><td style='text-align:center'>-6098.53 .. -1056.20</td><td style='text-align:center'>19:15 / 18:33</td></tr><tr><td>Tot_kWh</td><td>Total Energy (kWh)</td><td>17.18 kWh</td><td style='text-align:center'>8.36 kWh</td><td style='text-align:center'>8.82 .. 17.18</td><td style='text-align:center'>18:29 / 00:01</td></tr><tr><td style='background-color:cyan;text-align:center' colspan='6'>Modbus: &lt;solar_energy&gt;</td></tr><tr><td>EnergyExported_kWh</td><td>Energy Exported Accumulated (kWh)</td><td>0.00 kWh</td><td style='text-align:center'>0.00 kWh</td><td style='text-align:center'>0.00 .. 0.00</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>EnergyImported_kWh</td><td>Energy Imported Accumulated (kWh)</td><td>1.25 kWh</td><td style='text-align:center'>0.24 kWh</td><td style='text-align:center'>1.01 .. 1.25</td><td style='text-align:center'>18:29 / 19:46</td></tr><tr><td>L1L2_V</td><td>L1 Line to L2 (V)</td><td>409.95 V</td><td style='text-align:center'>-</td><td style='text-align:center'>390.85 .. 415.23</td><td style='text-align:center'>19:12 / 23:42</td></tr><tr><td>L1_A</td><td>L1 Current (A)</td><td>0.32 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.15 .. 0.56</td><td style='text-align:center'>19:25 / 18:31</td></tr><tr><td>L1_MAX_A</td><td>L1 Maximum Current (A)</td><td>0.76 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.76 .. 0.76</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L1_V</td><td>L1 Line to Neutral (V)</td><td>235.57 V</td><td style='text-align:center'>-</td><td style='text-align:center'>220.47 .. 238.83</td><td style='text-align:center'>19:13 / 23:22</td></tr><tr><td>L1_VA</td><td>L1 Volt Amps (VA)</td><td>74.71 VA</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 124.19</td><td style='text-align:center'>19:47 / 18:31</td></tr><tr><td>L1_W</td><td>L1 Power (W)</td><td>0.00 W</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 124.46</td><td style='text-align:center'>19:47 / 18:31</td></tr><tr><td>L2L3_V</td><td>L2 Line to L3 (V)</td><td>404.36 V</td><td style='text-align:center'>-</td><td style='text-align:center'>390.33 .. 409.58</td><td style='text-align:center'>18:52 / 23:41</td></tr><tr><td>L2_A</td><td>L2 Current (A)</td><td>0.33 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.14 .. 0.56</td><td style='text-align:center'>19:47 / 18:29</td></tr><tr><td>L2_MAX_A</td><td>L2 Maximum Current (A)</td><td>0.77 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.77 .. 0.77</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L2_V</td><td>L2 Line to Neutral (V)</td><td>237.86 V</td><td style='text-align:center'>-</td><td style='text-align:center'>223.92 .. 241.94</td><td style='text-align:center'>18:30 / 23:45</td></tr><tr><td>L2_VA</td><td>L2 Volt Amps (VA)</td><td>78.31 VA</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 124.81</td><td style='text-align:center'>19:48 / 18:33</td></tr><tr><td>L2_W</td><td>L2 Power (W)</td><td>0.00 W</td><td style='text-align:center'>-</td><td style='text-align:center'>-4.33 .. 124.19</td><td style='text-align:center'>20:18 / 18:32</td></tr><tr><td>L3L1_V</td><td>L3 Line to L1 (V)</td><td>402.40 V</td><td style='text-align:center'>-</td><td style='text-align:center'>387.00 .. 406.55</td><td style='text-align:center'>19:14 / 23:39</td></tr><tr><td>L3_A</td><td>L3 Current (A)</td><td>0.34 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.14 .. 0.58</td><td style='text-align:center'>19:51 / 18:30</td></tr><tr><td>L3_MAX_A</td><td>L3 Maximum Current (A)</td><td>0.77 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.77 .. 0.77</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L3_V</td><td>L3 Line to Neutral (V)</td><td>229.05 V</td><td style='text-align:center'>-</td><td style='text-align:center'>220.52 .. 236.95</td><td style='text-align:center'>21:38 / 20:19</td></tr><tr><td>L3_VA</td><td>L3 Volt Amps (VA)</td><td>76.54 VA</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 129.82</td><td style='text-align:center'>19:51 / 18:30</td></tr><tr><td>L3_W</td><td>L3 Power (W)</td><td>0.00 W</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 130.35</td><td style='text-align:center'>19:49 / 18:30</td></tr><tr><td>LineFrequency_Hz</td><td>Line frequency (Hz)</td><td>49.92 Hz</td><td style='text-align:center'>-</td><td style='text-align:center'>49.82 .. 50.00</td><td style='text-align:center'>23:02 / 19:01</td></tr><tr><td>N_A</td><td>Neutral Current (A)</td><td>0.01 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 0.04</td><td style='text-align:center'>19:23 / 19:14</td></tr><tr><td>N_MAX_A</td><td>Neutral Maximum Current (A)</td><td>0.00 A</td><td style='text-align:center'>-</td><td style='text-align:center'>-0.01 .. 512.87</td><td style='text-align:center'>21:16 / 18:29</td></tr><tr><td>Tot_VA</td><td>Total System Volt Amps (VA)</td><td>228.55 VA</td><td style='text-align:center'>-</td><td style='text-align:center'>8.21 .. 371.07</td><td style='text-align:center'>19:51 / 18:31</td></tr><tr><td>Tot_W</td><td>Total System Power (W)</td><td>0.00 W</td><td style='text-align:center'>-</td><td style='text-align:center'>-4.04 .. 372.05</td><td style='text-align:center'>20:18 / 18:29</td></tr><tr><td>Tot_kWh</td><td>Total Energy (kWh)</td><td>1.25 kWh</td><td style='text-align:center'>0.24 kWh</td><td style='text-align:center'>1.01 .. 1.25</td><td style='text-align:center'>18:29 / 19:46</td></tr><tr><td style='background-color:cyan;text-align:center' colspan='6'>Modbus: &lt;car_energy&gt;</td></tr><tr><td>EnergyExported_kWh</td><td>Energy Exported Accumulated (kWh)</td><td>0.08 kWh</td><td style='text-align:center'>0.06 kWh</td><td style='text-align:center'>0.02 .. 0.08</td><td style='text-align:center'>18:29 / 00:00</td></tr><tr><td>EnergyImported_kWh</td><td>Energy Imported Accumulated (kWh)</td><td>0.00 kWh</td><td style='text-align:center'>0.00 kWh</td><td style='text-align:center'>0.00 .. 0.00</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L1L2_V</td><td>L1 Line to L2 (V)</td><td>409.97 V</td><td style='text-align:center'>-</td><td style='text-align:center'>390.75 .. 415.21</td><td style='text-align:center'>19:23 / 23:42</td></tr><tr><td>L1_A</td><td>L1 Current (A)</td><td>0.00 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 0.00</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L1_MAX_A</td><td>L1 Maximum Current (A)</td><td>0.00 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 0.00</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L1_V</td><td>L1 Line to Neutral (V)</td><td>235.72 V</td><td style='text-align:center'>-</td><td style='text-align:center'>221.19 .. 238.92</td><td style='text-align:center'>19:23 / 23:22</td></tr><tr><td>L1_VA</td><td>L1 Volt Amps (VA)</td><td>0.00 VA</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 0.00</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L1_W</td><td>L1 Power (W)</td><td>0.00 W</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 0.00</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L2L3_V</td><td>L2 Line to L3 (V)</td><td>404.04 V</td><td style='text-align:center'>-</td><td style='text-align:center'>390.03 .. 409.29</td><td style='text-align:center'>18:52 / 23:47</td></tr><tr><td>L2_A</td><td>L2 Current (A)</td><td>0.00 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 0.00</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L2_MAX_A</td><td>L2 Maximum Current (A)</td><td>0.00 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 0.00</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L2_V</td><td>L2 Line to Neutral (V)</td><td>237.68 V</td><td style='text-align:center'>-</td><td style='text-align:center'>222.02 .. 241.61</td><td style='text-align:center'>18:30 / 23:43</td></tr><tr><td>L2_VA</td><td>L2 Volt Amps (VA)</td><td>0.00 VA</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 0.00</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L2_W</td><td>L2 Power (W)</td><td>0.00 W</td><td style='text-align:center'>-</td><td style='text-align:center'>0.00 .. 0.00</td><td style='text-align:center'>18:29 / 18:29</td></tr><tr><td>L3L1_V</td><td>L3 Line to L1 (V)</td><td>402.33 V</td><td style='text-align:center'>-</td><td style='text-align:center'>386.83 .. 406.46</td><td style='text-align:center'>19:15 / 23:39</td></tr><tr><td>L3_A</td><td>L3 Current (A)</td><td>0.17 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.16 .. 0.29</td><td style='text-align:center'>21:39 / 22:38</td></tr><tr><td>L3_MAX_A</td><td>L3 Maximum Current (A)</td><td>0.17 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.17 .. 0.17</td><td style='text-align:center'>18:29 / 00:00</td></tr><tr><td>L3_V</td><td>L3 Line to Neutral (V)</td><td>228.97 V</td><td style='text-align:center'>-</td><td style='text-align:center'>220.49 .. 236.59</td><td style='text-align:center'>21:38 / 20:18</td></tr><tr><td>L3_VA</td><td>L3 Volt Amps (VA)</td><td>35.60 VA</td><td style='text-align:center'>-</td><td style='text-align:center'>33.07 .. 44.31</td><td style='text-align:center'>20:33 / 23:58</td></tr><tr><td>L3_W</td><td>L3 Power (W)</td><td>-9.60 W</td><td style='text-align:center'>-</td><td style='text-align:center'>-28.42 .. -8.23</td><td style='text-align:center'>20:19 / 23:45</td></tr><tr><td>LineFrequency_Hz</td><td>Line frequency (Hz)</td><td>49.94 Hz</td><td style='text-align:center'>-</td><td style='text-align:center'>49.82 .. 50.00</td><td style='text-align:center'>23:01 / 19:01</td></tr><tr><td>N_A</td><td>Neutral Current (A)</td><td>0.17 A</td><td style='text-align:center'>-</td><td style='text-align:center'>0.16 .. 0.29</td><td style='text-align:center'>21:39 / 22:38</td></tr><tr><td>N_MAX_A</td><td>Neutral Maximum Current (A)</td><td>-10.83 A</td><td style='text-align:center'>-</td><td style='text-align:center'>-11.08 .. -10.67</td><td style='text-align:center'>18:49 / 22:34</td></tr><tr><td>Tot_VA</td><td>Total System Volt Amps (VA)</td><td>34.53 VA</td><td style='text-align:center'>-</td><td style='text-align:center'>31.57 .. 43.44</td><td style='text-align:center'>22:02 / 22:48</td></tr><tr><td>Tot_W</td><td>Total System Power (W)</td><td>-9.69 W</td><td style='text-align:center'>-</td><td style='text-align:center'>-28.09 .. -8.59</td><td style='text-align:center'>23:58 / 21:41</td></tr><tr><td>Tot_kWh</td><td>Total Energy (kWh)</td><td>0.08 kWh</td><td style='text-align:center'>0.06 kWh</td><td style='text-align:center'>0.02 .. 0.08</td><td style='text-align:center'>18:29 / 00:00</td></tr></tbody></table></body></html>
<!--e_insert-->

* * * 
* * * 
