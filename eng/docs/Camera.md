<!--s_name-->
# Camera

<!--e_name-->

<!--s_role-->
<!--e_role-->

## Defining Camera's

### Summary

<!--s_descr-->
is a network function to check the presence of a thing through a ping

<!--e_descr-->

### Current Limitations

Currently, the code for accessing the camera to obtain a picture or video is hard wired for Foscam camera's and should be linked to the type of camera.
For developers, monitor with Fiddler when changing manually a camera setting and then update the programming in PI_Parse.py where the Camera object is defined.
Three settings exist, one for taking a picture, one for getting a video and lastly for setting the time date of the camera.
Older Foscam camera's use port 80 and more recent camera's have port 88.

### Camera Syntax

<!--s_tbl-->
## List of [properties](Properties.md) for __Camera__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | active | valid_set_int | False | - | designate the active state for a binary thing, either 0 or 1 | 
  | cam_tpe | str | False | - | key in the Camera_driver dict cam_types | 
  | descr | str | False | - | free description field for this thing | 
  | descr_01 | list-2 | False | - | description for a binary thing when payload value is 0 or 1 | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | file_id | str | False | - | 2 characted file id | 
  | icon | str | True | - | icon file for this element | 
  | ip | str | False | - | ip in the format of xx.xx.xx.xx | 
  | ip_action | int | False | - | - | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'inactive', 'none', 'notify+', 'payload_no'] | True | - | the notifications for pings, see [__Notifier__](Notifier.md) | 
  | play | tuple:virtual_tuples | True | - | the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on' | 
  | port | int | False | - | ip port | 
  | pwd | str | False | - | password for the login | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | spec_func | str | False | - | special function attribute | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | user | str | False | - | user name for the login | 

## List of [Notifications](Notifier.md) for  __Camera__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is active | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | inactive | when payload is nonactive | 
  | none | value of the Virtual is None | 
  | notify+ | extra notifications | 
  | payload_no | the requested payload is refused | 

## List of [Errors/Warnings](Error_Warn.md) for  __Camera__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_cam_dt_nok | !!{:} url: {:} DT NOK |  
  | err_cam_url | !!CAM {:} urlopen issue={:}, error={:} |  
  | msg_cam_dt_ok | {:} DT set->OK |  
  | msg_cams_updated | all camera's updated |  
<!--e_tbl-->

<!--s_tbl_s-->
## List of [properties](Properties.md) for __Cameras__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | items | *Camera | False | True | Defining IP camera's and camera groups. Pictures will be taken at specified events through notifications and the camera group memberships | 
<!--e_tbl_s-->



A camera object is defined with:
| Field Name | Description |
| --- | --- |
file_ID | 2 letter short identification which is used as a file name header when taking pictures.  Make sure every camera has a unique file_ID, this is currently not verified during parsing. |
ip | the ipaddress of the camera |
port | port number of the camera, typically 80 or 88 |
user | is the user name for the login.  The password of the camera should be the same as that for the email account, but 
member_of | a list of self invented camera group names (quoted names), that are later used in notifications  
properties | additional properties (dictionary), not really used for camera's
alias_name | a yet to be defined field

## Example defining Camera's

The example below defines 2 camera's at the entrance of the property at the gate.

Camera names are generated with the prefix 'cam_' and the name of the place, in the configuration example below, the names cam_street_left and cam_street_right are generated and made unique.

<!--s_insert_{"tree":"(dk:street).*(o:Cameras)"}-->

from project.py tree:(dk:street).*(o:Cameras)
```python3
# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:street,o:Place,kw:contents,lp:2,o:Cameras>

from lucy_app import *

Cameras(items = {
            "cam_alpha_gate":Camera(
                    cam_tpe = "alpha_go",
                    file_id = "AG",
                    ip = "192.168.15.157",
                    member_of = ["cams_street","cams_gate","cams_alarm","cams_driveway"],
                    port = 80,
                    user = "rudyv"),
            "cam_alpha_soccer":Camera(
                    cam_tpe = "alpha_go",
                    file_id = "AS",
                    ip = "192.168.15.148",
                    member_of = ["cams_street","cams_alarm"],
                    port = 80,
                    user = "rudyv"),
            "cam_gate_left":Camera(
                    cam_tpe = "foscam1",
                    file_id = "GL",
                    ip = "192.168.15.52",
                    member_of = ["cams_street","cams_gate","cams_driveway"],
                    port = 88,
                    user = "rudyv"),
            "cam_gate_right":Camera(
                    cam_tpe = "foscam1",
                    file_id = "GR",
                    ip = "192.168.15.54",
                    member_of = ["cams_street","cams_gate","cams_driveway"],
                    port = 88,
                    user = "rudyv")})

```

<!--e_insert-->


## Example of using Camera groups in email notifications

On notifications, see [__notifier__](Notifier.md).

In this example in app_data.conf, 2 notifications are defined, whereby an email is sent and with reference to the cam group cams_street.
The email program will query the cameras in this group (left and right), take pictures, and take another picture 3 seconds later for nty_email_in as passes=2.
These pictures are then sent by email and as mail_more mentions EMAIL_notice, the email is also copied to the owners email address not only the safeguard email account.

<!--s_insert_{"tree":"(dk:street).*(o:Mailbox_alert)"}-->

from project.py tree:(dk:street).*(o:Mailbox_alert)
```python3
# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:street,o:Place,kw:contents,lp:5,o:Mailbox_alert>

from lucy_app import *

Mailbox_alert(mail_in = Input(
            effect_virtuals = {
                    "have_mail":Virtual(
                            play = Effect(maker='parent', condition='become_active', effect='make_active', taker='self', delay=None, duration=None))},
            notifications = {
                    "active":[
                        Mail(subject='{thing+is}', to='{prime}', cams=None, cam_groups=['cams_gate'], passes=2, body_file='', files2mail=None, ceiling=None),
                        Say(txt='{tts_start} new post arrived by mail{tts_end}', ceiling=None, times=1, override=None, volume=None),
                        Cal(txt='Post delivered in the mailbox', summary='', ceiling=None)]},
            path = "unipi:PI-Garden,input,6"),mail_out = Input(
            effect_virtuals = {
                    "have_mail":Virtual(
                            play = Effect(maker='parent', condition='become_inactive', effect='make_inactive', taker='self', delay=None, duration=None))},
            notifications = {
                    "active":Mail(subject='{thing+is}', to=None, cams=None, cam_groups=['cams_gate'], passes=1, body_file='', files2mail=None, ceiling=None)},
            path = "unipi:PI-Garden,input,7"),role_me = "PI-Garden")

```

<!--e_insert-->


<!--s_name_cd-->
# Camera_driver

<!--e_name_cd-->

<!--s_role_cd-->
<!--e_role_cd-->

<!--s_descr_cd-->
Driver for interfacing with camera's for pictures (pic), video (vid) and date/time (datim) setting.  Per cameratype the url's should be defined

<!--e_descr_cd-->

<!--s_tbl_cd-->
## List of [properties](Properties.md) for __Camera_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | cam_types | dict | False | - | per cam_tpe define a dictionary with url's for pic, vid and datim (picture, video and date/time setting).   Use keywords for format_map such as {ip}, {port}, {user}, which are camera specific, and {pwd} - derived from your system, and for datim {ntp_server} - from network_controller and {time_zone} which will be the time offset when you set the camera time. Monitor with Fiddler when changing manually a camera setting and then you have the string to use | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
<!--e_tbl_cd-->
