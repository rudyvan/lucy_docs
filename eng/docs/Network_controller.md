<!--s_name-->
# Network_controller

<!--e_name-->

## Summary

<!--s_role-->
<!--e_role-->

<!--s_descr-->
Protects the ip network. Scans all devices for ping latency, a summary is emailed at midnight

<!--e_descr-->

<!--s_sub_toc_nc-->

This is the first version of a full local network control concept.

Currently the network controller will read the ip address list from site.conf and ping every device to check it's presence on the network.
Also the absence of internet access is periodically verified.

As a final 'network' related check, the mains power is checked and loss is reported.

Notifications can be issued when a device is lost or returns or when the internet is lost or returns.

In the current setup, every device needs to be clicked firm against the assigned ip address and ensured that this address is registered in the site.conf file, a very manual process not for everyone.

In future versions this should be automatic whereby these ip addresses are generated (dhcp service) and whereby the network is protected against attacks and performance issues.

Then the issue dissapears to manually make fix ip addresses linked into site.conf, so that name resolution to ip address happens without any burden to the user.

Plug in the new device and configure it online!
<!--e_sub_toc_nc-->

<!--s_tbl-->
## List of [properties](Properties.md) for __Network_controller__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | IP_WAN | ip | False | - | wan ip address | 
  | fav | str | True | - | is this a favorite element | 
  | gateway | ip | False | - | lan gateway ip addr | 
  | icon | str | True | - | icon file for this element | 
  | internet_lost | Virtual | False | - | the virtual that will be raised if the internet is lost, there should be a ping device defined with ip_action=1 such as : 'Internet': Ping('8.8.8.8',ip_action=1) | 
  | internet_ping_name | str | False | - | the name of the Ping('8.8.8.8',ip_action=1) object that must be defined somewhere | 
  | internet_ping_repeat | int | False | - | the frequency that the internet_ping object will be inserted in every Ping series | 
  | notifications | ['internet_lost', 'internet_ok', 'network', 'ping_lost', 'ping_ok'] | True | - | possible notifications, see [__Notifier__](Notifier.md) | 
  | ntp_server | ip | False | - | ntp server ip addr | 
  | power_ok | Input | False | - | the input to be connected with the grid, obviously this things_controller should be connected to a battery | 
  | role_me | {tc} | False | - | role_me of 'Network_controller', adds <network> to the roles of the specified tc | 

## List of [Notifications](Notifier.md) for  __Network_controller__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | internet_lost |  | 
  | internet_ok |  | 
  | network |  | 
  | ping_lost |  | 
  | ping_ok |  | 

## List of [Errors/Warnings](Error_Warn.md) for  __Network_controller__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_internet_lost | !!Internet access failure!! |  
  | msg_IP_OK | IP ping success for {:}/{:} -> {:} sec |  
  | msg_internet_there | Internet access restored! |  
  | warn_IP_NOK | !IP ping for {:}/{:} Failed |  
<!--e_tbl-->

## Example network_controller


<!--s_insert_{"tree":"(o:Network_controller)"}-->

