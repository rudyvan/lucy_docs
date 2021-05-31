<!--s_name-->
# Things_sync

<!--e_name-->

## Summary

<!--s_descr-->
The process of ensuring that the as_is and to_be state of a Thing is there where it needs to be for the system to work as a whole

<!--e_descr-->

<!--s_role-->
<!--e_role-->

### rest API versus messaging

The situation is that piface devices do not have a rest api that raspberry's over the local lan can consult. Unipi devices do through evok.py
Even then, it would generate a lot of network traffic if every things_controller would consult every other one's rest api as frequently as possible.

Therefore a design assumption is included that raspberry's should know who else needs their input/output status and then inform the other party when a change happen.  
The other party acknowledges the receipt of input status, and also requests the status at startup.

This handshake only generate traffic at startup and when a change happen.   

Of-course with a lot of things_controllers, a lot of io_devices and very distributed functions and io_devices would still generate traffic, but only when a lot of status changes happen, and this is not a real world scenario.

The communications protocol is an UDP message with device status and a reply notification expectation within a reply time frame.
		
### Why a propriety protocol?

The MQTT protocol is used in many iot projects.  The main disadvantage (in my view) is the dependency of a message broker as a single point of failure.
Because every raspberry and every device is defined in site.conf, it is possible to design a star network where every device communicates with the other devices directly, exchanging the payload as required.

Therefore, there is no message broker that has to channel all traffic and there is no need for a subscription process.

During parsing of the config files (app_data, app_obj, site) by [Prj_parser](Prj_parser.md) every things_controller is made aware who needs what payload for every thing changed or in need. 

Also the payload repeats indefinitely until the payload is acknowledged by the receiver and payloads are refreshed if changed during the repeat.

It has proven to work fast and resiliently, there is no dependency on a single things_controller to control the traffic flow.

Should power be interrupted to one or multiple things_controllers, the remaining ones still work with the available data and continue to communicate with each other.   

Should the lost things_controller come back to power then the network restores and synchronizes itself automatically.  

Data exchange is also on a need only basis and is therefore the minimal charge to network bandwidth.

The only requirement is that all things_controllers stay current with the same programs and config file, which is normal expected design practice.

The version that is the result of these design considerations is called things_sync, but please advice that there is NO code or concepts shared from the real MQTT standard!
	
### How does things_sync work?

During [config_parsing](Prj_parser.md) a list of real or virtual things is created for every things_controller that has a role to play with these things.

Additionally it is analyzed how every things_controller will obtain or control the thing, either through a web_service when the thing is a UniPi input or output or through json messages when the thing is virtul or available through a piface driver. 

Another list is then created which things_controller can talk to who for the json messaging to work to ensure that the origin of the message is right.

The things owner things_controller is the one that can update or read the thing's value and the slave things_controller is just the received of the things value of wich it keeps a copy in memory.

The json message structure is as follows:

```{'type':'io','cmd':'','io':'','val':val}```   

* __cmd__ can be : 'set','reply','ask' and for pulses : "pulse" and "reply_pulse"
* __io__ is the name of the thing
* __val__ is the boolean, integer, float or string value of the thing to set.  In case the command is 'ask', val is then the current value of the thing

Pulses are short and by definition the return to normal state is not to be acknowledged again, just the reception of the pulse command.

Example : ```{"type":"io","io":"internet_lost","cmd":"set","val":1}```

json messages can be combined in lists to compress the data in one packed exchange, such as in the following example:

```[{"type":"io","io":"is_armed","cmd":"set","val":1},{"type":"io","io":"is_armed_partial","cmd":"set","val":1}]```

There is a timer system which follows up on the message to ensure that a UDP message gets properly replied from the destination.

If a reply is not received then then sender tries again indefinitely.

All exchanges are logged, by the sender as by the receiver.

### Other Things_sync commands

There is more than just synchronization of things, the possibilities are far more extensive.

Several types of incoming messages are identified and they are differentiated by the "type" of the message, "io","cmd","cum","clim":

