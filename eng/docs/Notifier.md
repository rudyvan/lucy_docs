# Notifications

## Summary

<!--s_sub_toc_nty-->

Notifications is the process of delivering messages through a Notification Channel when an app or a thing reaches a status causing a trigger.
These triggers are proposed and documented in every app and every type of thing under the banner "Notifications".

All notifications are defined in the Home Configuration File as these are highly user specific.  Various Notification Channels exists such as sending an email, saying something, sending an SMS, ...

For continuation when the internet is unavailable and to have no latency, all say messages are generated text to speech to wav files and stored ready to go on the local notifier controller. 

<!--e_sub_toc_nty-->
 
How do notifications work?

When a trigger point in the programming script specific for the App or the Thing is reached, a notification script runs to assess if a notification is specified for this event and then delivers that notification to that specific notification channel.

As example, in [__Irrigation__](Irrigation.md) there is an attribute __notifications__, that has a list of triggers that will be activated when that particular irrigation event happens.

Email, tcp and udp, zwave, vera and IFTTT notifications channels are easy because every things_controller that generates the notification, can deliver them.
There is no need for centralization of these notifications to one central controller.

However, the situation is different for the outgoing sms and voice (say) notification as they can only be delivered by the specific things_controller assigned to notifications.

Therefore when a things_controller triggers a notification for a channel that most be forwarded, a json message is sent to the notifier which can deliver the message, and that is what happens. 

The notifier things_controller has specific authorizations to receive these commands and deliver them out, so ensure this one is used to define these interfaces.

| notification channel | delivered to | json string |
| --- | --- | --- |
| say | things_controller with role 'voice'   | ```{"type":"cmd","role":"say","cmd":"tts","args":[text,room,times]}```
| sms | things_controller with role 'sms'     | ```{"type":"cmd","role":"sms","cmd":"sms","kwargs":{"to":[dest_list],"txt":"text"}}```


## Notification Channels

<!--s_sub_toc_nty2-->

Every notification is a named tuple.
Currently the following notification channels exist, some of them are work in progress (TBI) and some new channels could be defined in the future (snapchat, rss feeds, etc..):

  | prefix | effect | comment |
  | --- | --- | --- |  
  | mail | email a message to the designated recipients | the subject text is updated with the tag text.  Additional parameters apply such as camera groups to add picture shots to the email as well as body file, added files and subject formatting |
  | log | log message | The text message will logged. | 
  | say | text to speech message as will voiced through the sound system | either in one room, or in all the premises with possibility to repeat a few times and no matter what (even when sleeping) for fire or alarm notifications |
  | sms | gsm sms message | destination is a comma separated list of phone numbers. A phone must be an E.164 formatted string with a '+' sign, and the message string |
  | udp or tcp | ip message | is ip address, ip port and message | 
  | zw | zwave call via vera | is the zwave device name, the device number and the variable value, see the zw pin definition |
  | vera | vera control ltd vera call  | one of the vera scene calls can be activated, see the vera pin definition |
  | ifttt | IFTTT scene call | generates an ifttt maker scene (json) call, whereby the scene id is the nty name, value1 is the room or the option, value2 is the io_name and value3 is the io_state.  __This allows complete integration between IFTTT and Lucy to allow an intensive personalisation of needs__ |  
  | calendar | generate a calendar event with the text specified, duration=0, date & time of the notification | to log event in a calendar when a car left, or the home was armed/unarmed.. |
  | slack | generate a slack group message | TBI |
  | buzzer | generate a buzzer sound for a certain duration and pitch | TBI |
  | display| generate a display notification | |
  | twitter | generate a tweet | TBI |


<!--e_sub_toc_nty2-->

example of a nice list of notification in case of the security manager:

<!--s_insert_{"tree":"(o:Security_manager)"}-->

