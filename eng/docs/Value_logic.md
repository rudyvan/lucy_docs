<!--s_name_vl-->
# value_logic

<!--e_name-->


<!--s_descr_vl-->
Logic to automatically determine the payload  based on time or other things

<!--e_descr-->

<!--s_role_vl-->
<!--e_role_vl-->

<!--s_sub_toc_vl_d-->

Home automation results in things receiving a payload (typical jargon) based on very complex circumstances and value_logic is a reasonable simple solution to capture this complexity in an understandable manner.

Imagine the payload is determined on time conditions or status of other things (assign), or the current payload is frozen (freeze) until this lock is lifted. 
Additionally one could have conditions to keep the thing into a inactive state (disable) or just have conditions that must be satisfied to allow alteration of the thing (enable).
And when the payload is forced over, as in the example of light dimming where you desire the intensity to be different from the one determined by value_logic, then you lock your preference.
When this temporary payload lock is lifted is also automated.

So value_logic is the process of assigning a value to a thing and 4 logical possibilities exist:
	- assign : assign a payload based on a time occurrence or one of the special influencer things, real or virtuals
	- freeze : conditions in which payload is frozen and cannot not change
	- enable : all conditions to satisfy before an assign payload can apply
	- disable: any of the conditions True will force the payload to inactive (binary type things) or zero (analog or range type things)

So value logic is a dictionary with one or more of these 4 conditions (assign, freeze, enable, disable) with payload influencing properties that is available for output derived things.
The impact of each of these conditions can be delayed a number of seconds before or after they apply.

Value_logic can generate values for more complex circumstances and it that case a value_app is the solution whereby a program script is called in a controlled environment to obtain a value.

<!--e_sub_toc_vl_d-->

But let's first look in the definition. 

## definition

when defining things, an argument __value_logic__ can be added, which has to be a dictionary structure.
* conditions in the dictionary can be:
	* Virtuals : ["sunrise","sunset","is_alarm","sleep","is_armed_partial","away","is_armed_full","is_armed","is_holiday","is_day", "is_room_secure","is_room_climatised","is_comfort","is_economy","is_clim_normal","is_room_all_dws_closed" (all doors/windows of that room closed)]
	Important, above is the order in which these virtuals are tested and this overrides the definition sequence in the value_logic string
	* timestrings : "HH:MM"
	* sunrise and sunset : can be followed with + or - and an unquoted timestring to add or substract time from the sun event
	* "is_" can be replaced with "_is_not_" to mean the inverse, is_not_day	 ==> it is night
	* other conditionals involving names of things such as "wind_speed>50" or "raining" or "sun_light<25" or "home_occupancy=2"  
* for freeze : conditions results in the directory as:
	* True or False (=freeze): put thing on a list whereby updates for making the thing active are ignored.  There is a parameter freeze_delay that specifies the delay to push onto the freezelist
* for assign : conditions results in the directory as:
	* quoted strings (=assign): if the condition (virtual is active) or time is applicable then the string will be converted to the value for the thing and the thing will get this value. Updates will be ignored as assignments get precedence
* for enable : all conditions are evaluated (technically it is a set not a dictionary) and must be true and then assign will be allowed to run else the thing will receive zero value
* for disable : any of the conditions (technically it is a set not a dictionary) being true results in the thing to have a zero value	
* value_logic conditions are checked once a second, so there can be a small (unnoticeable) delay
* enable, disable and freeze can have a set delay: before or after  which delays the logic becoming active (before) or makes it active longer (after) 
* just for dimmers, if the Dimmer value is -1, then only the virtuals are applied, the time series setting is skipped, this is because the value could have been changed by the user and only a virtual best overrides
* just for Hue dimmers : Default available scenes (Hue app defined scenes work also) can be used, and note that here everything is lower case and spaces should be underscores: bright, dimmed, nightlight, energize, relax, read, concentrate, tropical_twilight, spring_blossom, arctic_aurora, savanna_sunset. Attention, the scene will be applied by the hue_bridge to ALL the lights in the room (group), this is a "feature" of the hue_bridge and is out of our control 

## value_logic examples

<!--s_sub_toc_vl-->

1. below is_day is defined as True after sunrise and before sunset else False

	```python3
	"is_day": Virtual(to_do="app", value_logic={"assign":{"00:00":"False","sunrise":"True","sunset":"False"}})
	```
2. in this example curtains open or close 15 minutes after sunrise or after 7:30 what comes last and before sunset or 5pm whatever comes first and not the rest of the day.

	```python3
	"vera_curtains": Virtual(to_do="do_me_follow", 
		value_logic={"freeze":{"sunrise+00:15":True,"00:00":False,"07:30":True,"17:00":False,"sunset":False})
	```
3. this example sets the ventilation speed (0..100) based on the occupancy modes of the house if it is day or night

	```python3
	"ventilation_speed": Dimmer(path="pi:PI-Climate,1",
		value_logic={"assign":{"is_holiday":"10","away":"10","sleep":"50","is_day":"100"})
	```
