<!--s_name-->
# Virtual

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
Virtual's are an important vehicle to obtain smart configurations whereby interaction and dependencies between Things and Apps can be arranged, think of Virtuals as abstract rather than real things

<!--e_descr-->

<!--s_sub_toc_vir1-->

When pondering the strategy to separate home specific configuration from programming logic, the idea emerged of using virtual things to make the configuration smart and to have a powerful design mechanism to have logic in the home configuration file.
It worked out better than anticipated, and the result is a very powerful combination.
The negatives, cluttering the configuration file with virtuals from apps or own invented virtuals has proven to be manageable although the syntax of closing parentheses and braces can drive you almost nuts.
However, it clearly delivers the result of separating home configuration data from the processing code.

Let's see how this works and we will cover the different virtuals, things that can have an imaginary payload not linked to the real world as real things can:

- app virtuals : they are created and used in the context of an App. Some are mandatory and have to be defined in order for the App to work.
- effect virtuals : things that can do a play: receive an effect or splash an effect on a parent
 
To illustrate the syntax in the example below, the Network_controller App has 1 "App" virtual 'internet_lost'.
This is an object starting with __Virtual()__, used for signaling the loss of internet in other places in the PHCF.

Another virtual 'power_flag', further down in the example, is a (non app) effect_virtual where the play is an effect: when power_ok becomes active, self (power_flag) is made active.

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
            "network":Mail(subject='Network Report - Lost={app_txt}', to='{prime}', cams=None, cam_groups=None, passes=0, body_file='ip', files2mail=None, ceiling=None)},
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

The security_system app has more than a dozen app virtuals defined, to be used in your PHDF.

As you learned in the example, it is possible to define own virtual things simply by creating them where needed with a name and an effect that defines the purpose.
These are called effect_virtuals,  
The config parser "knows" when a virtual is referenced when it has its name registered in a previous context.
Virtuals can do something on the thing(s) they are linked to (the parent acts) or inverse (self acts on the parent) and this is called a play.

The play is a named tuple "Effect" with fields: ["maker", "condition", "effect", "taker", "duration", "delay"].

- maker = self, parent : the thing that takes the initiative, the thing that defines the effect_virtual (parent) or the effect_virtual itself (self)
- condition = what condition activates the effect to make
- effect = what to do on the taker
- taker = the thing that the maker to act upon (must be the opposite of maker)
- duration = (optional) seconds for the duration of the effect
- delay = (optional) seconds before the effect to happen

For a Virtual Range thing, the 'condition' can be a list of discrete values (digital_range) or a from - till range for an analog range virtual

See below the valid values for each of the fields:

<!--s_insert_{"prj_parser":"app_obj.conf","section":"VIRTUAL_PARAMETERS","var":"play"}-->

from app_obj.conf:
```python3
[VIRTUAL_PARAMETERS]

play={"maker":    ["self","parent"],
	"condition":["become_active","become_inactive","i_change","when_active","when_inactive"],
	"effect":   ["make_active","make_inactive","make_toggle","make_same", "active_freeze","inactive_freeze","make_{val}"],
	"taker":    ["parent","self"],
	"delay":    None,
	"duration": None}

```

<!--e_insert-->


<!--e_sub_toc_vir1-->

A bigger example can be found in the security system app where many Virtual()'s are available:

<!--s_insert_{"tree":"(o:Security_system)"}-->