from project.py tree:(o:Security_manager)
```python3
# --> project.py :<dk:project,o:Project,kw:apps,lp:15,o:Security_manager>

from lucy_app import *

Security_manager(
    notifications = {
            "alarm_intrusion":[
                Mail(subject='Help! Intruders detected, the police is arriving', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='Help! Intruders detected, the police is arriving', ceiling=None, times=3, override=True, volume=60)],
            "alarm_loop":Mail(subject='!! {app_txt}', to='{everyone}', cams=['*'], cam_groups=None, passes=1, body_file='', files2mail=None, ceiling=None),
            "alarm_stopped":[
                Mail(subject='The alarm condition is lifted', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='The alarm condition is lifted', ceiling=None, times=1, override=True, volume=45)],
            "armed_dws_open":Mail(subject='!Security Armed but some doors/windows open: [{app_txt}]', to='{prime}', cams=None, cam_groups=['cams_alarm'], passes=1, body_file='', files2mail=None, ceiling=None),
            "burglar":[
                Mail(subject='Help! Burglars in the house, the police is notified', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='Help! Burglars in the house, the police is notified', ceiling=None, times=3, override=True, volume=60),
                Cal(txt='Burglar Alarm! {app_txt}', summary='', ceiling=None)],
            "burglar_stopped":[
                Mail(subject='The burglar alarm stopped', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='The burglar alarm stopped but the police are still coming', ceiling=None, times=1, override=True, volume=55),
                Cal(txt='Burglar Alarm now OFF!', summary='', ceiling=None),
                Sms(to='{prime}', txt='Home Burglar Alarm now OFF!', override=True, ceiling=None)],
            "fire":[
                Mail(subject='Help! Fire in the house, please evacuate NOW!', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='Help! Fire in the house, please evacuate NOW!', ceiling=None, times=3, override=True, volume=60)],
            "fire_stopped":[
                Mail(subject='The fire alarm is lifted', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='The fire alarm is lifted', ceiling=None, times=1, override=True, volume=45),
                Cal(txt='Fire Alarm now OFF!', summary='', ceiling=None),
                Sms(to='{prime}', txt='Home Fire Alarm now OFF!', override=None, ceiling=None)],
            "panic":[
                Mail(subject='Help! Panic trigger, the police is notified', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='Help! Panic trigger, the police is notified', ceiling=None, times=3, override=True, volume=45)],
            "panic_stopped":[
                Mail(subject='Panic detection stopped, the police is arriving', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='Panic detection stopped, the police is arriving', ceiling=None, times=1, override=True, volume=55)],
            "security_actuals":Mail(subject='Security Actuals Report{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='s_actua', files2mail=None, ceiling=None),
            "security_history":Mail(subject='Security History Report{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='s_hist', files2mail=['si.log'], ceiling=None),
            "security_warn":Mail(subject='!Security Warning DW:  {app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
            "tamper":[
                Mail(subject='Help! Security is tampered, the police is notified. {app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='Help! Security is tampered, the police is notified', ceiling=None, times=3, override=True, volume=45)],
            "tamper_stopped":[
                Mail(subject='Tamper detection stopped momentarily', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='Tamper detection stopped momentarily', ceiling=None, times=1, override=True, volume=55)],
            "{room}.alarm":[
                Mail(subject='Help, alarm detected in the {room}, the police is notified. {app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='Help, alarm detected in the {room}, the police is notified', ceiling=None, times=3, override=True, volume=60),
                Sms(to='{prime}', txt='Home Burglar Alarm in the {room}! {app_txt}', override=True, ceiling=None)],
            "{room}.burglar":[
                Mail(subject='Help, alarm detected in the {room}. {app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Cal(txt='Burglar Alarm in {room} {app_txt}!', summary='', ceiling=None),
                Sms(to='{prime}', txt='Home Burglar Alarm in the {room}! {app_txt}', override=True, ceiling=None)],
            "{room}.dw":[
                Mail(subject='Help, alarm detected in the {room} by a door or window, the police is notified. {app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='Help, alarm detected in the {room} by a door or window, the police is notified', ceiling=None, times=3, override=True, volume=60),
                Cal(txt='Burglar Alarm in the {room} {app_txt}!', summary='', ceiling=None)],
            "{room}.fire":[
                Mail(subject='Help, there is fire in the {room} detected, please evacuate NOW! {app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='Help, there is fire in the {room} detected, please evacuate NOW!', ceiling=None, times=3, override=True, volume=60),
                Cal(txt='Fire Alarm in the {room} {app_txt}!', summary='', ceiling=None),
                Sms(to='{prime}', txt='Home Fire Alarm in the {room}! {app_txt}', override=True, ceiling=None)]})

```