4. this example sets the hall light off when nobody is there, if sleeping then the value is 10 else 25 before sunset else 100

	```python3
	"hall_light": Dimmer(path="pi:AR-Hall,1", 
		value_logic={"assign":{"sleep":"10","away":"0","is_holiday":"0","00:00":"25","sunset":"100"}})
	```
5. for philips hue things, a hue defined scene name can be used in the value_logic, see below example where the light will be off when the room is protected or before sunrise.	 Then it will be at spring_blossom at 20 (values are 0..100) till noon, then tropical_twilight at 75 and finally from sunset savanna_sunset at 50. 

	```python3
	"office_ledstrip": Dimmer(path="hue:Hue_Bridge,{:}",
		value_logic={
			"assign":{"is_room_secure":"0","00:00":"0","sunrise":"20,spring_blossom","12:00":"75,tropical_twilight","sunset":"50,savanna_sunset"}}, 
		properties={"type":"RGB"})
	```
6. the most complete example is for a window covering (a sun blocker screen). The screen is down over the window from one hour after sunrise till 2 hours before sunset if the sunshine is more than 75% and the temperature outside is above 22 degrees.	But if the windspeed is more than 50 km/hour or it is raining, then the sunscreen is up (zero).  To have latency there is a enable delay of 600 secs so that a sudden cloud do not flip flop the screens.  But rain or wind will up the screens for at least 15 minutes after they disappear. 
	```python3
	"sun_screen": Win_cover(path="vera:{:}", 
		value_logic={		
			"assign":{"sunrise+01:00":"100","sunset-02:00":"0"},
			"enable":{"sun_light_wc>75","°C_outdoor_wc>22"},"enable_delay":{"after":600},
			"disable":{"wind_speed_wc>50","raining_wc"},	"disable_delay":{"after":900}})
	```

<!--e_sub_toc_vl-->




## value_logic aliases

some alias virtuals can be used and they translate internally like (alias: becomes internally):

  | positive alias         | negative alias |
  | --- | --- |
  | "away" -> "is_armed_full" | "not_away" -> "is_not_armed_full" |
  | "sleep" -> "is_armed_partial" | "not_sleep" -> "is_not_armed_partial" |
  | "is_comfort" -> "climate_comfort_mode=1" | |
  | "is_economy" -> "climate_comfort_mode=-1" | | 
  | "is_clim_normal" -> "climate_comfort_mode=0"  | |  

example for ventilation

	```python3
	"room_ventilation": Clim_DM(path="pi:{:},0", 
		value_logic={		
			"assign":{"away":"10","sleep":"25","is_clim_normal":"50"}})
	```

<!--s_name_va-->
# value_app

<!--e_name-->


<!--s_descr_va-->
Logic to automatically determine the payload  based on time or other things

<!--e_descr-->

<!--s_role_va-->
<!--e_role_va-->


<!--s_insert_{"value_app":""}-->


## Available Value_Apps

  | Value_app | Tuple_def | Doc |
  | --- | --- | --- |
  | Makers.heat_storage | ```Heat_storage(C_min=65, C_max=75)``` | ```Determines if the clim storage device such as a hot water tank needs energy<br>(below °C_min is yes, above °C_max is no)<br>"C_min":              65,  minimum storage temperature<br>"C_max":              75,  maximum storage temperature<br>via method_things<br>"C_fluid"            Sensor(path="ow:28E6B45F070000ED",i_read="°C")   storage device water temperature``` |
  | Makers.makers_pertinence | ```Makers_pertinence(check_freq_mins=5, not_used_hours=13, open_duration_mins=4, C_ok_diff=1.5)``` | ```Activates the on/off valves clim_SW regularly to ensure they keep functioning.<br>The script also tests the valve measuring its temperature against the producer.<br>"not_used_hours":      13,  time in hours that when a Clim_SW is not used it will run for a short time to<br>                            keep the mechanics working regularly<br>"check_freq_mins":      5,  timer in minutes that is looked for a Clim_SW not being used a while<br>"open_duration_mins":   4,  time in minutes that the Clim_SW is forced open, should be less than<br>                            pump_duration_min<br>"C_ok_diff":          1.5,  at the end of the run to test for good working of Clim_SW, the minumum<br>                            temperature difference of the Clim_SW sensor before and after activation``` |
  | Production.boiler_on_off | ```Boiler_on_off(max_boiler_nr_rooms=6, C_boiler_highest=65, C_boiler_lowest=35, C_boiler_threshold=4, C_outside_max_boiler=-5, C_outside_min_boiler=15)``` | ```Calculates the boiler range temperature based on the outside temperature and the arguments of this function<br>and determines to switch on or off the boiler.<br>"max_boiler_nr_rooms":       6,  if these number of rooms need heating then the boiler temp is increased<br>                                           to its max setting...<br>"C_boiler_highest":         65, highest boiler temperature, when all of heating is needed<br>"C_boiler_lowest":          35, lowest boiler temperature, when little heating is needed<br>"C_boiler_threshold":       4,  value under/above then boiler is on/off, so range is double this<br>"C_outside_max_boiler":     -5, outside low low temperature, all of warming needed<br>"C_outside_min_boiler":     15, outside high temperature, little warming needed<br><br> via parent method_things :<br>      "C_in": Sensor(path="..",i_read="°C"),  boiler incoming water temp<br>      "C_out": Sensor(path="..",i_read="°C")   boiler outgoing water temp<br><br>returns True/False if the boiler has to be switched on/off``` |
  | Transport.pump_speed_set | ```Pump_speed_set(act_run_idle_hours=13, max_speed_active_makers=60, speed_act_run=50, speed_lowest=50)``` | ```Calculates the optimal pump speed based on the number of clim_SW that are active and the clim_SP ones.<br>"speed_lowest":            50, minimum speed of the pump in percent,<br>"max_speed_active_makers": 60, percent of active clim_makers to reach full pump power<br>"act_run_idle_hours":      13, hours idle to shoot an activation run, !remember set duration<br>"speed_act_run":           50, speed when the pump is activated after not used for a while<br>returns pump_speed as a value between 0 and 100%``` |