from project.py tree:(o:Security_system)
```python3
# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:garage,o:Room,kw:contents,lp:9,o:Security_system>

from lucy_app import *

Security_system(
    blackout_mode = Virtual(duration = 600,effect_virtuals = {
                    "is_reboot":Virtual(
                            play = Effect(maker='self', condition='become_active', effect='make_active', taker='parent', delay=None, duration=None))}),
    daily_routine = Virtual(
            notifications = {
                    "active":Vera_nty(txt='vera_open_curtains'),
                    "app_done":Log(txt='unarm briefly completed', ceiling=None),
                    "app_start":Log(txt='unarm briefly started', ceiling=None),
                    "inactive":Vera_nty(txt='vera_close_curtains')},
            things_app = "unarm_briefly",
            value_logic = {"assign":{"is_day":"True","is_not_day":"False"},"freeze":{"sleep":True}}),
    do_alarm = Virtual(duration = 1),
    do_arm_at_close = Virtual(),
    do_arm_full = Virtual(duration = 90),
    do_arm_full_req = Virtual(duration = 1),
    do_arm_partial = Virtual(duration = 90),
    do_arm_partial_req = Virtual(duration = 4),
    do_burglar = Virtual(duration = 1),
    do_fire = Virtual(duration = 1),
    do_unarm = Virtual(duration = 1),
    is_alarm = Virtual(copy_things = {
                    "carbon_copy":Output(path = "vera:Vera_plus,zw,buttonset,173,Status6")},effect_virtuals = {
                    "dw_autom_close":Virtual(
                            duration = 600,
                            play = Effect(maker='parent', condition='i_change', effect='make_same', taker='self', delay=None, duration=None)),
                    "dw_autom_open":Virtual(
                            duration = 2,
                            play = Effect(maker='parent', condition='become_active', effect='make_active', taker='self', delay=None, duration=None))}),
    is_alarm_eminent = Virtual(duration = 90),
    is_arm_eminent = Virtual(duration = 90),
    is_armed = Virtual(
            effect_virtuals = {
                    "dw_autom_close":Virtual(
                            duration = 600,
                            play = Effect(maker='parent', condition='become_active', effect='make_active', taker='self', delay=None, duration=None))},
            notifications = {
                    "active":[
                        Mail(subject='Alarm is Armed', to=None, cams=None, cam_groups=['cams_alarm'], passes=1, body_file='', files2mail=None, ceiling=None),
                        Cal(txt='Alarm is Armed', summary='', ceiling=None)],
                    "inactive":[
                        Mail(subject='Alarm is Unarmed', to=None, cams=None, cam_groups=['cams_alarm'], passes=1, body_file='', files2mail=None, ceiling=None),
                        Cal(txt='Alarm is Unarmed', summary='', ceiling=None)]}),
    is_armed_full = Virtual(),
    is_armed_partial = Virtual(effect_virtuals = {
                    "wakeup_curtains":Virtual(
                            notifications = {"inactive":Vera_nty(txt='vera_open_curtains')},
                            play = Effect(maker='parent', condition='i_change', effect='make_same', taker='self', delay=None, duration=None),
                            value_logic = {"freeze":{"is_not_day":True}})}),
    is_burglar = Virtual(notifications = {"active":Vera_nty(txt='vera_open_curtains')}),
    is_fire = Virtual(copy_things = {
                    "carbon_copy":Output(path = "vera:Vera_plus,zw,buttonset,173,Status7")}),
    light_armed_warn = Light(
            copy_things = {
                    "carbon_copy":Output(path = "unipi:PI-Veranda,relay,8")},
            duration = 1800,
            effect_virtuals = {
                    "do_arm_at_close":Virtual(
                            play = Effect(maker='self', condition='i_change', effect='make_same', taker='parent', delay=None, duration=None))},
            path = "unipi:PI-Security,relay,5"),
    maintenance_mode = Virtual_R(descr_range = ["OFF","Ignore Master","Ignore Slave","Silent_only"],digital_range = [0,1,2,3]),
    master_r_armed_always = Input(path = "unipi:PI-Security,input,5"),
    master_r_armed_partial = Input(path = "unipi:PI-Security,input,6"),
    master_r_burglar = Input(path = "unipi:PI-Security,input,3"),
    role_me = "PI-Security",
    safe_ways = {
            "entry_way":["garage_rear_door","garage","main_entrance","old_entrance","movement_veranda"],
            "exit_way":["garage_rear_door","garage","main_entrance","old_entrance","movement_veranda"]},
    si_system_type = Virtual_R(descr_range = ["Slave","Alone","Master","Hybrid"],digital_range = [-1,0,1,2]),
    slave_s_arm_full_t = Output(duration = 2,path = "unipi:PI-Security,relay,3"),
    slave_s_arm_partial_t = Output(duration = 2,path = "unipi:PI-Security,relay,6"),
    slave_s_burglar = Output(duration = 12,path = "unipi:PI-Security,relay,14"),
    slave_s_fire = Output(duration = 12,path = "unipi:PI-Security,relay,4"),
    zones = {"always_zones":["house"],"ignore_zones":["street","garden"],"partial_zones":["sleep"]})

```

<!--e_insert-->


<!--s_sub_toc_vir2-->

For effect_virtuals, the syntax of the play is built to almost have a readable sentence, just read the examples below:

Examples of plays where the parent acts on the Virtual self:

```python3
play=Effect(maker="parent", condition="become_active",   effect="make_active",   taker="self")
play=Effect(maker="parent", condition="become_inactive", effect="make_inactive", taker="self")
play=Effect(maker="parent", condition="changes",         effect="make_toggle",   taker="self")
play=Effect(maker="parent", condition="changes",         effect="make_same",     taker="self")
play=Effect(maker="parent", condition="become_active",   effect="make_inactive", taker="self")

```