<!--e_insert-->

Some notifications are specific for a room, think about climatisation, security.   Then the above notification type consists of the keyword {room} and a period and prj_parser will automatically generated all the notifications for the rooms of interest to that app.
  
When [Prj_parser](Prj_parser.md) completes the compilation of [myproject.py](myproject.py), then a list of all notifications per type is generated in the report (close at the end). 
  
## Tag Text substitution

In a mail subject message, in an SMS message or in any other notification type, substitution of tags in the message will convert to their content as follows:

  | Tag          | Becomes           | Example |
  | ---          | ---               | --- |
  | {thing}      | name of the thing | 
  | {thing+is}   | name and description of the thing (in what room) and the thing payload | ```{"subject":"{thing+is}"}``` |
  | {thing_state}| current thing payload | |
  | {thing_o}    | thing object (reserved) | |
  | {app}		 | name of the app | |
  | {app_o}      | app object (reserved) | |
  | {id}         | who or what ||
  | {override}   | no matter what; the notification has to be delivered even if the virtual is not active, such as in case of fire | |
  | {default}	 | default text, is specific for the object or the app | |
  | {nty_id}     | the name of the notification | |
  | {ign_xxx}    | with xxx the notification type to ignore.  Is reserved | |
  | __{app_txt}__ | text generated by the app cfr the context of the notification | |
  | {repr}, {rm_o_key}, {nty} | reserved | |
  | {value1}, {value2}, {value3} | also reserved | |
  | {site}		 | name of the site | | 
  | {home_occ}	 | home occupancy text | |
  | {room}	 | room where the thing or room app is defined | |

Especially the app_txt is an important important notification payload contributor.

## Ceiling: Limiting Repeat Notifications

The process to limit notifications is using the key "ceiling" in the notification tuple as follows:

```
ceiling = "x/day" or "x/week" or "x/month" or "x/year" or "x/hour" or "x/minute"
          with x a number from 1 to the maximum of occurences of this notification in that timeframe
```

See the example things "sun_light" and "ws_raining" as examples where the notification is limited to one a day.

## Notification Tuples

The following notification types exist, the fields that can be used and the defaults (filled from right to left, when no default then field is mandatory):


    / Nty Type  / Fields / Defaults /
    / -- / -- / -- /
    / Mail /     subject, to, cams, cam_groups, passes, body_file, files2mail, ceiling / None, None, None, 0, , None, None
    / Say /      txt, ceiling, times, override, volume / None, None, None, None
    / Cal  /     txt, summary, ceiling / "", None
    / Ifttt /    txt, ceiling / None  
    / Log /      txt, ceiling / None  
    / Vera_nty / txt               / 
    / Zw_nty / txt               / 
    / Tcp /      ip, port, txt / 
    / Udp /      ip, port, txt / 
    / Buzzer /   txt               / 
    / Display /  txt               / 
    / Sms /      to, txt, override, ceiling / None, None 


## MAIL Parameters

   | Parameter      | what is     | example |
   | --- | --- | --- |
   | subject        | subject of the email | ```Mail(subject="{thing+is}", to="prime", cam_groups=["cams_street"], passes=2)```
   | to             | email or mail group destination |  ```Mail(subject="!! {app_txt}", to="everyone", cams=["*"],passes=1)```
   | body_file      | the html body file, is generated automatically (by the app) | ```Mail(subject="Security Report{app_txt}", files2mail=["si.log"], body_file="si_rep")```
   | files2mail     | the attachments such as log and forensics, is generated automatically (by the app) | ```Mail(subject="{app_text}", files2mail=["log.log","err.log"])```
   | cam_groups     | a list of name(s) containing camera's | ```Mail(subject="Alarm is Armed", cam_groups=["cams_alarm"], passes=1)```
   | cams           | a list of name(s) of individual camera's | see below |
   | passes         | how many camera picture shots to collect (3 secs in between) | ```Mail(subject="Gate Beam Tripped", cams=["driveway"], passes=2)``` 
   