* If the message type is "io", then it concerns a command of set/reply or ask for an things value through a handshake
 
 ```example : {"type":"io","io":"is_armed","cmd":"set","val":1}```
  
* If the message type is "cum", then it concerns a cumulative data upload, the request is then for the io thing in "fld"
  The reply should be again "fld" with the things name and the json cumul string with "cum".
  
  ```request: {"type":"cum","fld":"is_alarm"}```
  ```reply: {"type":"cum","fld":"is_alarm","cum":{"..."}}```
  
  Sending an end of day cumul reset is issued by the things_forensic things_controller through the command ```{'type':'cum'}```
	
* If the message type is "cmd", then it concerns a regular command.

  Commands can be anything that is programmed, but are requests typically associated to the given role of the things_controller:
  ```{"type":"cmd","role":"security","cmd":"report"}``` : will email the security report from the security things_controller

* If the message type is "clim", then it concerns a heating/cooling command.
  This command can be simply ```{'type':'clim'}``` and this signals a reload of the climate settings else a json string of new heating settings
  There are a few exceptions to the above rule, when this is the things_controller has the role 'show'

### Available Commands

Below is the list of all available commands and the role that the receiving things_controller should have:

| things_controller role | command | does what? | example json string |
| --- | --- | --- | --- |
| security | report | emails current security report | ```{"type":"cmd","role":"security","cmd":"report"}``` |
| security | echo_report | emails current hue emulation report | ```{"type":"cmd","role":"security","cmd":"echo_report"}``` |
| cmd_do | version | returns the version string | ```{"type":"cmd","role":"cmd_do","cmd":"version","kwargs":{"with_email":true}}``` |
| cmd_do | reboot | reload the application or reboots | ```{"type":"cmd","role":"cmd_do","cmd":"reboot","kwargs":{"reboot_not_exit":true}}``` |
| cmd_do | reload | reloads the application and config files from the deployer | ```{"type":"cmd","role":"cmd_do","cmd":"reload"}``` |
| cmd_do | logging | logs a text | ```{"type":"cmd","role":"cmd_do","cmd":"logging","kwargs":{"reason":"blabla"}}``` |
| cmd_do | timers | emails report of all timers | ```{"type":"cmd","role":"cmd_do","cmd":"timers"}``` |
| cmd_do | new_day | does the new day process | ```{"type":"cmd","role":"cmd_do","cmd":"new_day"}``` |
| cmd_do | reload_all | reloads all the things_controllers with the latest versions | ```{"type":"cmd","role":"cmd_do","cmd":"reload_all"}``` |
| deploy | report | is for the deployer and will trigger all reports from all things_controllers | ```{"type":"cmd","role":"cmd_do","cmd":"deploy_report"}``` |
| deploy | all | is for the deployer and deploys the command to all things_controller | ```{"type":"cmd","role":"cmd_do","cmd":"deploy_all","kwargs":{"do_what":"reboot", "raspis":["PI-Light"]}}``` |
| climate | report | emails the climate report | ```{"type":"cmd","role":"climate","cmd":"report"}``` |
| m_clim | report | emails the climate report | ```{"type":"cmd","role":"m_clim","cmd":"report"}``` |
| network | report | emails the network report | ```{"type":"cmd","role":"network","cmd":"report"}``` |
| weather | report | emails the weather report | ```{"type":"cmd","role":"weather","cmd":"report"}``` |
| irr | report | emails the irrigation report | ```{"type":"cmd","role":"irr","cmd":"report"}``` |
| irr | fix_time | starts the irrigation for a fixed time run | ```{"type":"cmd","role":"irr","cmd":"fix_time", "args":["from things_sync"]}``` |
| irr | adj | starts the irrigation with the adjusted time | ```{"type":"cmd","role":"irr","cmd":"adj", "args":["from things_sync"]}``` |
| irr | abort | stops the irrigation | ```{"type":"cmd","role":"irr","cmd":"abort", "args":["from things_sync"]}``` |
| light | report | emails the light report | ```{"type":"cmd","role":"light","cmd":"report"}``` |
| light | home | switches all the lights in the home on or off | ```{"type":"cmd","role":"light","cmd":"home","args":[0]}``` |
| light | set | switches all the lights in the rooms specified on or off | ```{"type":"cmd","role":"light","cmd":"set","args":["GARAGE_DRESSING",0]}``` |
| light | report | report all what is possible with Hue, Ikea and Vera | ```{"type":"cmd","role":"light","cmd":"report"}``` |
| light | reboot | reboot all what is possible with Hue, Ikea and Vera | ```{"type":"cmd","role":"light","cmd":"reboot"}``` |
| voice | tts_all | plays all voice notifications in the specified room the number of times specified | ```{"type":"cmd","role":"voice","cmd":"tts_all","args":["GARAGE_DRESSING",1]}``` |
| voice | tts | plays the tts id in the specified room the number of times specified | ```{"type":"cmd","args": ["tts_clim_on_0_DAUGHTER","DAUGHTER.SLEEP",2], "cmd": "tts", "role": "voice"}``` |
| forensics | report | emails the forensics_report | ```{"type":"cmd","role":"forensics","cmd":"report"}``` |
| sms | sms | sends an sms to a list of designators | ```{"type":"cmd","role":"sms","cmd":"sms","args":["sms_fire_on",["+441234123423"]]}``` | 
  
  
<!--s_tbl-->
## List of [properties](Properties.md) for __Things_sync__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | TCP_port | int | False | - | port for the http TCP things_sync service | 
  | UDP_port | int | False | - | port for the http UDP things_sync service, used on special authority such as master and vera tc's | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | role_me | {tc} | True | - | role_me of 'Things_sync', adds <system> to the roles of the specified tc | 
  | ws_port | int | False | - | port for the web_socket services | 
  | ws_url | str | False | - | url for the web_socket services, must contain ip and port formatters | 