<!--e_insert-->
   
Value apps are pieces of program that can be called to deliver a complex circumstantial value to a thing.
The above table lists the available value apps, the args and kwargs and some documentation.
Value apps are circumstantial, they can only be used when they make sense in the logic of the context.

## Example value_app

See extract below and notice the 3 value apps, one to determine the boiler on off moment, one for the pump and one for the radiators periodic open.    

<!--s_insert_{"tree":"(o:Climate_system)"}-->

from project.py tree:(o:Climate_system)
```python3
# --> project.py :<dk:project,o:Project,kw:property,o:House,kw:places,dk:garage_dressing,o:Room,kw:contents,lp:5,o:Climate_system>

from lucy import *

Climate_system(
    air_removal = Virtual(
            copy_things = {
                    "twin_copy":Output(path = "zw:Vera_plus,buttonset,152,Status5")},
            notifications = {
                    "active":[
                        Mail(subject='The heating air removal process is started', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                        Say(txt='{tts_start} the heating air removal process is started{tts_end}', ceiling=None, times=1, override=None, volume=35)],
                    "inactive":[
                        Mail(subject='The heating air removal process is completed', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                        Say(txt='{tts_start} the heating air removal process is stopped, heating works normal again{tts_end}', ceiling=None, times=1, override=None, volume=35)]}),
    clim_SW_periodic_on = Virtual(value_app = Makers_pertinence(check_freq_mins=5, not_used_hours=13, open_duration_mins=4, C_ok_diff=-0.001)),
    production = {
            "gas_heater":Clim_energy_SW(
                    copy_things = {
                            "carbon_copy":Output(path = "unipi:PI-Climate,relay,3")},
                    i_make = ['warm'],
                    method_things = {
                            "C_in":Sensor(i_read = "°C",path = "ow:PI-Climate,28F1EE5E07000094,DS18B20,,77"),
                            "C_out":Sensor(i_read = "°C",path = "ow:PI-Climate,28E6B45F070000ED,DS18B20,,96")},
                    path = "unipi:PI-Climate,relay,2",
                    value_app = Boiler_on_off(max_boiler_nr_rooms=6, C_boiler_highest=70, C_boiler_lowest=40, C_boiler_threshold=4, C_outside_max_boiler=-5, C_outside_min_boiler=15))},
    role_me = "PI-Climate",
    storage = {
            "hot_water_tank":Clim_SW(
                    active = 0,
                    i_make = ['warm'],
                    member_of = ["pump"],
                    method_things = {
                            "C_fluid":Sensor(i_read = "°C",path = "ow:PI-Climate,28A91F600700002D,DS18B20,,84")},
                    path = "unipi:PI-Test,relay,1",
                    value_logic = {"assign":{"hot_water_tank^C_fluid<55":"0","hot_water_tank^C_fluid>65":"1"},"disable":['is_holiday']})},
    transport = {
            "%vent":Motor(path = "unipi:PI-Gate,ao,1",value_logic = {"assign":{"is_armed":"15","is_day":"50","is_holiday":"10","sleep":"25"}}),
            "pump":Motor(
                    duration = 310,
                    member_of = ["gas_heater"],
                    method_things = {
                            "on_off_relay":Output(active = 0,duration = 310,path = "unipi:PI-Climate,relay,1")},
                    path = "unipi:PI-Climate,ao,1",
                    threshold = 1.0,
                    value_app = Pump_speed_set(act_run_idle_hours=13, max_speed_active_makers=60, speed_act_run=50, speed_lowest=50))})

```

<!--e_insert-->