from project.py tree:(o:Network_controller)
```python3
# --> project.py :<dk:project,o:Project,kw:apps,lp:0,o:Network_controller>

from lucy_app import *

Network_controller(
    IP_WAN = "127.0.0.1",
    gateway = "192.168.15.1",
    internet_lost = Virtual(
            notifications = {
                    "active":[
                        Say(txt='{tts_start} the internet connection is down{tts_end}', ceiling=None, times=1, override=None, volume=None),
                        Sms(to='{prime}', txt='Home Internet is down!', override=None, ceiling=None)],
                    "inactive":[
                        Say(txt='{tts_start} the internet connection returned{tts_end}', ceiling=None, times=1, override=None, volume=None),
                        Sms(to='{prime}', txt='Home Internet is restored!', override=None, ceiling=None)]}),
    internet_ping_name = "internet_access",
    internet_ping_repeat = 15,
    notifications = {
            "internet_lost":Mail(subject='{app_txt}', to=None, cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
            "internet_ok":Mail(subject='{app_txt}', to=None, cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
            "network":Mail(subject='Network Report - Lost={app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='ip', files2mail=None, ceiling=None),
            "ping_lost":Mail(subject='{app_txt}', to=None, cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
            "ping_ok":Mail(subject='{app_txt}', to=None, cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None)},
    ntp_server = "192.168.15.1",
    power_ok = Input(
            active = 0,
            duration = 2,
            effect_virtuals = {
                    "power_flag":Virtual(
                            duration = 2,
                            play = Effect(maker='parent', condition='become_inactive', effect='make_active', taker='self', delay=None, duration=None))},
            notifications = {
                    "active":[
                        Mail(subject='The House is back with electricity', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                        Say(txt='{tts_start} electrical power in the house is restored{tts_end}', ceiling=None, times=1, override=None, volume=None),
                        Cal(txt='Home Power restored, electricity is back!', summary='', ceiling=None),
                        Sms(to='{prime}', txt='Home Power restored, electricity is back!', override=None, ceiling=None)],
                    "inactive":[
                        Mail(subject='The House is without electricity', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                        Say(txt='{tts_start} the house is without electricity{tts_end}', ceiling=None, times=1, override=None, volume=None),
                        Cal(txt='Home Power lost, electricity is down!', summary='', ceiling=None),
                        Sms(to='{prime}', txt='Home Power lost, electricity is down!', override=None, ceiling=None)]},
            path = "unipi:PI-Stats,input,3"),
    role_me = "PI-Stats")

```

<!--e_insert-->


<!--s_name_pg-->
# Ip_ping

<!--e_name_pg-->

## Summary

<!--s_descr_pg-->
Register network devices with special parameters for non pingable items and 'special' ip addresses. Devices defined with their ip address such as sonos, camera's and things_controllers are automatically added to the ip_ping list

<!--e_descr_pg-->

<!--s_tbl_pg-->
## List of [properties](Properties.md) for __Ip_ping__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | items | *Ping | False | True | Register network devices with special parameters for non pingable items and 'special' ip addresses. Devices defined with their ip address such as sonos, camera's and things_controllers are automatically added to the ip_ping list | 
<!--e_tbl_pg-->

Aside the mandatory ip address, one parameter __ip_action__ is allowed : ip_action=-1 (no ping), 0 (ping), 1 (ping and if lost then internet alarm).

ip_ping objects are automatically created for raspi, sonos objects and camera's as in the examples below.

<!--s_insert_{"tree":["(dk:living_loung).*(o:Ip_ping)","(dk:living_loung).*(o:Cameras)","(dk:office).*(o:Ip_ping)","(dk:office).*(o:Cameras)","(dk:office).*(o:Things_controllers)"]}-->

