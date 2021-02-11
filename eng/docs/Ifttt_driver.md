<!--s_name-->
# Ifttt_driver

<!--e_name-->

## Summary

<!--s_role-->
<!--e_role-->

Warning : must be the things_controller assigned to security.
BUT every things_controller can output an outgoing IFTTT notification, the above mentioned role is only for incoming triggers, they are managed by the [__Feeder__](Feeder.md).

For more on IFTTT, see https://ifttt.com/discover

<!--s_descr-->
IFTTT IF THIS THEN THAT driver, both as a trigger with 'maker' and as an google assistant applet processor, These allow ok Google to work, see instructions and the trigger url and reverse web hook url

<!--e_descr-->

<!--s_tbl-->
## List of [properties](Properties.md) for __Ifttt_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | google_assistant | bool | False | - | for the IFTTT applet with google assistant and webhooks | 
  | icon | str | True | - | icon file for this element | 
  | notifications | ['ifttt_log'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 
  | request_port | int | False | - | the port to map from your router to the security role computer which will watch this port for incoming IFTTT messages | 
  | reverse_url | str | False | - | the url needed to reach the security things_controller | 
  | secret_key | str | False | - | private secret | 
  | skip_ifttt_in | Virtual | True | - | the virtual that allows or prohibit incoming IFTTT maker messages | 
  | skip_ifttt_out | Virtual | True | - | the virtual that allows or prohibit outgoing IFTTT triggers | 
  | trigger_url | str | False | - | the url needed to reach the IFTTT maker trigger | 

## List of [Notifications](Notifier.md) for  __Ifttt_driver__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | ifttt_log | when this report runs | 

## List of [Errors/Warnings](Error_Warn.md) for  __Ifttt_driver__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_cert_missing | !!Missing Certificate File : <{:}> |  
  | err_ifttt_g_fail | !!IFTTT <{:}> GET fail |  
  | err_ifttt_p_fail | !!IFTTT <{:}> POST fail |  
  | err_ssi_ky | !!Webserver SSI Secret Key error: <{:}><{:}>,data <{:}> |  
  | err_ssi_secret | !!web_secret missing in things_forensics |  
  | msg_ifttt_ok | IFTTT <{:}> with <{:}> : <{:}> |  
<!--e_tbl-->

## outbound IFTTT messaging

Based on notifications defined in site.conf, the things_controller that changes triggers the notification, is also the one creating and sending the IFTTT trigger to start a remote process.

__Three variables are allowed by the IFTTTT maker process and they are assigned by the driver as follows : value1 = room/option, value2=io_name, value3=io_value__

## inbound IFTTT messaging

With IFTTT it is possible to create an ok Google scene that sends the message to a specific ip address and port.

This is captured by the router and forwarded to the security things_controller on the request port where a flask process is waiting and handling the input.

Following a successful validation check, the message is forwarded to one of the hue emulators (light, climate or command) to be further processed.

Inbound IFTTT processing is also called by the inbound sms_interface processing as these messages are expected to have the same format as the IFTTT messages from the maker.

The ok Google phrase that passes on should be turn \$ / switch \$ / report \$.
Through webhooks a GET json : '''{"when":"{{CreatedAt}}","what":"{{TextField}}"}'''

Make sure that:

* the certificates in "/root/"name of pi".crt","/root/"name of pi".key" are generated and valid

* open request port (5050 in the example below) from the router is mapped to the role_me things_controller after configuring the webhook.

## Example ifttt_driver

In the following example the secret is stored following the creation of a maker's ok google applet in IFTTT.

outbound IFTTT notifications are generated when the car or motor enters, exits or when they are refused entry (if the optional google calendar check fails)

<!--s_insert_{"tree":["(o:Btle_driver)","(o:Ifttt_driver)"]}-->

from project.py tree:['(o:Btle_driver)', '(o:Ifttt_driver)']
```python3
# --> project.py :<dk:project,o:Project,kw:drivers,lp:11,o:Btle_driver>

from lucy import *

Btle_driver(
    btle_blackout = Virtual(duration = 180),
    btle_gw_entry = ["PI-Garden","PI-Gate","PI-Soccer"],
    btle_gw_exit = ["PI-Security"],
    btle_gw_other = ,
    notifications = {
            "b_none":[
                Mail(subject='{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='{tts_start} unidentified something approached the house{tts_end}', ceiling=None, times=1, override=None, volume=None),
                Cal(txt='{app_txt}', summary='', ceiling=None),
                Ifttt(txt='unidentified', ceiling=None)],
            "{id}.b_detected":[
                Mail(subject='{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='{tts_start} Leandro arrived for the soccer training{tts_end}', ceiling=None, times=1, override=None, volume=None),
                Cal(txt='{app_txt}', summary='', ceiling=None),
                Ifttt(txt='beacon_discovered', ceiling=None)],
            "{id}.b_entry":[
                Mail(subject='{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Cal(txt='{app_txt}', summary='', ceiling=None),
                Say(txt='{tts_start} {id} entered the house{tts_end}', ceiling=None, times=1, override=None, volume=None),
                Ifttt(txt='entry', ceiling=None)],
            "{id}.b_exit":[
                Mail(subject='{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='{tts_start} {id} left the house{tts_end}', ceiling=None, times=1, override=None, volume=None),
                Cal(txt='{app_txt}', summary='', ceiling=None),
                Ifttt(txt='exit', ceiling=None)],
            "{id}.b_lost":[
                Mail(subject='{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='{tts_start} Leandro closed the soccer training{tts_end}', ceiling=None, times=1, override=None, volume=None),
                Cal(txt='{app_txt}', summary='', ceiling=None),
                Ifttt(txt='beacon_lost', ceiling=None)],
            "{id}.b_refused":[
                Mail(subject='{app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='', files2mail=None, ceiling=None),
                Say(txt='{tts_start} {id} is refused access to the house{tts_end}', ceiling=None, times=1, override=None, volume=None),
                Cal(txt='{app_txt}', summary='', ceiling=None),
                Ifttt(txt='refused_entry', ceiling=None)]},
    role_me = "PI-Security")

# --> project.py :<dk:project,o:Project,kw:drivers,lp:4,o:Ifttt_driver>

from lucy import *

Ifttt_driver(
    google_assistant = True,
    notifications = {
            "ifttt_log":Mail(subject='IFTTT Logging - {app_txt} new items', to=None, cams=None, cam_groups=None, passes=0, body_file='ifttt_log', files2mail=None, ceiling=None)},
    request_port = 8443,
    reverse_url = "https://{security_ip}:{request_port}/ok_google",
    role_me = "PI-Security",
    secret_key = "jbKyAgze8TYo8kje_yPwc-x-IGMXBV9qHMDeFF3kjFL",
    trigger_url = "https://maker.ifttt.com/trigger/{event_name}/with/key/{secret_key}")

```

<!--e_insert-->


## IFTTT Logging

IFTTT traffic is logged and reported, every things_controller that has IFTTT notifications executed will output this log at the end of every day.

See below for an example of the security things_controller:

<!--s_insert_{"role":"security","suffix":"ifttt_log"}-->


[PI-Security_ifttt_log.html](PI-Security_ifttt_log.html)

<!DOCTYPE html><html><body><h1>IFTTT Triggers -> PI-Security_wlc.html  2020/06/19 00:00:52</h1><table><thead><tr><th>Date</th><th>Time</th><th>event_name</th><th>value1</th><th>value2</th><th>value3</th><th>Delivered?</th></tr></thead><tbody><tr><td>2020-06-18</td><td>14:57:51</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-18</td><td>12:33:04</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-18</td><td>12:28:08</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-18</td><td>10:40:44</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-17</td><td>13:58:46</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-17</td><td>12:59:33</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-16</td><td>15:30:32</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-16</td><td>14:12:59</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-16</td><td>14:09:59</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-16</td><td>14:06:08</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-16</td><td>13:44:59</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-16</td><td>12:14:10</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-16</td><td>10:16:52</td><td>exit</td><td>-</td><td>scooter</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-16</td><td>09:22:19</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-16</td><td>09:12:58</td><td>entry</td><td>-</td><td>Zoulikha</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-16</td><td>09:12:56</td><td>entry</td><td>-</td><td>Zoulikha</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-15</td><td>11:47:43</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-15</td><td>10:33:47</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-13</td><td>15:23:49</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-13</td><td>13:13:41</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-12</td><td>10:18:57</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-12</td><td>09:33:20</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-11</td><td>15:43:30</td><td>entry</td><td>-</td><td>scooter</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-11</td><td>15:43:05</td><td>entry</td><td>-</td><td>Rudy_scooter</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-11</td><td>15:12:42</td><td>exit</td><td>-</td><td>scooter</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-11</td><td>14:35:35</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-11</td><td>13:36:20</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-10</td><td>17:42:16</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-10</td><td>16:30:08</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-10</td><td>15:09:59</td><td>entry</td><td>-</td><td>Rudy</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-10</td><td>11:52:34</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-10</td><td>09:26:14</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-10</td><td>08:45:40</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-10</td><td>08:07:17</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-09</td><td>17:41:42</td><td>entry</td><td>-</td><td>motor</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-09</td><td>16:27:54</td><td>exit</td><td>-</td><td>motor</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-09</td><td>14:50:29</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-09</td><td>14:32:26</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-09</td><td>14:13:46</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-09</td><td>13:11:20</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-09</td><td>13:09:15</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-09</td><td>13:03:13</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-09</td><td>12:33:46</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-09</td><td>09:10:41</td><td>entry</td><td>-</td><td>Zoulikha</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-08</td><td>16:19:32</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-08</td><td>13:17:08</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-07</td><td>12:44:09</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-07</td><td>12:21:34</td><td>exit</td><td>-</td><td>Rudy</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-07</td><td>12:07:33</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-07</td><td>11:29:07</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-06</td><td>13:10:47</td><td>entry</td><td>-</td><td>Rudy_scooter</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-06</td><td>10:59:41</td><td>entry</td><td>-</td><td>Rudy_scooter</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-06</td><td>10:55:04</td><td>entry</td><td>-</td><td>Rudy_scooter</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-06</td><td>10:51:00</td><td>exit</td><td>-</td><td>Rudy_scooter</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-05</td><td>15:31:20</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-05</td><td>15:28:20</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-05</td><td>13:08:26</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-05</td><td>10:14:50</td><td>entry</td><td>-</td><td>scooter</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-05</td><td>09:36:16</td><td>exit</td><td>-</td><td>scooter</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-04</td><td>13:52:08</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-04</td><td>12:43:28</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-03</td><td>11:24:07</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-03</td><td>09:35:49</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-02</td><td>16:45:51</td><td>entry</td><td>-</td><td>scooter</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-02</td><td>15:58:01</td><td>exit</td><td>-</td><td>scooter</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-02</td><td>12:20:25</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-02</td><td>10:57:40</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-02</td><td>10:11:47</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-06-02</td><td>09:39:39</td><td>entry</td><td>-</td><td>Zoulikha</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-06-02</td><td>09:19:56</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-30</td><td>14:26:28</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-30</td><td>14:15:23</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-30</td><td>11:26:08</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-30</td><td>11:23:30</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-30</td><td>10:08:03</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-30</td><td>10:01:59</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-29</td><td>14:08:48</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-29</td><td>13:47:12</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-29</td><td>13:15:59</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-29</td><td>12:07:40</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-29</td><td>10:25:13</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-29</td><td>09:58:31</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-27</td><td>10:52:46</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-27</td><td>09:06:49</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-26</td><td>09:35:38</td><td>entry</td><td>-</td><td>Zoulikha</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-25</td><td>10:10:54</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-25</td><td>09:27:49</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-23</td><td>14:25:08</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-23</td><td>13:20:20</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-23</td><td>13:10:09</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-23</td><td>11:58:45</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-23</td><td>11:55:54</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-23</td><td>11:00:54</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-22</td><td>11:32:55</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-22</td><td>10:52:21</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-20</td><td>11:07:48</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr><tr><td>2020-05-20</td><td>11:05:49</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-20</td><td>11:05:04</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-20</td><td>10:48:12</td><td>entry</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the entry event</td></tr><tr><td>2020-05-20</td><td>10:15:05</td><td>exit</td><td>-</td><td>car</td><td>False</td><td>Congratulations! You&#x27;ve fired the exit event</td></tr></tbody></table></body></html>
<!--e_insert-->
