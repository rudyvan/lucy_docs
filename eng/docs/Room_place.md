
# Definition of Rooms and Places

site.conf starts with sections [DEFAULT], {VERSION], [APPS] and then follows rooms or places of the site.

These should all be in square braces, and preferably upper case as this is the standard in python's prj_parser.

Typically you would have sections [STREET}, [GARDEN], [HAL] and then all the rooms in the house, but any of these are all your own such as [VERANDA], [TERRACE].
Any order is fine. The idea is that a room or place is defined when some thing or system is in there, such as security, climate, weather, etc...

Rooms or places can be grouped by using a dot in the name to separate from the group, for example, [hall.ground] and [hall.upstairs] are both member of the group HALL.

## Referring to rooms in voice commands

__name_say__ : is a special field with a string of the room/place how to name the room or the room group (use the same name_say for all these rooms) in a voice command

In the config example little further, [hall.ground] and [hall.upstairs] are both member of the group HALL and you could simply __name_say__ them as "Hall" to group them also from a voice command perspective.

## Grouping rooms in zones

In the security app in a room, the zone can be defined to which this room belongs, so in the example below, hall.ground is in the zone 'house' and hall.upstairs is in the zone 'sleep'.

When you define a door or window, you can state to what different zones this door or window connects, it is in the door properties 'access'.

This information is necessary for the security module to see what the safe exit ways are when arming the house, what rooms are not to be secured while sleeping, etc..

You can name the zone's any way you want, but a given room can only belong to one zone.

For more information on zones and security, see [Security](Security.md) and the example below.
 
## Room definition examples

Below the hall is defined as 2 rooms, and they are both referred to as hall.

The toilet is a 2 room combination, a small hall and the toilet room itself.

In the rooms the different things and systems are defined.

The ground level piece of the hall belongs to the zone 'house' and the door gives access between the zones garden and house.
The top level piece of the hall belongs to the zone 'sleep'.   As in this house all the bedrooms are at the top level all the rooms belonging to the zone 'sleep' will not be secured when the security system is armed partially.
In the security system one can define which zones are armed partially or fully and what exit_way or entry_way is available to arm or disarm the house, more details in the [Security system](Security.md) overview.


<!--s_insert_{"tree":["(dk:veranda)","(dk:hall.ground)","(dk:hall.upstairs)","(dk:toilet.ground)","(dk:toilet.hall)"]}-->