from project.py tree:['(dk:living_loung).*(o:Ip_ping)', '(dk:living_loung).*(o:Cameras)', '(dk:office).*(o:Ip_ping)', '(dk:office).*(o:Cameras)', '(dk:office).*(o:Things_controllers)']
```python3
# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:living_lounge,o:Room,kw:contents,lp:7,o:Ip_ping>

from lucy_app import *

Ip_ping(items = {
            "TV_Sony":Ping(
                    ip = "192.168.15.154",
                    ip_action = -1,
                    spec_func = "TV",
                    usage = {"watts":10}),
            "{room}_echo":Ping(
                    ip = "192.168.15.117",
                    ip_action = -1,
                    spec_func = "Echo",
                    usage = {"watts":10})})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:living_lounge,o:Room,kw:contents,lp:1,o:Cameras>

from lucy_app import *

Cameras(items = {
            "cam_lounge":Camera(
                    cam_tpe = "foscam1",
                    file_id = "SA",
                    ip = "192.168.15.46",
                    port = 88,
                    user = "admin")})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:office,o:Room,kw:contents,lp:8,o:Ip_ping>

from lucy_app import *

Ip_ping(
    items = {
            "imac_black":Ping(ip = "192.168.15.166",spec_func = "Master",usage = {"watts":150}),
            "internet_access":Ping(ip = "8.8.8.8",ip_action = 1),
            "ip_phone_lucy_621":Ping(ip = "192.168.15.21",usage = {"watts":15}),
            "ip_phone_rudy_624":Ping(ip = "192.168.15.112",usage = {"watts":15}),
            "printer_dell_3110cn_backup":Ping(ip = "192.168.15.186",usage = {"watts":25}),
            "printer_dell_3110cn_main":Ping(ip = "192.168.15.185",usage = {"watts":25}),
            "printer_kyocera_m5526cdn":Ping(ip = "192.168.15.102",usage = {"watts":15}),
            "router2":Ping(ip = "192.168.15.3"),
            "router_fritzbox":Ping(ip = "192.168.15.1",ip_action = 1),
            "{room}_echo":Ping(
                    ip = "192.168.15.105",
                    ip_action = -1,
                    spec_func = "Echo",
                    usage = {"watts":10})})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:office,o:Room,kw:contents,lp:1,o:Cameras>

from lucy_app import *

Cameras(items = {
            "cam_office":Camera(
                    cam_tpe = "foscam1",
                    file_id = "OC",
                    ip = "192.168.15.142",
                    port = 88,
                    user = "rudyv")})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:office,o:Room,kw:contents,lp:0,o:Things_controllers>

from lucy_app import *

Things_controllers(
    items = {
            "DK_Office":Daikin(path = "ip:192.168.15.60"),
            "Hue_Bridge":Hue(path = "ip:192.168.15.136"),
            "Ikea_Tradfri":Ikea(path = "ip:192.168.15.164",secret = "Ua42jpHcvKu3xsKy"),
            "PI-CSlave":Raspi(path = "ip:192.168.15.91"),
            "PI-Dev":Raspi(path = "ip:192.168.15.56"),
            "PI-Notify":Raspi(hw_gws = ["piface:8,8"],path = "ip:192.168.15.106"),
            "PI-Notify2":Raspi(path = "ip:192.168.15.63"),
            "PI-Notify3":Raspi(hw_gws = ["piface:8,8"],path = "ip:192.168.15.133"),
            "PI-Notify4":Raspi(hw_gws = ["piface:8,8"],path = "ip:192.168.15.120"),
            "PI-Stats":Raspi(hw_gws = ["unipi:6,6"],path = "ip:192.168.15.35"),
            "Vera_plus":Vera(path = "ip:192.168.15.75"),
            "imac-lucy":Ubuntu(path = "ip:192.168.15.113"),
            "ow_office":Eds(path = "ip:192.168.15.151")})

```

<!--e_insert-->

* * * 
* * * 
# Reporting IP Overview 

Below an ip ping report is presented, such a report is always available but is daily emailed at midnight.

* * * 
* * * 

<!--s_insert_{"role":"network","suffix":"ip"}-->


[PI-Stats_ip.html](PI-Stats_ip.html)

