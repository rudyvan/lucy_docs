<!--s_name-->
# Google_driver

<!--e_name-->

<!--s_role-->
<!--e_role-->

## Summary

<!--s_descr-->
This is the google calendar driver to read the calendar and read person and device credentials (f.i. is entrance allowed?) and to execute events such as holidays, heating up guest rooms, triggering irrigation or lights for special occasions

<!--e_descr-->

A calendar is a great instrument to state the beginning and end of an event and this is available for your domotica system.

Google calendar is selected (maybe others can follow) because the installation on a raspberry pi computer is possible and fairly straightforward.

For more information on how to create persons and devices and access, see [__access__](Access.md) and [__Btle_driver__](Btle_driver.md).

In this driver, the syntax is defined for your google account and calendar items to invoke the trigger of an event or the syntax for a person or device to grant access.

Daily at midnight, a report is mailed with the calendar upcoming events, see example below.

It is possible to insert last minute calendar events, such as giving access to the cleaner when it was forgotten, f.i. when the cleaner is at the door waiting to get access to enter.

However, the program checks only every 5 minutes and 25 events in the future as to avoid Google querying overload.
When the event comes closer, the check interval is reduced to be on or about on the time that the event should commence or finishes. 
  
New events therefore could be picked up with a maximum of 5 minutes delay.

## Google Mail Settings

The google mail settings are hard wired in the installation of every raspberry, in the ssmtp settings for that matter and can only be changed with the right authorisations.

The parameters below are only applicable to the google calendar settings.

Follow carefully the google calendar installation scenario, this is to be performed by a professional unfortunately.

Please do not change these settings.
  