## List of [Errors/Warnings](Error_Warn.md) for  __Things_sync__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_cmd_args | !!IP command {:}, from {:}, callability issue {:}, args={:}, kwargs={:}, error={:} |  
  | err_drv_msg | !!{:} driver error wrapper expects msg list, not {:} |  
  | err_get_crash | !!{:} http-get crashed, a={:}, kw={:} |  
  | err_get_gone | !!{:} http-get now OK! |  
  | err_ip_in_cmd | !!IP {:} not valid cmd, requester={:} with {:} |  
  | err_ip_in_io | !!IP {:} not thing name, requester={:} with {:} |  
  | err_ip_in_json_req | !!json.loads error, requester={:} with {:} {:} |  
  | err_ip_in_refused | !!IP from {:} with {:} refused |  
  | err_ip_in_req | !!message type error, requester={:} with <{:}> {:} |  
  | err_ip_in_ths_i_use | !!IP {:} not ths_i_use for me, requester={:} with {:} |  
  | err_ip_in_val | !!IP from {:} for {:} with {:} is invalid value |  
  | err_read_crash | !!Read of <{:}> crashed, a={:}, kw={:} |  
  | err_read_gone | !!Read of <{:}> now OK! |  
  | err_scan_crash | !!Scan crashed of <{:}> {:}{:} |  
  | err_scan_gone | !!Scan of <{:}>  now OK! |  
  | err_write_crash | !!Write to <{:}> crashed, a={:}, kw={:} |  
  | err_write_gone | !!Write to <{:}> now OK! |  
  | err_ws_crash | !!Websocket crash: <{:}> {:}{:} |  
  | err_ws_msg | !!Websocket msg: <{:}> {:}{:} |  
  | err_ws_sanic | !!Websocket Sanic crash: <{:}> {:}{:} |  
  | msg_ws_closed | Websocket: {:} is closed {:} |  
  | msg_ws_connect | Websocket: {:} is connected {:} |  
  | msg_ws_reject | Websocket: {:} is rejected {:} |  
  | warn_notify_expired | !Reply? {:} -> {:} |  
  | warn_retry | !{:}, retry {:}, err {:}, kw={:}{:} |  
<!--e_tbl-->