Examples of plays where the self Virtual acts on the parent:

```python3     
play=Effect(maker="self", condition="become_active",   effect="make_active",     taker="parent")
play=Effect(maker="self", condition="become_inactive", effect="make_active",     taker="parent")
play=Effect(maker="self", condition="become_inactive", effect="make_inactive",   taker="parent")
play=Effect(maker="self", condition="become_active",   effect="make_inactive",   taker="parent")
play=Effect(maker="self", condition="changes",         effect="make_toggle",     taker="parent")
play=Effect(maker="self", condition="when_inactive",   effect="freeze_inactive", taker="parent")
```

Example of a Virtual Range play:

For a Virtual Range thing, the 'condition' can be a list of discrete values (digital_range) or a from - till range for an analog range virtual

```python3
play=Effect(maker="self", condition=[0,2], effect="freeze_inactive", taker="parent")
```

<!--e_sub_toc_vir2-->


Just remember that a binary thing is normally active when it achieves a high state but with **active=0**, the inverse is stated.

Also good to know in this context is that Doors and Windows have an active state when they are closed.

Range Virtuals have parameters to state the range when the action should apply, as in the following example where the phone warning dialer should not work if the Internet is down and you are sleeping or you are in the house (home_occupancy is then 0 or 2):

This rather complex example demonstrates 2 levels deep nesting of effect_virtuals with a range virtual.

```python3
pho_say_internet_lost=Output(
       duration=40, 
       path="piface:PI-Data,do,2"), 
       effect_virtuals={
            "internet_lost": Virtual(
                    duration=2, 
                    play=Effect(maker="self", condition="become_active", effect="make_active", taker="parent"),
                    effect_virtuals={
                            "home_occupancy": Virtual_R(
                                     descr_range="Day,Away,Sleep,Holiday", 
                                     digital_range="0,1,2,3",
                                     play=Effect(maker="self", condition=[0,2], effect="freeze_inactive", taker="parent"))})})
```

Also refer to the previous examples whereby a user virtual is created that shows a light when new post arrives, but the light only shows when the gate opens, such as when you are entering or leaving the house and want to know if you should stop to take the mail.
Look at the above example of mail_notification where the virtual __have_mail__ is created and used in the previous door example where the __have_mail__ virtual is used again to prohibit the light.

More complex examples exists where specific doors open automatically in case an fire or burglar alarm. 

## Delay and Duration

Virtuals that are acting on things can have parameters whereby the parameters are specified in a dict form:

  | Attribute | Representation | Optional? | Description |
  | --- | --- | --- | --- |
  | delay    | seconds | yes | delays the virtual to_do for x seconds |
  | duration | seconds | yes | duration that the virtual to_do impacts for x seconds, thereafter the thing becomes inactive |
  | list |   list of range values | mandatory for __Virtual_R__ | must match one of the values in the list for the to_do to happen |

<!--s_tbl-->
## List of [properties](Properties.md) for __Virtual__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | active | valid_set_int | False | - | designate the active state for a binary thing, either 0 or 1 | 
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | descr_01 | list-2 | False | - | description for a binary thing when payload value is 0 or 1 | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'check_fail', 'check_ok', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'inactive', 'none', 'notify_binary+', 'payload_no'] | True | - | the notifications for virtuals, see [__Notifier__](Notifier.md) | 
  | play | tuple:virtual_tuples | True | - | the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on' | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_app | tuple:value_app_tuples | True | - | app logic to determine the payload based programming logic and input parameters | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 

## List of [Notifications](Notifier.md) for  __Virtual__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is non zero | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | check_fail | the vfy_same_delayed thingsmethod fails after the set time and the input does not reflects the parent output | 
  | check_ok | the vfy_same_delayed thingsmethod succeeds after the set time and the input reflects the parent output | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | inactive | when payload is zero | 
  | none | value of the Virtual is None | 
  | notify_binary+ | extra notifications that apply to all binary type things | 
  | payload_no | the requested payload is refused | 

## List of [copy_things] for  __Virtual__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 

## List of [Errors/Warnings](Error_Warn.md) for  __Virtual__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | msg_virtual_play | PLAY '{}' on '{}' with '{}' --> {} |  
<!--e_tbl-->

<!--s_name_aflg-->
# Virtual_A

<!--e_name_aflg-->

<!--s_descr_aflg-->
Analog type Virtual

<!--e_descr_aflg-->