<!--s_tbl-->
## List of [properties](Properties.md) for __Google_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | application_name | str | False | - | the 'given' google calendar application name | 
  | client_secret_file | str | False | - | the file name of the oath secret file | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | notifications | ['cal_log', 'gmail_events'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 
  | scopes | str | False | - | is the path to the google api scope | 

## List of [Notifications](Notifier.md) for  __Google_driver__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | cal_log | generated calendar events, when this report runs | 
  | gmail_events | when this report runs | 

## List of [Errors/Warnings](Error_Warn.md) for  __Google_driver__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_gmail_cred | !!Gmail API credentials failed |  
  | err_gmail_import | !!Gmail API requires API imports |  
  | err_gmail_kw | !!Gmail event keyword {:} for {:} not found in Hue |  
  | err_gmail_note | !!Gmail Notes login error or IMAP not enabled, {:} |  
  | msg_cal_notif | CAL nty added :{:} -> {:}/{:} |  
  | msg_gmail_cred | Gmail: saving creds to {:} |  
  | msg_gmail_kw | Gmail Event : {:} played to {:} <{:}> |  
  | war_gmail_note | !Gmail Session or Socket expired, new login required, {:} {:} |  
<!--e_tbl-->

## Example google_driver

In the below example driver configuration, it is possible to put __\@TEDDYBEAR\@__ in a Google calendar event to allow this person access (gcal_must=True for that person), same for __\@CAR\@__.

All voice control events can be specified in the calendar, such as __\@ALEXA\@=__Holiday (set holiday to start and finish) or  __\@ALEXA\@=__IrrNow (start irrigation at the time of the event).

For the list of all voice commands and therefore all calendar invokable events, see [__My_assistant__](My_assistant.md).  This list is generated automatically and emailed by the deploy raspberry at start.   

<!--s_insert_{"tree":"(o:Google_driver)"}-->

from project.py tree:(o:Google_driver)
```python3
# --> project.py :<dk:project,o:Project,kw:drivers,lp:10,o:Google_driver>

from lucy_app import *

Google_driver(
    application_name = "HomeEvents",
    client_secret_file = "client_secret.json",
    notifications = {
            "cal_log":Mail(subject='Google Calendar Notifier Generated Events - {app_txt} new items', to=None, cams=None, cam_groups=None, passes=0, body_file='cal_log', files2mail=None, ceiling=None),
            "gmail_events":Mail(subject='Google Calendar Events Report', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='gm', files2mail=['gme.log'], ceiling=None)},
    scopes = "https://www.googleapis.com/auth/calendar")

```

<!--e_insert-->


* * * 
* * * 
## Example Google Calendar report, daily emailed at midnight

* * * 
* * * 

<!--s_insert_{"role":"security","suffix":"gm"}-->


[PI-Security_gm.html](PI-Security_gm.html)

<!DOCTYPE html><html><body><h1>Google Calendar Events Report -> PI-Security_gm.html  2020/04/07 00:00:41</h1><h2>Calendar Upcoming Events</h2><table><thead><tr><th>Date</th><th>Weekday</th><th>Time</th><th>TimeZone</th><th>Summary</th><th>Keyword</th></tr></thead><tbody><tr><td>2020-04-06</td><td>Monday</td><td>00:00:00</td><td>CEST</td><td>Paasvakantie</td><td>-</td></tr><tr><td>2020-04-07</td><td>Tuesday</td><td>08:30:00</td><td>UTC+02:00</td><td style='background-color:plum'>@Zoulikha@ Cleaning</td><td>-</td></tr><tr><td>2020-04-07</td><td>Tuesday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-08</td><td>Wednesday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-09</td><td>Thursday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-10</td><td>Friday</td><td>00:00:00</td><td>CEST</td><td>Good Friday</td><td>-</td></tr><tr><td>2020-04-10</td><td>Friday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-11</td><td>Saturday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-12</td><td>Sunday</td><td>00:00:00</td><td>CEST</td><td>LEBRUN STAGE MADRID</td><td>-</td></tr><tr><td>2020-04-12</td><td>Sunday</td><td>00:00:00</td><td>CEST</td><td>Bruna 12/4/1989 aniversary</td><td>-</td></tr><tr><td>2020-04-12</td><td>Sunday</td><td>00:00:00</td><td>CEST</td><td>Easter Day</td><td>-</td></tr><tr><td>2020-04-12</td><td>Sunday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-13</td><td>Monday</td><td>00:00:00</td><td>CEST</td><td>Easter Monday</td><td>-</td></tr><tr><td>2020-04-13</td><td>Monday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-14</td><td>Tuesday</td><td>00:00:00</td><td>CEST</td><td>Rudy vaccinatie regelen - zie voorschrift</td><td>-</td></tr><tr><td>2020-04-14</td><td>Tuesday</td><td>08:30:00</td><td>UTC+02:00</td><td style='background-color:plum'>@Zoulikha@ Cleaning</td><td>-</td></tr><tr><td>2020-04-14</td><td>Tuesday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-15</td><td>Wednesday</td><td>00:00:00</td><td>CEST</td><td>Hubert Vandenberghe</td><td>-</td></tr><tr><td>2020-04-15</td><td>Wednesday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-16</td><td>Thursday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-17</td><td>Friday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-18</td><td>Saturday</td><td>11:00:00</td><td>UTC+02:00</td><td>Weekend Stefan/Joyce bij Lucy/Rudy</td><td>-</td></tr><tr><td>2020-04-18</td><td>Saturday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-19</td><td>Sunday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr><tr><td>2020-04-20</td><td>Monday</td><td>19:00:00</td><td>UTC+02:00</td><td>@ALEXA@=Irr</td><td style='background-color:plum'>Irr</td></tr></tbody></table></body></html>
<!--e_insert-->

* * * 
* * * 
* * * 
* * * 
## Example Google Calendar Notification report, daily emailed at midnight

* * * 
* * * 

<!--s_insert_{"role":"security","suffix":"cal_log"}-->


[PI-Security_cal_log.html](PI-Security_cal_log.html)

<!DOCTYPE html><html><body><h1>Calendar Notifications -> PI-Security_wlc.html  2020/06/19 00:00:52</h1><table><thead><tr><th>Date</th><th>Time</th><th>cal_id</th><th>Summary</th><th>Message</th><th>Delivered?</th></tr></thead><tbody><tr><td>2020-06-18</td><td>19:00:04</td><td>irr_ignored</td><td>Irrigation ignored!  Too Wet, Decay=110 min - CMD_hue</td><td>irr_ignored</td><td>True</td></tr><tr><td>2020-06-18</td><td>14:57:50</td><td>{id}.b_entry</td><td>car entry by beacon car/entry_via_garage</td><td>{id}.b_entry</td><td>True</td></tr><tr><td>2020-06-18</td><td>12:33:03</td><td>{id}.b_exit</td><td>car exit by beacon car/exit_no_lockup</td><td>{id}.b_exit</td><td>True</td></tr><tr><td>2020-06-18</td><td>12:28:07</td><td>{id}.b_entry</td><td>car entry by beacon car/entry_via_garage</td><td>{id}.b_entry</td><td>True</td></tr><tr><td>2020-06-18</td><td>10:40:44</td><td>{id}.b_exit</td><td>car exit by beacon car/exit_no_lockup</td><td>{id}.b_exit</td><td>True</td></tr><tr><td>2020-06-18</td><td>05:54:34</td><td>active</td><td>Post delivered in the mailbox</td><td>active</td><td>True</td></tr><tr><td>2020-06-17</td><td>19:00:03</td><td>irr_ignored</td><td>Irrigation ignored!  Too Wet, Decay=51 min - CMD_hue</td><td>irr_ignored</td><td>True</td></tr><tr><td>2020-06-17</td><td>15:44:32</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-17</td><td>15:44:30</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-17</td><td>15:17:40</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-17</td><td>14:25:04</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-17</td><td>13:58:45</td><td>{id}.b_entry</td><td>car entry by beacon car/entry_via_garage</td><td>{id}.b_entry</td><td>True</td></tr><tr><td>2020-06-17</td><td>12:59:32</td><td>{id}.b_exit</td><td>car exit by beacon car/exit_no_lockup</td><td>{id}.b_exit</td><td>True</td></tr><tr><td>2020-06-17</td><td>07:48:15</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-17</td><td>05:26:01</td><td>active</td><td>Post delivered in the mailbox</td><td>active</td><td>True</td></tr><tr><td>2020-06-16</td><td>19:00:03</td><td>irr_ignored</td><td>Irrigation ignored!  Too Wet, Decay=37 min - CMD_hue</td><td>irr_ignored</td><td>True</td></tr><tr><td>2020-06-16</td><td>15:30:32</td><td>{id}.b_entry</td><td>car entry by beacon car/entry_via_garage</td><td>{id}.b_entry</td><td>True</td></tr><tr><td>2020-06-16</td><td>14:32:42</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-16</td><td>14:12:58</td><td>{id}.b_exit</td><td>car exit by beacon car/exit_no_lockup</td><td>{id}.b_exit</td><td>True</td></tr><tr><td>2020-06-16</td><td>14:09:58</td><td>{id}.b_entry</td><td>car entry by beacon car/entry_via_garage</td><td>{id}.b_entry</td><td>True</td></tr><tr><td>2020-06-16</td><td>14:06:08</td><td>{id}.b_entry</td><td>car entry by beacon car/entry_via_garage</td><td>{id}.b_entry</td><td>True</td></tr><tr><td>2020-06-16</td><td>13:57:36</td><td>active</td><td>Post delivered in the mailbox</td><td>active</td><td>True</td></tr><tr><td>2020-06-16</td><td>13:44:58</td><td>{id}.b_exit</td><td>car exit by beacon car/exit_no_lockup</td><td>{id}.b_exit</td><td>True</td></tr><tr><td>2020-06-16</td><td>12:14:10</td><td>{id}.b_entry</td><td>car entry by beacon car/entry_via_garage</td><td>{id}.b_entry</td><td>True</td></tr><tr><td>2020-06-16</td><td>10:16:51</td><td>{id}.b_exit</td><td>scooter exit by beacon scooter/exit_no_lockup</td><td>{id}.b_exit</td><td>True</td></tr><tr><td>2020-06-16</td><td>09:22:19</td><td>{id}.b_exit</td><td>car exit by beacon car/exit_no_lockup</td><td>{id}.b_exit</td><td>True</td></tr><tr><td>2020-06-16</td><td>09:12:58</td><td>{id}.a_entry</td><td>Zoulikha/cleaner entry by 006D00001939D336/entry_house</td><td>{id}.a_entry</td><td>True</td></tr><tr><td>2020-06-16</td><td>09:12:55</td><td>{id}.a_entry</td><td>Zoulikha/cleaner entry by 006D00001939D336/entry_house</td><td>{id}.a_entry</td><td>True</td></tr><tr><td>2020-06-16</td><td>07:50:47</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-16</td><td>05:28:13</td><td>active</td><td>Post delivered in the mailbox</td><td>active</td><td>True</td></tr><tr><td>2020-06-15</td><td>19:00:04</td><td>irr_ignored</td><td>Irrigation ignored!  Too Wet, Decay=86 min - CMD_hue</td><td>irr_ignored</td><td>True</td></tr><tr><td>2020-06-15</td><td>14:06:08</td><td>active</td><td>Post delivered in the mailbox</td><td>active</td><td>True</td></tr><tr><td>2020-06-15</td><td>11:47:42</td><td>{id}.b_entry</td><td>car entry by beacon car/entry_via_garage</td><td>{id}.b_entry</td><td>True</td></tr><tr><td>2020-06-15</td><td>10:33:47</td><td>{id}.b_exit</td><td>car exit by beacon car/exit_no_lockup</td><td>{id}.b_exit</td><td>True</td></tr><tr><td>2020-06-15</td><td>08:48:32</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-14</td><td>19:00:06</td><td>irr_ignored</td><td>Irrigation ignored!  Too Wet, Decay=10 min - CMD_hue</td><td>irr_ignored</td><td>True</td></tr><tr><td>2020-06-13</td><td>20:18:56</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-13</td><td>19:38:54</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-13</td><td>19:00:03</td><td>irr_ignored</td><td>Irrigation ignored!  Too Wet, Decay=46 min - CMD_hue</td><td>irr_ignored</td><td>True</td></tr><tr><td>2020-06-13</td><td>15:23:49</td><td>{id}.b_entry</td><td>car entry by beacon car/entry_via_garage</td><td>{id}.b_entry</td><td>True</td></tr><tr><td>2020-06-13</td><td>13:38:04</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-13</td><td>13:13:40</td><td>{id}.b_exit</td><td>car exit by beacon car/exit_no_lockup</td><td>{id}.b_exit</td><td>True</td></tr><tr><td>2020-06-13</td><td>11:51:34</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-13</td><td>07:26:25</td><td>active</td><td>Post delivered in the mailbox</td><td>active</td><td>True</td></tr><tr><td>2020-06-12</td><td>19:00:03</td><td>irr_ignored</td><td>Irrigation ignored!  Too Wet, Decay=34 min - CMD_hue</td><td>irr_ignored</td><td>True</td></tr><tr><td>2020-06-12</td><td>17:14:06</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-12</td><td>14:32:02</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-12</td><td>13:23:13</td><td>active</td><td>Post delivered in the mailbox</td><td>active</td><td>True</td></tr><tr><td>2020-06-12</td><td>13:22:51</td><td>active</td><td>Post delivered in the mailbox</td><td>active</td><td>True</td></tr><tr><td>2020-06-12</td><td>13:22:49</td><td>active</td><td>Post delivered in the mailbox</td><td>active</td><td>True</td></tr><tr><td>2020-06-12</td><td>13:06:50</td><td>ring</td><td>RING at the door</td><td>ring</td><td>True</td></tr><tr><td>2020-06-12</td><td>12:02:20</td><td>active</td><td>Post delivered in the mailbox</td><td>active</td><td>True</td></tr></tbody></table></body></html>
<!--e_insert-->

* * * 
* * * 


