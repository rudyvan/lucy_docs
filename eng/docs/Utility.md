<!--s_name-->
# Home_utilities

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
Measures and reports utility consumption for heating, cooling, cooking, water, ... by reading utility meters and sensors.  It also reports solar and wind energy production and consumption and recharge of the home battery.

<!--e_descr-->

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

<!--s_tbl-->
## List of [properties](Properties.md) for __Home_utilities__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | consumers | dict | True | True | is a dictionary of consumers which counts when something is heating, taking energy, such as cooking, room heating or hot water tub.  CURRENTLY NOT IMPLEMENTED | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | meters | ['Utility_meter', 'Flow_meter'] | True | True | is a dictionary of meters which counts when something is heating, taking energy, such as cooking, room heating or hot water tub.  CURRENTLY NOT IMPLEMENTED | 
  | notifications | ['power', 'power_cam_shot'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 
  | producers | dict | True | True | is a dictionary of utility producers which generate water, electricity (solar panels), gas.  CURRENTLY NOT IMPLEMENTED | 
  | sensors | ['Sensor'] | False | True | is a dictionary of sensors which measures when something is heating, taking energy, such as cooking, room heating or hot water tub.  CURRENTLY NOT IMPLEMENTED | 

## List of [Notifications](Notifier.md) for  __Home_utilities__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | power |  | 
  | power_cam_shot |  | 
<!--e_tbl-->

<!--s_name_utl-->
# utility_meter

<!--e_name_utl-->

<!--s_descr_utl-->
The pysical ean meter for one of the utilities measured

<!--e_descr_utl-->

<!--s_tbl_utl-->
Allowed Objects : Meter
<!--e_tbl_utl-->

parameters:
* vid is 0=picam, 1..=usb camera 

* it is possible for 2 meters to be on the same vid, such as a night/day electricity counter

* cam_roi is specified in pixels to a 320x240 raster 4:3 aspect ratio : pt_st_hor,pt_st_vert,pt_end_hor, pt_end_vert.  Example : ```1,1,320,240``` (coordinates rect)
* digit_format is the representation of digits in the counter

  --> X is a white digit on a black background, x is the inverse    
  --> use "." to separate whole and fractions
  --> they should be evenly spaced in the horizontal roi (region of interest)
* value is a float and the cost per unit in € and is used to show a day cost
* the "_day" and "_night" suffix have a special purpose and allow one camera image to produce 2 cntrs

# Example


<!--s_insert_{"tree":"(o:Home_utilities)"}-->

from project.py tree:(o:Home_utilities)
```python3
# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:garage_dressing,o:Room,kw:contents,lp:6,o:Home_utilities>

from lucy_app import *

Home_utilities(
    meters = {
            "domestic_hot_water":Flow_meter(path = "unipi:PI-Climate,input,6",q_per_rev = 1.0),
            "domestic_water":Flow_meter(path = "unipi:PI-Climate,input,5",q_per_rev = 10.0),
            "electricity_day":Utility_meter(path = "ean:PI-Climate,electricity,541448820048316727,4117-Piek,XXXXXX00,kW/h,0.25,,,"),
            "electricity_night":Utility_meter(path = "ean:PI-Climate,electricity,541448820048316727,4117-Dal,XXXXXX00,kW/h,0.125,,,"),
            "gas":Utility_meter(path = "ean:PI-Climate,gas,41448820048316734,6237,XXXXX.x,m3,0.4078,kwH,9.99,"),
            "gas_boiler":Flow_meter(path = "unipi:PI-Climate,input,7",q_per_rev = 10.0),
            "pool_water":Flow_meter(path = "unipi:PI-Climate,input,8",q_per_rev = 1.0),
            "water":Utility_meter(path = "ean:PI-Climate,water,,43828915,XXXXX,m3,41.7,,,")},
    notifications = {
            "power":Mail(subject='Power & Utility Charges', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='pwr', files2mail=None, ceiling=None),
            "power_cam_shot":Mail(subject='Power & Utility CAM Shot', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None)},
    role_me = "PI-Climate",
    sensors = {
            "C_domestic_hot_water":Sensor(i_read = "°C",path = "ow:PI-Climate,287B4A740600005D,DS18B20,,92")})

```

<!--e_insert-->

* * * 
* * * 
# Utility Reporting Example, daily emailed

* * * 
* * * 

<!--s_insert_{"role":"forensics","suffix":"pwr"}-->


[PI-Stats_pwr.html](PI-Stats_pwr.html)
<html><body><p><h1>Power & Utility Charges</h1><table id="selfgen"><thead><tr><th>EAN/Meter</th><th>Utility</th><th align="center">Start</th><th align="center">Close</th><th align="center">Units</th><th>-</th><th align="right">Price</th><th align="right">Total</th></tr></thead><tbody><tr><td  colspan="8",  align="center", bgcolor="cyan">      0.00 &euro;</td></tr></tbody></table></p></body></html>
<!--e_insert-->


* * * 
* * *