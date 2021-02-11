<!--s_name-->
# Sms_driver

<!--e_name-->

## Summary

<!--s_role-->
<!--e_role-->

<!--s_descr-->
GSM SMS driver, both as a notification sender of messages as a receiver of remote commands, via the hologram nova modem, see http://hologram.io

<!--e_descr-->

<!--s_tbl-->
## List of [properties](Properties.md) for __Sms_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | do_sms | Virtual | False | - | the virtual that allows or prohibit sms messages.  This virtual is ignored if override is true in the sms message dictionary | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | notifications | ['sms_log'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 
  | sms_from | data_list | True | - | authorised sources of sms messages, whereby phone is an E.164 formatted string with a '+' sign.  If empty then all sources are allowed | 
  | sms_rcv | str | True | - | the bash command string for receiving a message, if empty then no sms receiving will happen | 
  | sms_snd | str | False | - | the bash command string for sending a message, whereby phone is an E.164 formatted string with a '+' sign whereto the msg sms message will be sent | 
  | sms_tags | data_dict | - | - | tags that work like formatting in strings in python | 

## List of [Notifications](Notifier.md) for  __Sms_driver__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | sms_log | when this report runs | 

## List of [Errors/Warnings](Error_Warn.md) for  __Sms_driver__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_sms_file | !!SMS modem file <{:}> not exists |  
  | err_sms_modem | !!SMS modem not found, usb power restart |  
  | err_sms_rcv | !!SMS from {:} not in {:}, {:} |  
  | err_sms_snd | !!SMS error {:}, <{:}>, stat=<{:}> |  
  | err_sms_to | !!SMS invalid phone <{:}> in <{:}> in sms_driver |  
  | msg_sms_ign | SMS dropped by do_sms, {:} |  
  | msg_sms_notif | SMS nty added :{:} -> {:}/{:} |  
  | msg_sms_rcv | SMS received {:} {:} |  
  | msg_sms_rcv_started | SMS receiver process started |  
  | msg_sms_rcving | SMS receiving... |  
  | msg_sms_sending | SMS sending to {:}, {:} chars... |  
  | msg_sms_snd | SMS sent {:}, <{:}> |  
<!--e_tbl-->

## Definition of sms destinations

SMS notifications are defined as a 2 key dictionary : {"to":"..,..","txt":"..."}

The "to" string is a destination and is a comma separated list of phone numbers. A phone must be an E.164 formatted string with a '+' sign, and the message string.
The "txt" is a payload string, there is a search and replace for certain keywords:

| keyword | meaning |
| --- | --- |
| {site} | will be replaced with the site name
| {id} | will be replaced with the device or person name in case this is an ibutton or btle device | 
| {json} | a json string same as for IFTTT value1, value2, value3 will be generated. see [__ifttt_interface__](ifttt_interface.md) |
| {default} | room/option, io name, value seperated by forward slash |
| {sms_to} | will get the phone destionations of the sms_to list in the sms_interface in site.conf |
| {io_name}| the name of the io device where the notification origins from (optional)
| {value1}, {value2}, {value3} | just like IFTTT : value1 = room/option, value2=io name, value3=value
| {nty_id} | the original item key name in the properties defining the sms identifier 
| {app_txt} | what the program sometimes generate and is used in email notifications (optional)
| {nmw} | 'no matter what' : the sms is sent ignoring the do_sms flag state

Alternatively routes can be defined in hologram nova, whereby the phone becomes optional.  Just make an empty string in that case.

## Example sms_driver and notifications


<#--s_insert_{"tree":"(o:Sms_driver)"}--> (patched out because of device key 2 ampersands)

from project.py tree:(o:Sms_driver)
```python3
# --> project.py :<dk:project,o:Project,kw:drivers,lp:5,o:Sms_driver>

from lucy import *

Sms_driver(
    do_sms = Virtual(value_logic = {"assign":{"00:00":"True","is_holiday":"True","sleep":"False"}}),
    notifications = {
            "sms_log":Mail(subject='SMS Logging - {app_txt} new items', to=None, cams=None, cam_groups=None, passes=0, body_file='sms_log', files2mail=None, ceiling=None)},
    role_me = "PI-Stats",
    sms_from = ["+447937405250"],
    sms_rcv = "sudo hologram receive -t 1 --sms",
    sms_snd = "sudo hologram send --timeout {time_out} --destination {phone} --sms --devicekey XXX '{msg}'",
    sms_tags = {"everyone":"+32479400501,+32471043409","prime":"+32479400501"})

```

<!--e_insert-->

Please observe the generic sms format in \[DEFAULT\] which works in all sms notification circumstances but is cryptic at first sight.

## Receiving SMS

For security reasons it is best to have the allowed origin phone numbers listed in sms_from.
The sms message itself has to be one of the voice commands that are available with Siri, ok Google or Alexa.
Messages have to be separated by comma if they are grouped in a single SMS message.

## SMS Logging

SMS traffic is logged and reported, see below an example emailed once a day at midnight:

<!--s_insert_{"role":"sms","suffix":"sms_log"}-->


[PI-Stats_sms_log.html](PI-Stats_sms_log.html)

<!DOCTYPE html><html><body><h1>SMS Notifications -> PI-Stats_cum.html  2020/11/08 20:28:25</h1><table><thead><tr><th>Date</th><th>Time</th><th>sms_id</th><th>sms_to</th><th>Message</th><th>Delivered?</th></tr></thead><tbody><tr><td>2020-11-08</td><td>20:12:44</td><td>sms_MASTER_BED_fire</td><td>+32479400501</td><td>Help, there is fire in the kings bedroom detected, please evacuate NOW! master_bed.rear/fire_master_bed.rear:Armed-&gt;Alarm</td><td>RESPONSE MESSAGE: Message sent successfully,</td></tr><tr><td>2020-11-08</td><td>20:01:08</td><td>sms_MASTER_BED_fire</td><td>+32479400501</td><td>Help, there is fire in the kings bedroom detected, please evacuate NOW! master_bed.rear/fire_master_bed.rear:Armed-&gt;Alarm</td><td>-</td></tr><tr><td>2020-11-08</td><td>19:55:00</td><td>sms_MASTER_BED_fire</td><td>+32479400501</td><td>Help, there is fire in the kings bedroom detected, please evacuate NOW! master_bed.rear/fire_master_bed.rear:Armed-&gt;Alarm</td><td>-</td></tr><tr><td>2020-11-08</td><td>19:44:45</td><td>sms_MASTER_BED_fire</td><td>+32479400501</td><td>Help, there is fire in the kings bedroom detected, please evacuate NOW! master_bed.rear/fire_master_bed.rear:Armed-&gt;Alarm</td><td>-</td></tr><tr><td>2020-11-08</td><td>19:34:29</td><td>sms_MASTER_BED_fire</td><td>+32479400501</td><td>Help, there is fire in the kings bedroom detected, please evacuate NOW! master_bed.rear/fire_master_bed.rear:Armed-&gt;Alarm</td><td>-</td></tr></tbody></table></body></html>
<!--e_insert-->

 