<!DOCTYPE html><html><body><h1>Network_controller -> PI-Stats_ip.html  2020/11/08 19:44:04</h1><table><thead><tr><th>room</th><th>ip</th><th>name</th><th style='text-align:center'>error count</th><th style='text-align:center'>lastlost hh:mm:ss</th><th style='text-align:center'>lastfound hh:mm:ss</th><th style='text-align:center'>ping fastest sec</th><th style='text-align:center'>ping slowest sec</th></tr></thead><tbody><tr><td style='background-color:cyan;text-align:center' colspan='8'>IP Overview</td></tr><tr><td style='background-color:cyan;text-align:center' colspan='8'>Network Devices Lost : 1/97</td></tr><tr><td>garage_dressing</td><td>192.168.15.84</td><td>ipb_out_mod1</td><td style='text-align:center'>0</td><td style='text-align:center'>None </td><td style='text-align:center'>None </td><td style='text-align:center'>-1.00</td><td style='text-align:center'>-1.00</td></tr><tr><td style='background-color:cyan;text-align:center' colspan='8'>Network Devices OK : 96/97</td></tr><tr><td>attic</td><td>192.168.15.146</td><td>Healthbox_North</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.40</td><td style='text-align:center'>6.23</td></tr><tr><td>attic</td><td>192.168.15.145</td><td>Healthbox_South</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.42</td><td style='text-align:center'>1.20</td></tr><tr><td>attic</td><td>192.168.15.66</td><td>PI-Light</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.41</td><td style='text-align:center'>0.86</td></tr><tr><td>beauty.work</td><td>192.168.15.80</td><td>beauty.work_sonos_1</td><td style='text-align:center'>0</td><td style='text-align:center'>19:10</td><td style='text-align:center'>19:10</td><td style='text-align:center'>1.68</td><td style='text-align:center'>5.93</td></tr><tr><td>beauty.work</td><td>192.168.15.30</td><td>beauty.work_sonos_2</td><td style='text-align:center'>0</td><td style='text-align:center'>19:10</td><td style='text-align:center'>19:10</td><td style='text-align:center'>1.40</td><td style='text-align:center'>5.36</td></tr><tr><td>beauty.work</td><td>192.168.15.97</td><td>DK_Beauty</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>1.67</td><td style='text-align:center'>47.60</td></tr><tr><td>daughter.sleep</td><td>192.168.15.139</td><td>daughter.sleep_echo_ping</td><td style='text-align:center'>no-ping</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td></tr><tr><td>daughter.sleep</td><td>192.168.15.162</td><td>daughter.sleep_sonos</td><td style='text-align:center'>0</td><td style='text-align:center'>19:10</td><td style='text-align:center'>19:10</td><td style='text-align:center'>1.88</td><td style='text-align:center'>9.58</td></tr><tr><td>daughter.sleep</td><td>192.168.15.98</td><td>DK_Daughter</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>2.23</td><td style='text-align:center'>94.40</td></tr><tr><td>daughter.sleep</td><td>192.168.15.26</td><td>ip_phone_rebecca_622_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:10</td><td style='text-align:center'>19:10</td><td style='text-align:center'>0.50</td><td style='text-align:center'>1.26</td></tr><tr><td>garage</td><td>192.168.15.42</td><td>cam_garage_front</td><td style='text-align:center'>0</td><td style='text-align:center'>19:10</td><td style='text-align:center'>19:10</td><td style='text-align:center'>0.33</td><td style='text-align:center'>1.59</td></tr><tr><td>garage</td><td>192.168.15.126</td><td>cam_garage_rear</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.34</td><td style='text-align:center'>1.14</td></tr><tr><td>garage</td><td>192.168.15.167</td><td>garage_sonos</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>1.39</td><td style='text-align:center'>4.15</td></tr><tr><td>garage</td><td>192.168.15.140</td><td>Miele_tumble_dryer_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>2.86</td><td style='text-align:center'>53.30</td></tr><tr><td>garage</td><td>192.168.15.139</td><td>Miele_washing_machine_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>2.53</td><td style='text-align:center'>7.69</td></tr><tr><td>garage</td><td>192.168.15.33</td><td>PI-Security</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.45</td><td style='text-align:center'>0.97</td></tr><tr><td>garage</td><td>192.168.15.64</td><td>PI-Water</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.86</td><td style='text-align:center'>1.34</td></tr><tr><td>garage</td><td>192.168.15.103</td><td>Shelly-EM_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>7.48</td><td style='text-align:center'>78.00</td></tr><tr><td>garage_dressing</td><td>192.168.15.156</td><td>cam_dressing_rear</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.32</td><td style='text-align:center'>1.56</td></tr><tr><td>garage_dressing</td><td>192.168.15.14</td><td>DS1_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.18</td><td style='text-align:center'>3.60</td></tr><tr><td>garage_dressing</td><td>192.168.15.16</td><td>DS2_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.66</td><td style='text-align:center'>1.65</td></tr><tr><td>garage_dressing</td><td>192.168.15.86</td><td>ipb_in_mod1</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.68</td><td style='text-align:center'>1.07</td></tr><tr><td>garage_dressing</td><td>192.168.15.82</td><td>loxone1</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.61</td><td style='text-align:center'>1.37</td></tr><tr><td>garage_dressing</td><td>192.168.15.70</td><td>PI-Climate</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.48</td><td style='text-align:center'>3.45</td></tr><tr><td>garage_dressing</td><td>192.168.15.169</td><td>PI-Energy</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.85</td><td style='text-align:center'>1.43</td></tr><tr><td>garage_dressing</td><td>192.168.15.124</td><td>Sunny_portal_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.87</td><td style='text-align:center'>4.86</td></tr><tr><td>garage_dressing</td><td>192.168.15.74</td><td>vaillant_gw_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.36</td><td style='text-align:center'>1.16</td></tr><tr><td>garden</td><td>192.168.15.93</td><td>cam_driveway_gate</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.28</td><td style='text-align:center'>1.21</td></tr><tr><td>garden</td><td>192.168.15.44</td><td>cam_driveway_house</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.43</td><td style='text-align:center'>11.70</td></tr><tr><td>garden</td><td>192.168.15.51</td><td>cam_garden_house</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.48</td><td style='text-align:center'>2.65</td></tr><tr><td>garden</td><td>192.168.15.45</td><td>cam_house_front</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.51</td><td style='text-align:center'>18.10</td></tr><tr><td>garden</td><td>192.168.15.49</td><td>cam_house_side</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.47</td><td style='text-align:center'>11.60</td></tr><tr><td>garden</td><td>192.168.15.48</td><td>items</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.95</td><td style='text-align:center'>4.30</td></tr><tr><td>garden</td><td>192.168.15.128</td><td>PI-Garden</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.48</td><td style='text-align:center'>1.02</td></tr><tr><td>garden</td><td>192.168.15.29</td><td>PI-Gate</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.51</td><td style='text-align:center'>0.67</td></tr><tr><td>garden</td><td>192.168.15.76</td><td>swimpool_pump_shelly</td><td style='text-align:center'>0</td><td style='text-align:center'>19:14</td><td style='text-align:center'>19:14</td><td style='text-align:center'>2.82</td><td style='text-align:center'>7.84</td></tr><tr><td>guest.sleep</td><td>192.168.15.100</td><td>DK_Guest</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>1.84</td><td style='text-align:center'>44.30</td></tr><tr><td>guest.sleep</td><td>192.168.15.163</td><td>guest.sleep_sonos</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>1.52</td><td style='text-align:center'>57.50</td></tr><tr><td>guest.sleep</td><td>192.168.15.87</td><td>ip_phone_guest_622_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.51</td><td style='text-align:center'>0.93</td></tr><tr><td>hall.ground</td><td>192.168.15.131</td><td>cam_entrance</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.32</td><td style='text-align:center'>1.14</td></tr><tr><td>hall.upstairs</td><td>192.168.15.153</td><td>cam_upstairs</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.52</td><td style='text-align:center'>1.39</td></tr><tr><td>hall.upstairs</td><td>192.168.15.118</td><td>hall.upstairs_echo_ping</td><td style='text-align:center'>no-ping</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td></tr><tr><td>kitchen</td><td>192.168.15.40</td><td>cam_kitchen</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.59</td><td style='text-align:center'>2.81</td></tr><tr><td>kitchen</td><td>192.168.15.157</td><td>kitchen_echo_ping</td><td style='text-align:center'>no-ping</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td></tr><tr><td>kitchen</td><td>192.168.15.111</td><td>kitchen_sonos_1</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>1.47</td><td style='text-align:center'>4.83</td></tr><tr><td>kitchen</td><td>192.168.15.83</td><td>kitchen_sonos_2</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>1.78</td><td style='text-align:center'>7.13</td></tr><tr><td>living_dining</td><td>192.168.15.47</td><td>cam_dining</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.42</td><td style='text-align:center'>11.90</td></tr><tr><td>living_lounge</td><td>192.168.15.46</td><td>cam_lounge</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>0.39</td><td style='text-align:center'>10.90</td></tr><tr><td>living_lounge</td><td>192.168.15.61</td><td>DK_Living</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>2.16</td><td style='text-align:center'>94.70</td></tr><tr><td>living_lounge</td><td>192.168.15.117</td><td>living_lounge_echo_ping</td><td style='text-align:center'>no-ping</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td></tr><tr><td>living_lounge</td><td>192.168.15.114</td><td>living_lounge_sonos_1</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>1.75</td><td style='text-align:center'>14.60</td></tr><tr><td>living_lounge</td><td>192.168.15.115</td><td>living_lounge_sonos_2</td><td style='text-align:center'>0</td><td style='text-align:center'>19:18</td><td style='text-align:center'>19:18</td><td style='text-align:center'>-1.00</td><td style='text-align:center'>9.42</td></tr><tr><td>living_lounge</td><td>192.168.15.99</td><td>living_lounge_sonos_3</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>1.64</td><td style='text-align:center'>6.33</td></tr><tr><td>living_lounge</td><td>192.168.15.90</td><td>living_lounge_sonos_4</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>1.14</td><td style='text-align:center'>1084.00</td></tr><tr><td>living_lounge</td><td>192.168.15.81</td><td>TV_ledstrip_shelly</td><td style='text-align:center'>0</td><td style='text-align:center'>19:14</td><td style='text-align:center'>19:14</td><td style='text-align:center'>3.88</td><td style='text-align:center'>43.00</td></tr><tr><td>living_lounge</td><td>192.168.15.154</td><td>TV_Sony_ping</td><td style='text-align:center'>no-ping</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td></tr><tr><td>master_bath</td><td>192.168.15.168</td><td>master_bath_sonos</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>1.55</td><td style='text-align:center'>4.32</td></tr><tr><td>master_bed</td><td>192.168.15.95</td><td>bed_light_shelly</td><td style='text-align:center'>0</td><td style='text-align:center'>19:14</td><td style='text-align:center'>19:14</td><td style='text-align:center'>5.35</td><td style='text-align:center'>7.19</td></tr><tr><td>master_bed</td><td>192.168.15.79</td><td>closet_RGB_shelly</td><td style='text-align:center'>0</td><td style='text-align:center'>19:14</td><td style='text-align:center'>19:14</td><td style='text-align:center'>5.74</td><td style='text-align:center'>6.90</td></tr><tr><td>master_bed</td><td>192.168.15.92</td><td>DK_Bedroom</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>1.69</td><td style='text-align:center'>4.97</td></tr><tr><td>master_bed</td><td>192.168.15.67</td><td>dressing_wall_light_shelly</td><td style='text-align:center'>0</td><td style='text-align:center'>19:14</td><td style='text-align:center'>19:14</td><td style='text-align:center'>5.46</td><td style='text-align:center'>6.73</td></tr><tr><td>master_bed</td><td>192.168.15.159</td><td>Hue_Bridge2</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.37</td><td style='text-align:center'>0.94</td></tr><tr><td>master_bed</td><td>192.168.15.138</td><td>master_bed_echo_ping</td><td style='text-align:center'>no-ping</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td></tr><tr><td>master_bed</td><td>192.168.15.108</td><td>master_bed_sonos</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>1.52</td><td style='text-align:center'>4.26</td></tr><tr><td>office</td><td>192.168.15.142</td><td>cam_office</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.29</td><td style='text-align:center'>10.90</td></tr><tr><td>office</td><td>192.168.15.60</td><td>DK_Office</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>1.61</td><td style='text-align:center'>38.60</td></tr><tr><td>office</td><td>192.168.15.136</td><td>Hue_Bridge</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.40</td><td style='text-align:center'>2.19</td></tr><tr><td>office</td><td>192.168.15.164</td><td>Ikea_Tradfri</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.17</td><td style='text-align:center'>0.45</td></tr><tr><td>office</td><td>192.168.15.113</td><td>imac-lucy</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.26</td><td style='text-align:center'>1.06</td></tr><tr><td>office</td><td>192.168.15.166</td><td>imac_black_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.37</td><td style='text-align:center'>0.63</td></tr><tr><td>office</td><td>8.8.8.8</td><td>internet_access_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:11</td><td style='text-align:center'>19:11</td><td style='text-align:center'>15.10</td><td style='text-align:center'>28.40</td></tr><tr><td>office</td><td>192.168.15.21</td><td>ip_phone_lucy_621_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.49</td><td style='text-align:center'>1.86</td></tr><tr><td>office</td><td>192.168.15.112</td><td>ip_phone_rudy_624_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.39</td><td style='text-align:center'>0.82</td></tr><tr><td>office</td><td>192.168.15.105</td><td>office_echo_ping</td><td style='text-align:center'>no-ping</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td><td style='text-align:center'>-</td></tr><tr><td>office</td><td>192.168.15.107</td><td>office_sonos_1</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.90</td><td style='text-align:center'>73.10</td></tr><tr><td>office</td><td>192.168.15.101</td><td>office_sonos_2</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>1.12</td><td style='text-align:center'>90.70</td></tr><tr><td>office</td><td>192.168.15.151</td><td>ow_office</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.24</td><td style='text-align:center'>0.40</td></tr><tr><td>office</td><td>192.168.15.56</td><td>PI-CSlave</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.62</td><td style='text-align:center'>2.15</td></tr><tr><td>office</td><td>192.168.15.57</td><td>PI-Data</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.53</td><td style='text-align:center'>0.92</td></tr><tr><td>office</td><td>192.168.15.201</td><td>PI-Notify</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>22.10</td><td style='text-align:center'>124.00</td></tr><tr><td>office</td><td>192.168.15.65</td><td>PI-Notify2</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.53</td><td style='text-align:center'>1.14</td></tr><tr><td>office</td><td>192.168.15.35</td><td>PI-Stats</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.08</td><td style='text-align:center'>0.09</td></tr><tr><td>office</td><td>192.168.15.91</td><td>PI-Trace</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.21</td><td style='text-align:center'>0.26</td></tr><tr><td>office</td><td>192.168.15.2</td><td>printer_dell_mfp3115_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.84</td><td style='text-align:center'>0.98</td></tr><tr><td>office</td><td>192.168.15.102</td><td>printer_kyocera_m5526cdn_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.57</td><td style='text-align:center'>5.48</td></tr><tr><td>office</td><td>192.168.15.3</td><td>router2_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.36</td><td style='text-align:center'>0.92</td></tr><tr><td>office</td><td>192.168.15.1</td><td>router_fritzbox_ping</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.40</td><td style='text-align:center'>0.75</td></tr><tr><td>office</td><td>192.168.15.121</td><td>rudyv-VGN-Z5</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.23</td><td style='text-align:center'>0.76</td></tr><tr><td>office</td><td>192.168.15.75</td><td>Vera_plus</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>0.44</td><td style='text-align:center'>0.54</td></tr><tr><td>street</td><td>192.168.15.52</td><td>cam_gate_left</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.53</td><td style='text-align:center'>1.69</td></tr><tr><td>street</td><td>192.168.15.54</td><td>cam_gate_right</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.37</td><td style='text-align:center'>1.54</td></tr><tr><td>veranda</td><td>192.168.15.144</td><td>cam_veranda</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>0.35</td><td style='text-align:center'>1.53</td></tr><tr><td>veranda</td><td>192.168.15.62</td><td>DK_Veranda</td><td style='text-align:center'>0</td><td style='text-align:center'>19:13</td><td style='text-align:center'>19:13</td><td style='text-align:center'>1.81</td><td style='text-align:center'>53.70</td></tr><tr><td>veranda</td><td>192.168.15.69</td><td>PI-Veranda</td><td style='text-align:center'>0</td><td style='text-align:center'>19:14</td><td style='text-align:center'>19:14</td><td style='text-align:center'>0.61</td><td style='text-align:center'>1.09</td></tr><tr><td>veranda</td><td>192.168.15.161</td><td>veranda_sonos_1</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>1.38</td><td style='text-align:center'>7.46</td></tr><tr><td>veranda</td><td>192.168.15.160</td><td>veranda_sonos_2</td><td style='text-align:center'>0</td><td style='text-align:center'>19:12</td><td style='text-align:center'>19:12</td><td style='text-align:center'>1.35</td><td style='text-align:center'>4.85</td></tr></tbody></table></body></html>
<!--e_insert-->


* * * 
* * * 