## SMS Parameters

The define an SMS notification, 2 parameters are needed, the destination(s), the text to send, the override flag (sms to send no matter what) and the ceiling, see example in [Sms_driver](Sms_driver.md]

## SAY Parameters

There are 4 parameters for voice messaging: the text to say, the ceiling, the "times" to repeat, the override (no matter what) and the volume% (full is 100%), 

```
"burglar": Say(txt="Help! Burglars in the house, the police is notified", volume=60, override=True, times=3) 
```  
  
As example; to make a speech notification for the completion of irrigation, the identifier "irr_completed" should be referenced in myproject.py in Irrigation_system.

## Notifications for Range Virtuals

Examples: 

* for range virtuals, the val_x (x the value) is used as a suffix, see below example whereby a text message is played when climatisation switches from heating to cooling :

```
"climate_mode":         
    Virtual_R("role",[-1,0,1], ["Cooling","Off","Heating"]),
        notifications={
            "val_-1":   Say(txt="climatisation with cooling is enabled as outside it is warm"),
            "val_1":    Say(txt="climatisation with heating is enabled as temperature outside dropped")}
```
several other notification keys exist for digital range things: going_up, going_down, low, high, normal


* for binary devices we have active and inactive.  In this example there is a zwave multi switch device that get triggered when the virtual do_say gets active and a tcp and udp message when this virtual becomes inactive. 

```
"do_say": 
    Virtual("app", value_logic={"is_armed":"False","is_holiday":"False","00:00":"False","09:15":"True","22:30":"False"}, 
        notifications={
            "active":    Zw(txt="p_switch,135,1"),
            "inactive":  [ Zw(txt="p_switch,135,1"), Tcp(ip="192.168.15.58", port=5000, txt="text!!"), 
                           Udp(ip="192.168.15.58", port=5001, txt="text!!")]})
```

* for sensors we have high/low and normal.  In this example there is a notification email and a sonos speech message when the temperature is high and back to normal.

<!--s_insert_{"tree":"(dk:attic).*(o:Monitor)"}-->

from project.py tree:(dk:attic).*(o:Monitor)
```python3
# --> project.py :<dk:project,o:Project,kw:property,o:House,kw:places,dk:attic,o:Room,kw:contents,lp:3,o:Monitor>

from lucy_app import *

Monitor(items = {
            "pwr_light_relay":Input(
                    active = 0,
                    duration = 10,
                    notifications = {
                            "active":[
                                Mail(subject='24 volt relays power for the light system in the attic is suddenly gone', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the 24 volt relays power for the light system in the attic is suddenly gone{tts_end}', ceiling=None, times=2, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)],
                            "inactive":[
                                Mail(subject='24 volt relays power for the light system in the attic is normal', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the 24 volt relays power for the light system in the attic is again normal{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)]},
                    path = "unipi:PI-Light,input,8"),
            "°C_case_light_front":Sensor(
                    alt_name = "sensor-88",
                    high = 40.0,
                    i_read = "°C",
                    notifications = {
                            "high":[
                                Mail(subject='Warning! temp {thing} is above {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the light box in the attic gets too hot inside{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)],
                            "normal":[
                                Mail(subject='Happy! temp {thing} is below {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the light box temperature in the attic is normal again{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)]},
                    path = "ow:PI-Light,28FF5F2465040067,DS18B20,,88"),
            "°C_case_light_rear":Sensor(
                    high = 40.0,
                    i_read = "°C",
                    notifications = {
                            "high":[
                                Mail(subject='Warning! temp {thing} is above {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the light box in the attic gets too hot inside{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)],
                            "normal":[
                                Mail(subject='Happy! temp {thing} is below {thing_state}°C', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                                Say(txt='{tts_start} the light box temperature in the attic is normal again{tts_end}', ceiling=None, times=1, override=None, volume=None),
                                Sms(to='{everyone}', txt='{site}-{default}/{nty_id}', override=None, ceiling=None)]},
                    path = "ow:PI-Light,28FF7C1965040004,DS18B20,,87")})

```

