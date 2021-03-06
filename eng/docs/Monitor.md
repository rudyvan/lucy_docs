<!--s_name-->
# Monitor

<!--e_name-->

<!--s_role-->
<!--e_role-->

## Summary

<!--s_descr-->
Device monitoring such as waste water levels, wine cellar temperatures and any other things data to watch and to notify if set boundaries are crossed

<!--e_descr-->

Monitoring of sensors is a built in, always ready [__things_app__](things_apps.md) .

<!--s_tbl-->
## List of [properties](Properties.md) for __Monitor__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | items | ['Input', 'Sensor', 'Sensor_switch'] | False | - | Device monitoring such as waste water levels, wine cellar temperatures and any other things data to watch and to notify if set boundaries are crossed | 
<!--e_tbl-->

## Monitoring Examples

In the first example, the waste water levels are monitored and when they are high for 15 seconds (duration), then a voice and sms message are issued.

In the 2nd example, the temperature of the climatisation electronics is monitored as well as the output 24V generator for the heating valves.
If something happens, proper notifications are issued.


<!--s_insert_{"tree":["(dk:garden).*(o:Monitor)","(dk:boiler_room).*(o:Monitor)"]}-->

from project.py tree:['(dk:garden).*(o:Monitor)', '(dk:boiler_room).*(o:Monitor)']
```python3
# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:garden,o:Place,kw:contents,lp:5,o:Monitor>

from lucy_app import *

Monitor(items = {
            "rear_door_movement":Input(
                    notifications = {
                            "active":[
                                Mail(subject='Movement at the rear door', to=None, cams=['cam_alpha_rear_door'], cam_groups=None, passes=2, body_file='', files2mail=None, ceiling=None)]},
                    path = "unipi:PI-RearDoor,input,4"),
            "°C_garden_toilet":Sensor(
                    i_read = "°C",
                    notifications = {
                            "nothing_is":[
                                Mail(subject='Happy! temp {thing} is below {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the temperature of the electronics in the garden toilet is normal again{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)],
                            "when_is>40.0":[
                                Mail(subject='Warning! temp {thing} is above {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the electronics in the garden toilet gets too hot inside{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)]},
                    path = "unipi:PI-Garden,ow,284BF15E0700004F,DS18B20,,100"),
            "°C_pool_case":Sensor(
                    i_read = "°C",
                    notifications = {
                            "nothing_is":[
                                Mail(subject='Happy! temp {thing} is below {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the temperature of the electronics in the soccer door case is normal again{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)],
                            "when_is>40.0":[
                                Mail(subject='Warning! temp {thing} is above {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the electronics in the soccer door case gets too hot inside{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)]},
                    path = "unipi:PI-Pool,ow,2811CE790B000008,DS18B20,,107"),
            "°C_soccer_case":Sensor(
                    i_read = "°C",
                    notifications = {
                            "nothing_is":[
                                Mail(subject='Happy! temp {thing} is below {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the temperature of the electronics in the soccer door case is normal again{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)],
                            "when_is>40.0":[
                                Mail(subject='Warning! temp {thing} is above {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the electronics in the soccer door case gets too hot inside{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)]},
                    path = "unipi:PI-Soccer,ow,28D4747A0B000006,DS18B20,,106")})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:boiler_room,o:Room,kw:contents,lp:2,o:Monitor>

from lucy_app import *

Monitor(
    items = {
            "pwr_clim_relay_top":Input(
                    active = 0,
                    duration = 10,
                    notifications = {
                            "active":[
                                Mail(subject='Warning! {thing} is gone {thing_state}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the 24 volt relays power for the climate system in the garage is suddenly gone{tts_end}', ceiling=None, times=2, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)],
                            "inactive":[
                                Mail(subject='Happy! temp {thing} is normal {thing_state}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the 24 volt relays power for the climate system in the garage is again normal{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)]},
                    path = "unipi:PI-Climate,input,1"),
            "pwr_clim_relay_under":Input(
                    active = 0,
                    duration = 10,
                    notifications = {
                            "active":[
                                Mail(subject='Warning! {thing} is gone {thing_state}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the 24 volt relays power for the climate system in the garage is suddenly gone{tts_end}', ceiling=None, times=2, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)],
                            "inactive":[
                                Mail(subject='Happy! temp {thing} is normal {thing_state}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the 24 volt relays power for the climate system in the garage is again normal{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)]},
                    path = "unipi:PI-Climate,input,2"),
            "°C_case_clim_top":Sensor(
                    i_read = "°C",
                    notifications = {
                            "nothing_is":[
                                Mail(subject='Happy! temp {thing} is below {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the climate box temperature in the garage is normal again{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)],
                            "when_is>40.0":[
                                Mail(subject='Warning! temp {thing} is above {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the climate box in the garage gets too hot inside{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)]},
                    path = "unipi:PI-Climate,ow,28CD3A7406000085,DS18B20,,95"),
            "°C_case_clim_under":Sensor(
                    i_read = "°C",
                    notifications = {
                            "nothing_is":[
                                Mail(subject='Happy! temp {thing} is below {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the climate box temperature in the garage is normal again{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)],
                            "when_is>40.0":[
                                Mail(subject='Warning! temp {thing} is above {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the climate box in the garage gets too hot inside{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)]},
                    path = "unipi:PI-Climate,ow,2818525F070000CA,DS18B20,,76"),
            "°C_case_test":Sensor(
                    i_read = "°C",
                    notifications = {
                            "nothing_is":[
                                Mail(subject='Happy! temp {thing} is below {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the test box temperature in the garage is normal again{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)],
                            "when_is>40.0":[
                                Mail(subject='Warning! temp {thing} is above {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the test box in the garage gets too hot inside{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)]},
                    path = "unipi:PI-Energy,ow,289574D906000075,DS18B20,,44")})

```

<!--e_insert-->