<!--s_tbl_aflg-->
## List of [properties](Properties.md) for __Virtual_A__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | i_read | str | True | - | the type of data that this sensor reads | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'deicing', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'freezing', 'inactive', 'negative', 'nothing_is', 'notify_analog+', 'payload_no', 'positive', 'when_is>{cur_state}'] | True | - | similar for the notifications for Sensors, see [__Notifier__](Notifier.md) | 
  | play | tuple:virtual_tuples | True | - | the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on' | 
  | scalar | data_dict | True | - | a function that maps a things value within a certain range to another range such as scalar={'in':[24,100], 'out':[0,100]} which returns 0 if the thing reads 24.  It is currently only implemented on usb:arduino and unipi inputs. | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | threshold | float | False | - | the minimum % that an analog input must change before the value is considered changed | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 

## List of [Notifications](Notifier.md) for  __Virtual_A__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is non zero | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | deicing | temperature becomes positive | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | freezing | temperature becomes below zero | 
  | inactive | when payload is zero | 
  | negative | when payload reaches negative, coming from a positive payload | 
  | nothing_is | when payload does not encounter any active conditional notification when there were previously | 
  | notify_analog+ | extra notifications that apply to all analog type things | 
  | payload_no | the requested payload is refused | 
  | positive | when payload reaches positive or zero coming from a negative payload | 
  | when_is>{cur_state} | if the current value is > cur_state (or <, =) | 

## List of [copy_things] for  __Virtual_A__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_aflg-->

<!--s_name_rflg-->
# Virtual_R

<!--e_name_rflg-->

<!--s_descr_rflg-->
Range Virtual's do not just have a binary state such as ordinary virtuals but they can have a value in a range of consecutive integer numbers

<!--e_descr_rflg-->

<!--s_tbl_rflg-->
## List of [properties](Properties.md) for __Virtual_R__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Virtual_R']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Virtual_R']}, 'carbon_copy@{val}': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light']}, 'twin_copy@{val}': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | descr_range | str | False | - | a list of strings corresponding to the digital_range | 
  | digital_range | str | False | - | a sequential list of integers determining the first, last and other possible states | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['going_down', 'going_up', 'high', 'low', 'normal', 'val_', 'when_is>{cur_state}'] | True | - | the notifications for range virtuals. val_ can be followed with the value of the virtual, see [__Notifier__](Notifier.md) | 
  | play | tuple:virtual_tuples | True | - | the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on' | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 

## List of [Notifications](Notifier.md) for  __Virtual_R__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | going_down | when the payload decreases | 
  | going_up | when the payload increases | 
  | high | when the payload reaches high | 
  | low | when the payload reaches low | 
  | normal | when payload becomes lower than high or higher than low | 
  | val_ | when a specific value has been reached | 
  | when_is>{cur_state} | if the current value is > cur_state (or <, =) | 