<!--e_insert-->

<!--s_name-->
# Notifier

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
Is the App to deliver all outgoing notifications to displays, buzzers, voice output or any other notification channel defined and available through a driver

<!--e_descr-->

  
<!--s_tbl-->
## List of [properties](Properties.md) for __Notifier__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | buzzers | ['Output'] | True | True | list of buzzer(s) that go off when notification is played | 
  | do_buzzers | Virtual | False | - | = virtual, when reset, buzzers stay silent (unless No_Matter_What) | 
  | do_say | Virtual | False | - | = virtual, when reset, sound will not play and the sound request is ignored (unless No_Matter_What) | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | msg_dpls | data_list | True | - | things_controllers that will act as message displays, f.i. to be place next to the television | 
  | notifications | ['say_log', 'timers'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 
  | tts_port | int | False | - | port for the http tts file web services, choose not to interfere with other ports such as the hue emulation port | 
  | tts_request | str | False | - | accepted web requests, this string is a python3 format string and should contain {ip}, {port} and {wav_file} keyword | 
  | tts_tags | data_dict | - | - | tags that work like formatting in strings in python | 
  | tts_volume | int | False | - | on a scale of 100 | 

## List of [Notifications](Notifier.md) for  __Notifier__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | say_log |  | 
  | timers |  | 

## List of [Errors/Warnings](Error_Warn.md) for  __Notifier__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_cam_failure | !!Camera Failure {:} |  
  | err_cam_nok | !!Camera Pict {:} -> {:}/{:} {:} |  
  | err_do_nty | !!Notification Issue {:} {:} {:} |  
  | err_email_fail | !!Email Failure - {:} - {:} |  
  | err_email_file | !!Email File issue {:}{:}, error={:} |  
  | err_file_gmail | !!Email Attachment {:} (needed-{:}MB > avail-{:}MB) -> skipped |  
  | err_nty_obj | !!Notifier {:}, <{:}>??, {:} |  
  | err_show_data | !!show txt split fail 'date time tc_n:' not in {:} {:} |  
  | err_show_mismatch | !!show message, who<>ip mismatch {:} <> {:} in {:} |  
  | err_show_who | !!show message, who is {:}?? {:} |  
  | msg_dpl | msg screen -> {:} from {:} |  
  | msg_nty_ceiling | nty_{:} ignored due ceiling instruction |  
  | msg_nty_ignored | nty_{:} ignored due per APP <{:}> instruction |  
  | msg_papirus | papirus screen -> {:} from {:} |  
  | msg_th_method | METH {:}.{:} |  
  | msg_th_run | APP {:}.{:} |  
  | msg_th_set | SET {:} {:} |  
  | msg_th_upd | UPD {:} |  
<!--e_tbl-->

  
## How does voice messaging (say) work?

see also [Sonos](Sonos.md).

* * * 
* * * 
# Reporting Say Notifications 

Below an overview report is presented of all the SAY (text to speech) messages aired through the sound system, if volume is zero, then the message was ignored, such a report is always available but is daily emailed at midnight.

* * * 
* * * 

<!--s_insert_{"role":"notifier","suffix":"say_log"}-->


[PI-Stats_say_log.html](PI-Stats_say_log.html)

<!DOCTYPE html><html><body><h1>Voice Notifications -> PI-Stats_cum.html  2020/11/08 20:28:25</h1><table><thead><tr><th>Date</th><th>Time</th><th>SAY_id</th><th>Volume</th><th>Repeats</th><th>Room</th><th>Duration</th><th>Message</th></tr></thead><tbody><tr><td>2020-11-08</td><td>19:52:25</td><td>say_sun_light.high</td><td>30</td><td>1</td><td>OFFICE</td><td>6</td><td>&lt;prosody rate=&#x27;medium&#x27;&gt;Hi honey, it is a bright day outside, surely good for your mood&lt;/prosody&gt;</td></tr><tr><td>2020-11-08</td><td>19:51:51</td><td>say_climate.office.clim_on_0</td><td>30</td><td>2</td><td>OFFICE</td><td>5</td><td>&lt;prosody rate=&#x27;medium&#x27;&gt;Hi honey, office climatisation is de-activated&lt;/prosody&gt;</td></tr><tr><td>2020-11-08</td><td>19:50:42</td><td>say_climate_manager.comfort_1</td><td>30</td><td>1</td><td>All Sonos</td><td>5</td><td>&lt;prosody rate=&#x27;medium&#x27;&gt;Hi honey, house is set to comfort climatisation&lt;/prosody&gt;</td></tr><tr><td>2020-11-08</td><td>19:50:24</td><td>say_climate.daughter.sleep.clim_on_0</td><td>30</td><td>2</td><td>DAUGHTER</td><td>6</td><td>&lt;prosody rate=&#x27;medium&#x27;&gt;Hi honey, rebeccas room climatisation is de-activated&lt;/prosody&gt;</td></tr></tbody></table></body></html>
<!--e_insert-->

* * * 
* * * 
* * * 
* * * 
# Reporting SMS Notifications 

Below an overview report is presented of all the SMS messages sent and the destination, such a report is always available but is daily emailed at midnight.

* * * 
* * * 

<!--s_insert_{"role":"notifier","suffix":"sms_log"}-->


[PI-Stats_sms_log.html](PI-Stats_sms_log.html)

<!DOCTYPE html><html><body><h1>SMS Notifications -> PI-Stats_cum.html  2020/11/08 20:28:25</h1><table><thead><tr><th>Date</th><th>Time</th><th>sms_id</th><th>sms_to</th><th>Message</th><th>Delivered?</th></tr></thead><tbody><tr><td>2020-11-08</td><td>20:12:44</td><td>sms_MASTER_BED_fire</td><td>+32479400501</td><td>Help, there is fire in the kings bedroom detected, please evacuate NOW! master_bed.rear/fire_master_bed.rear:Armed-&gt;Alarm</td><td>RESPONSE MESSAGE: Message sent successfully,</td></tr><tr><td>2020-11-08</td><td>20:01:08</td><td>sms_MASTER_BED_fire</td><td>+32479400501</td><td>Help, there is fire in the kings bedroom detected, please evacuate NOW! master_bed.rear/fire_master_bed.rear:Armed-&gt;Alarm</td><td>-</td></tr><tr><td>2020-11-08</td><td>19:55:00</td><td>sms_MASTER_BED_fire</td><td>+32479400501</td><td>Help, there is fire in the kings bedroom detected, please evacuate NOW! master_bed.rear/fire_master_bed.rear:Armed-&gt;Alarm</td><td>-</td></tr><tr><td>2020-11-08</td><td>19:44:45</td><td>sms_MASTER_BED_fire</td><td>+32479400501</td><td>Help, there is fire in the kings bedroom detected, please evacuate NOW! master_bed.rear/fire_master_bed.rear:Armed-&gt;Alarm</td><td>-</td></tr><tr><td>2020-11-08</td><td>19:34:29</td><td>sms_MASTER_BED_fire</td><td>+32479400501</td><td>Help, there is fire in the kings bedroom detected, please evacuate NOW! master_bed.rear/fire_master_bed.rear:Armed-&gt;Alarm</td><td>-</td></tr></tbody></table></body></html>
<!--e_insert-->

* * * 
* * * 
* * *
* * *
# Notifications : list from prj_parser

Detailed notification reporting is generated by every things_controller when the program starts, but it comes emailed from the deploy_controler.
For every room, for every trigger and every channel that the user wants, the notification is pre-generated

See below for an example of the extend of the notification reporting that is available.

see the section ```Notifications``` at the end.

* * *
* * *

<!--s_insert_{"role":"deploy","suffix":"ref"}-->


[imac-lucy_ref.html](imac-lucy_ref.html)
<!DOCTYPE html><html><body><h1>Report_ref -> imac-lucy_ref.html  2021/02/07 11:25:57</h1>

<!--e_insert-->