from project.py tree:['(dk:veranda)', '(dk:hall.ground)', '(dk:hall.upstairs)', '(dk:toilet.ground)', '(dk:toilet.hall)']
```python3
# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:veranda,o:Room>

from lucy_app import *

Room(
    contents = [
        Things_controllers(items = {
                        "DK_Veranda":Daikin(path = "ip:192.168.15.62"),
                        "PI-Veranda":Raspi(path = "ip:192.168.15.32",ths_hw = ["unipi,12,14"])}),
        Access_ways(items = {
                        "iButton_out_veranda":Access_point(direction = "exit",method_things = {
                                        "access_green":Light(duration = 4,path = "unipi:PI-Veranda,relay,6"),
                                        "access_red":Light(duration = 4,path = "unipi:PI-Veranda,relay,7")},path = "usb:PI-Veranda,serial_arduino,1w_button,0")}),
        Music_players(items = [Sonos(ip = "192.168.15.161",ip_action = 0,sonos_type = "PLAY:1"),Sonos(ip = "192.168.15.160",ip_action = 0,sonos_type = "PLAY:1")]),
        Cameras(items = {
                        "cam_veranda":Camera(
                                cam_tpe = "foscam1",
                                file_id = "VE",
                                ip = "192.168.15.144",
                                member_of = ["cams_garage","cams_alarm","cams_entrance","cams_driveway"],
                                port = 88,
                                user = "rudyv")}),
        Windows(items = {
                        "sun_veranda_side":Win_cover(
                                path = "vera:Vera_plus,sun_veranda_side",
                                value_logic = {
                                        "assign":{"sunrise+03:00":"100","sunset-01:00":"0"},
                                        "disable":['raining_wc', 'wind_speed_wc^wind_gust>60'],
                                        "disable_delay":{"after":1800},
                                        "enable":['C_outdoor_wc>22', 'sun_light_wc>90'],
                                        "enable_delay":{"after":1800,"before":120}}),
                        "sun_veranda_tent":Win_cover(
                                my_assistant = True,
                                notifications = {
                                        "enable_off":Say(txt='{tts_start} the sun tent is closed as the sun and temperature do not need the tent to open{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                        "enable_on":Say(txt='{tts_start} the sun tent is enabled and can open{tts_end}', ceiling=None, times=1, override=None, volume=None)},
                                path = "vera:Vera_plus,sun_veranda_tent",
                                value_logic = {
                                        "assign":{"sunrise+01:00":"50","sunrise+02:00":"100","sunset-02:00":"0","sunset-03:00":"50"},
                                        "disable":['raining_wc', 'sun_light_wc<50', 'wind_speed_wc^wind_gust>60'],
                                        "disable_delay":{"after":1800},
                                        "enable":['C_outdoor_wc>22', 'sun_light_wc>90'],
                                        "enable_delay":{"after":1800,"before":120}})}),
        Security(alarm_detectors = {
                        "movement_veranda":Alarm_detector(active = 0,detector_type = "burglar",path = "unipi:PI-Veranda,input,4"),
                        "tamper_veranda":Alarm_detector(active = 0,detector_type = "tamper",path = "unipi:PI-Veranda,input,5")},fire_detectors = [Fire_detector(path = "unipi:PI-Veranda,input,7")],zone = "house"),
        Doors(items = {
                        "main_entrance":Door(
                                method_things = {
                                        "access":["garden","house"],
                                        "beam2open":Optical(
                                                notifications = {
                                                        "payload_no":Mail(subject='Veranda Beam Alert, {app_txt}', to='{prime}', cams=None, cam_groups=['cams_driveway'], passes=2, body_file='', files2mail=None, ceiling=None)},
                                                path = "unipi:PI-Veranda,input,6",
                                                value_logic = {"freeze":{"is_alarm":False,"is_armed":True}}),
                                        "is_opened":Input(active = 0,path = "unipi:PI-Veranda,input,1"),
                                        "light_night":Light(duration = 120,path = "unipi:PI-Veranda,relay,4",usage = {"watts":150}),
                                        "lights_on_at_open":Virtual(value_logic = {"assign":{"00:00":"1"}}),
                                        "pulse2open":Output(duration = 6,method_things = {
                                                        "activate_button":Button(
                                                                effect_virtuals = {
                                                                        "do_arm_at_close":Virtual(
                                                                                play = Effect(maker='parent', condition='when_inactive', effect='make_toggle', taker='self', delay=None, duration=None)),
                                                                        "dw_cmd_gate":Virtual(
                                                                                duration = 2,
                                                                                play = Effect(maker='parent', condition='become_active', effect='make_active', taker='self', delay=None, duration=None))},
                                                                path = "unipi:PI-Veranda,input,8")},path = "unipi:PI-Veranda,relay,2"),
                                        "time_open_max":120},
                                my_assistant = True,
                                notifications = {
                                        "inactive":Mail(subject='{thing+is}', to=None, cams=None, cam_groups=['cams_entrance'], passes=2, body_file='', files2mail=None, ceiling=None),
                                        "open_max":[
                                            Mail(subject='Main Entrance is open longtime!', to='{prime}', cams=None, cam_groups=['cams_driveway'], passes=1, body_file='', files2mail=None, ceiling=None),
                                            Say(txt='{tts_start} this is a warning that the main entrance is still open{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                            Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)]},
                                path = "unipi:PI-Veranda,input,9")}),
        Lights(my_assistant = True,room_lights = {
                        "veranda_color":Color_light(
                                my_assistant = True,
                                path = "vera:Vera_plus,veranda_color",
                                usage = {"watts":12},
                                value_logic = {
                                        "assign":{
                                                "00:00":C_state(brightness=0, scene='', color=''),
                                                "away":C_state(brightness=5, scene='', color='red'),
                                                "sleep":C_state(brightness=5, scene='', color='red'),
                                                "sunset":C_state(brightness=10, scene='Rainbow', color=''),
                                                "sunset+01:00":C_state(brightness=5, scene='', color='#FFFFFF')}}),
                        "veranda_main_light":Dim_light(
                                copy_things = {
                                        "carbon_copy":Dim_light(path = "shelly:192.168.15.81,2",usage = {"watts":24})},
                                method_things = {
                                        "toggle_button":Button(active = 0,path = "unipi:PI-Veranda,input,10")},
                                path = "unipi:PI-Veranda,ao,1",
                                usage = {"watts":24},
                                value_logic = {"assign":{"00:00":"15","is_armed":"0","sunrise":"0","sunset":"35","sunset-01:00":"25"}})}),
        Climate(
                clim_makers = {
                        "dk_veranda_dry_sp":Clim_SP(i_make = ['dry'],path = "daikin:DK_Veranda,sp"),
                        "dk_veranda_f_dir":Clim_ANY(path = "daikin:DK_Veranda,f_dir",value_logic = {"assign":{"00:00":"3"}}),
                        "dk_veranda_f_rate":Clim_ANY(
                                path = "daikin:DK_Veranda,f_rate",
                                value_logic = {"assign":{"00:00":"B","away":"A","sleep":"A","°C_veranda>30":"5","°C_veranda>35":"7"}}),
                        "dk_veranda_sp":Clim_SP(
                                i_make = ['cold', 'warm'],
                                method_things = {
                                        "is_on":Input(path = "daikin:DK_Veranda,is_on")},
                                path = "daikin:DK_Veranda,sp",
                                usage = {"watts":"from_daikin"})},
                clim_sensors = {
                        "°C_veranda":Sensor(i_read = "°C",path = "ow:PI-Veranda,284572ED0500008F,DS18B20,,104"),
                        "°C_veranda2":Sensor(i_read = "°C",path = "daikin:DK_Veranda,h_temp")},
                clim_targets = {
                        "cold_sp":{"away":27.0,"comfort":-2,"day":{"off":27.0,"on":24.0},"economy":1.5,"sleep":30.0},
                        "dry_sp":{"preset":"humid_preset"},
                        "warm_sp":{"away":10.0,"comfort":2,"day":{"off":12.0,"on":25.0},"economy":-1.5,"sleep":10.0}},
                my_assistant = True,
                notifications = {
                        "{room}.clim_on_0":Say(txt='{tts_start} {room} climatisation is de-activated{tts_end}', ceiling=None, times=1, override=None, volume=None),
                        "{room}.clim_on_1":Say(txt='{tts_start} {room} climatisation is activated, it will get comfortable soon{tts_end}', ceiling=None, times=1, override=None, volume=None),
                        "{room}.comfort_0":Say(txt='{tts_start} {room} is set to regular climatisation{tts_end}', ceiling=None, times=1, override=None, volume=None),
                        "{room}.comfort_1":Say(txt='{tts_start} {room} is set to comfort climatisation{tts_end}', ceiling=None, times=1, override=None, volume=None),
                        "{room}.economy_0":Say(txt='{tts_start} {room} is set to regular climatisation{tts_end}', ceiling=None, times=1, override=None, volume=None),
                        "{room}.economy_1":Say(txt='{tts_start} {room} is set to economy climatisation{tts_end}', ceiling=None, times=1, override=None, volume=None),
                        "{room}_clim_on_0":Mail(subject='Veranda Climatisation is Stopped{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                        "{room}_clim_on_1":Mail(subject='Veranda Climatisation is Activated{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None)},
                room_virtuals = {
                        "{room}^clim_on":Virtual(copy_things = {
                                        "twin_copy":Output(path = "zw:Vera_plus,buttonset,146,Status3")}),
                        "{room}^clim_pref":Virtual_R(
                                copy_things = {
                                        "twin_copy@-1":Output(path = "zw:Vera_plus,buttonset,171,Status5"),
                                        "twin_copy@1":Output(path = "zw:Vera_plus,buttonset,171,Status1")},
                                descr_range = ["Economy","Standard","Comfort"],
                                digital_range = [-1,0,1]),
                        "{room}^humid_soll":Virtual_A(i_read = "%H")})],
    say = "veranda")

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:hall.ground,o:Room>

from lucy_app import *

Room(
    contents = [
        Cameras(items = {
                        "cam_entrance":Camera(
                                cam_tpe = "foscam1",
                                file_id = "GA",
                                ip = "192.168.15.131",
                                member_of = ["cams_entrance"],
                                port = 88,
                                user = "rudyv")}),
        Doors(items = {
                        "old_entrance":Door(
                                notifications = {
                                        "inactive":Mail(subject='{thing+is}', to=None, cams=None, cam_groups=['cams_entrance'], passes=1, body_file='', files2mail=None, ceiling=None)},
                                path = "unipi:PI-Veranda,input,3")}),
        Lights(my_assistant = True,room_lights = {
                        "stairs_ledstrip":Color_light(
                                path = "hue:Hue_Bridge,stairs_ledstrip",
                                value_logic = {
                                        "assign":{
                                                "00:00":C_state(brightness=50, scene='', color='yellow'),
                                                "12:00":C_state(brightness=75, scene='', color='green'),
                                                "away":C_state(brightness=0, scene='', color=''),
                                                "sleep":C_state(brightness=100, scene='', color='red'),
                                                "sunrise":C_state(brightness=35, scene='arctic_aurora', color=''),
                                                "sunset":C_state(brightness=35, scene='', color='yellow')}})}),
        Climate(
                clim_makers = {
                        "r06":Clim_SW(
                                i_make = ['warm'],
                                member_of = ["pump"],
                                method_things = {
                                        "C_fluid":Sensor(i_read = "°C",path = "ow:PI-Climate,2859115F0700002F,DS18B20,,79")},
                                path = "unipi:PI-Climate,relay,11")},
                clim_sensors = [Sensor(i_read = "°C",path = "ow:PI-Light,28BDB65F070000B8,DS18B20,,71")],
                clim_targets = {"warm_sp":{"away":16.0,"comfort":1.0,"day":17.0,"economy":-1.5,"sleep":16.0}}),
        Security(zone = "house")],
    say = "{room_grp}")

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:hall.upstairs,o:Room>

from lucy_app import *

Room(
    contents = [
        Security(fire_detectors = [Fire_detector(path = "unipi:PI-Light,input,3")],sirens = [Alarm_siren(
                            copy_things = {
                                    "carbon_copy":Output(path = "zw:Vera_plus,buttonset,173,Status1")},
                            notifications = {
                                    "app_done":Log(txt='Sirens testing completed', ceiling=None),
                                    "app_start":Say(txt='{tts_start} beware, now follows a monthly sirens test, report urgently if it stays silent {tts_end}', ceiling=None, times=2, override=True, volume=35)},
                            path = "unipi:PI-Light,relay,1",
                            things_app = "sirens_test")],zone = "sleep"),
        Cameras(items = {
                        "cam_upstairs":Camera(
                                cam_tpe = "foscam1",
                                file_id = "US",
                                ip = "192.168.15.153",
                                member_of = ["cams_entrance","cams_alarm"],
                                port = 88,
                                user = "rudyv")}),
        Climate(
                clim_makers = {
                        "r05":Clim_SW(
                                i_make = ['warm'],
                                member_of = ["pump"],
                                method_things = {
                                        "C_fluid":Sensor(i_read = "°C",path = "ow:PI-Light,28C90674060000FC,DS18B20,,97")},
                                path = "unipi:PI-Light,relay,15")},
                clim_sensors = [Sensor(i_read = "°C",path = "ow:PI-Light,28BDB65F070000B8,DS18B20,,71"),Sensor(i_read = "%V",path = "renson:Healthbox_South,hall.upstairs")],
                clim_targets = {"warm_sp":{"away":16.0,"comfort":1.0,"day":18.0,"economy":-1.5,"sleep":16.0}}),
        Lights(my_assistant = True,room_lights = {
                        "hall_light":Dim_light(
                                path = "unipi:PI-Light,ao,1",
                                value_logic = {"assign":{"00:00":"75","away":"0","is_holiday":"0","sleep":"10","sunset":"100"}})}),
        Ip_ping(items = {
                        "{room}_echo":Ping(ip = "192.168.15.118",ip_action = -1,spec_func = "Echo")})],
    say = "{room_grp}")

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:toilet.ground,o:Room>

from lucy_app import *

Room(
    contents = [
        Climate(clim_makers = {
                        "r08":Clim_SW(
                                i_make = ['warm'],
                                member_of = ["pump"],
                                method_things = {
                                        "C_fluid":Sensor(i_read = "°C",path = "ow:PI-Climate,2806895F070000AC,DS18B20,,62")},
                                path = "unipi:PI-Climate,relay,21")},clim_sensors = [Sensor(i_read = "°C",path = "ow:PI-Climate,2806895F070000AC,DS18B20,,62")],clim_targets = {"warm_sp":{"away":13.0,"day":18.0,"sleep":13.0}}),
        Security(zone = "house")],
    say = "{room_grp}")

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:toilet.hall,o:Room>

from lucy_app import *

Room(
    contents = [
        Climate(clim_makers = {
                        "r07":Clim_SW(
                                i_make = ['warm'],
                                member_of = ["pump"],
                                method_things = {
                                        "C_fluid":Sensor(i_read = "°C",path = "ow:PI-Climate,28ED006007000097,DS18B20,,60")},
                                path = "unipi:PI-Climate,relay,24")},clim_sensors = [Sensor(i_read = "°C",path = "ow:PI-Climate,28ED006007000097,DS18B20,,60")],clim_targets = {"warm_sp":{"away":13.0,"day":18.0,"sleep":13.0}}),
        Security(zone = "house")],
    say = "{room_grp}")

```