## List of [copy_things] for  __Virtual_R__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Virtual_R'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | carbon_copy@{val} | ['Output', 'Motor', 'Light', 'Dim_light'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Virtual_R'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
  | twin_copy@{val} | ['Output', 'Motor', 'Light', 'Dim_light'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_rflg-->

<!--s_name_mflg-->
# Fake_meter

<!--e_name_mflg-->

<!--s_descr_mflg-->
Virtual meter for the registration of calculated meter values, for example the water consumption in a T pipe when real meters work for 2 of the 3 legs.

<!--e_descr_mflg-->

<!--s_tbl_mflg-->
## List of [properties](Properties.md) for __Fake_meter__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect | valid_list | False | - | effect of utility measured, + for adding, - for reducing and +- or -+ for a hybrid node where it can add or reduce | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | i_read | str | False | - | the type of data that this meter stores | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | method_things | ['fake_sensor', 'sensor'] | True | - | special methods of this thing, mostly realised through things | 
  | notifications | ['app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'notify+', 'payload_no', 'sum_day>{d}', 'sum_hour>{h}', 'sum_minute>{m}', 'sum_month>{M}', 'sum_month[]>{M}', 'sum_now>{cur_state}', 'sum_week>{w}', 'sum_weekday[]>{d}', 'sum_year>{y}'] | True | - | similar for the notifications for Meters, see [__Notifier__](Notifier.md) | 
  | play | tuple:virtual_tuples | True | - | the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on' | 
  | rate | dict | True | - | rate per effect and per unit to determine utility usage cost, can be a dict specifying different rates during the day or for weekdays | 
  | rate_fictive | dict | True | - | fictive rate per effect and per unit to determine utility usage cost, can be a dict specifying different rates during the day or for weekdays.  An example is a fictive rate for hot domestic water, the cost of water and heating is already in other utilities, but calculating and printing the cost of heated water on itself can provide useful information. | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | threshold | float | False | - | the minimum % that an analog input must change before the value is considered changed | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 

## List of [Notifications](Notifier.md) for  __Fake_meter__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | notify+ | extra notifications | 
  | payload_no | the requested payload is refused | 
  | sum_day>{d} | if the current day sum is above (>), below (<) or equal (=) to d | 
  | sum_hour>{h} | if the sum of the last hour ago is above (>), below (<) or equal (=) to h | 
  | sum_minute>{m} | if the sum of the last minute ago is above (>), below (<) or equal (=) to m | 
  | sum_month>{M} | if the current month sum is above (>), below (<) or equal (=) to M | 
  | sum_month[]>{M} | if the current month is in [..] and the sum is above (>), below (<) or equal (=) to M | 
  | sum_now>{cur_state} | if the current meter level is > cur_state | 
  | sum_week>{w} | if the current week sum is above (>), below (<) or equal (=) to w | 
  | sum_weekday[]>{d} | if the current week day position (monday=1) in [] and that day sum is above (>), below (<) or equal (=) to d | 
  | sum_year>{y} | if the current year sum is above (>), below (<) or equal (=) to y | 

## List of [copy_things] for  __Fake_meter__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 

## List of [method_things] for  __Fake_meter__:

  | Method Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | fake_sensor | *Fake_sensor | {'descr': 'virtual sensor associated with the meter, such as power for an electricity meter or temperature for heated water', 'short': 'fake_sensor'} | 
  | sensor | *Sensor | {'descr': 'the sensor associated with the meter, such as power for an electricity meter or temperature for heated water', 'short': 'sensor'} | 
<!--e_tbl_mflg-->

<!--s_name_sflg-->
# Fake_sensor

<!--e_name_sflg-->

<!--s_descr_sflg-->
Virtual sensor for the registration of calculated sensor values, for example the electricity power taken to make the sum of power users zero.

<!--e_descr_sflg-->

<!--s_tbl_sflg-->
## List of [properties](Properties.md) for __Fake_sensor__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | copy_things | {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor']}} | False | - | copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions) | 
  | descr | str | False | - | free description field for this thing | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | i_read | str | False | - | the type of data that this meter stores | 
  | icon | str | True | - | icon file for this element | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'deicing', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'freezing', 'inactive', 'negative', 'nothing_is', 'notify_analog+', 'payload_no', 'positive', 'when_is>{cur_state}'] | True | - | similar for the notifications for Meters, see [__Notifier__](Notifier.md) | 
  | play | tuple:virtual_tuples | True | - | the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on' | 
  | scalar | data_dict | True | - | a function that maps a things value within a certain range to another range such as scalar={'in':[24,100], 'out':[0,100]} which returns 0 if the thing reads 24.  It is currently only implemented on usb:arduino and unipi inputs. | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 
  | threshold | float | False | - | the minimum % that an analog input must change before the value is considered changed | 
  | value_logic | dict | False | - | logic to automatically determine the payload  based on time or other things | 

## List of [Notifications](Notifier.md) for  __Fake_sensor__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | active | when payload is non zero | 
  | app_done | when a things_app completes | 
  | app_start | when a things_app starts | 
  | deicing | temperature becomes positive | 
  | disable_off | when all of the disable conditions fail | 
  | disable_on | when one of the disable conditions succeed | 
  | enable_off | when one of the enable conditions fail | 
  | enable_on | when all the enable conditions succeed | 
  | freeze_off | all of the freeze conditions fail | 
  | freeze_on | one of the freeze conditions succeed | 
  | freezing | temperature becomes below zero | 
  | inactive | when payload is zero | 
  | negative | when payload reaches negative, coming from a positive payload | 
  | nothing_is | when payload does not encounter any active conditional notification when there were previously | 
  | notify_analog+ | extra notifications that apply to all analog type things | 
  | payload_no | the requested payload is refused | 
  | positive | when payload reaches positive or zero coming from a negative payload | 
  | when_is>{cur_state} | if the current value is > cur_state (or <, =) | 

## List of [copy_things] for  __Fake_sensor__:

  | Copy Thing | Type Thing | What it does? |
  | --- | --- | --- | 
  | carbon_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'} | 
  | twin_copy | ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A', 'Fake_sensor'] | {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'} | 
<!--e_tbl_sflg-->