<!--e_insert-->

## Room Virtuals

Several apps generate room virtuals, these are virtuals that are linked to a room and provide status information, such as a room is occupied or the room temperature is ok.
Other virtuals allow room commands to be issued such as turn on or off all lights.   The documentation of every app which contains room virtuals will publish them and provide information of how to use them.

<!--s_tbl_pl-->
## List of [properties](Properties.md) for __Place__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | contents | list | - | - | what is inside the place | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | room_virtuals | ['role_me', '{room}^is_locked', '{room}^is_occupied'] | True | True | Room Virtuals are prescribed in their structure and store information about room occupancy aspects such as if the room is in use or not.  These settings can be influenced by other virtuals such that you can build user interface panels easily as in the examples | 
  | say | str | True | - | verbose name of the place and is thus used with the assistant | 

## List of [Room Virtuals](place.md) for  __Place__:

  | Virtual | Type Virtual | What it does? |
  | --- | --- | --- | 
  | {room}^is_locked | Virtual | is the room locked, all doors and windows closed? | 
  | {room}^is_occupied | Virtual | is the occupied or abandoned, if abandoned then ^do_lights_off for lights and ^clim_on climatizing to save energy when is_occupied becomes inactive | 
<!--e_tbl_pl-->

For a Room they are obviously the same:

<!--s_tbl_rm-->
## List of [properties](Properties.md) for __Room__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | contents | list | - | - | what is inside the room | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | room_virtuals | ['role_me', '{room}^is_locked', '{room}^is_occupied'] | True | True | Room Virtuals are prescribed in their structure and store information about room occupancy aspects such as if the room is in use or not.  These settings can be influenced by other virtuals such that you can build user interface panels easily as in the examples | 
  | say | str | True | - | verbose name of the place and is thus used with the assistant | 

## List of [Room Virtuals](place.md) for  __Room__:

  | Virtual | Type Virtual | What it does? |
  | --- | --- | --- | 
  | {room}^is_locked | Virtual | is the room locked, all doors and windows closed? | 
  | {room}^is_occupied | Virtual | is the occupied or abandoned, if abandoned then ^do_lights_off for lights and ^clim_on climatizing to save energy when is_occupied becomes inactive | 
<!--e_tbl_rm-->




