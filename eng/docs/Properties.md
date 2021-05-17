# Properties : adding features and logic

## what are properties?

<!--s_sub_toc_properties-->

Properties are extra features for a thing and they come in the form of method_things, copy_things, notifications 
and the making of a payload with effect_virtuals and value_logic.

Some or all fields are mandatory or can be repetitive in a list or dictionary form. 
The fields of this dictionary are checked for eligibility and it can be best showed through some examples.

Properties in apps are attributes such as the temperature scale °C or °F in site_settings

Properties are also available in the definition of [Inputs, Outputs, Lights, Buttons, Dimmers,..](Things.md) to define a dictionary of additional attributes.

### method properties : method_things

These are properties associated to the specific nature of a thing, such as a door which sometimes have a pulse contact to open or close the door.

There a keyword 'method_things=' is to be added followed by a dictionary structure.

Several types of properties exist and can be activated :

1. Inherited properties : properties of [basic things](Things.md) they pass on to their offspring
2. Circumstantial properties : such as the ones for a [door or window](Door.md) which are specific for the thing or the app

Some method properties have a special meaning, such as a toggle_button in an output thing (it will toggle the output when the input becomes active) and in the same way it is possible to define virtuals in properties to activate things.

### copy properties : copy_things

Copy properties add inter thing logic and make your configuration smartDefining or referring to a Virtual.

One thing can influence another, as for a Carbon copy thing, or twin copy when both things influence each other when they change value.

Other things can act as trigger or can be triggered.

### notification properties

Notification properties : for every context there is a list of possible [notifications](Notifier.md) and you are free to configure these to your needs

Such as in the example below where you want a voice notification if the internet becomes unavailable or reappears.

Properties are checked for eligibility during parsing of site.conf and error messages are generated when issues are noticed. 

Most errors stop the program altogether, as there is zero tolerance to parsing errors to ensure proper operations. 

Some examples will demonstrate how properties work.

### Example of a notification property

Use notification properties to issue a voice message and an sms when internet access or electrical power is lost or restored or when a network ping on a device fails or works again.

These properties are simply [notifications](Notifier.md):

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

Many notification properties exist and some are available through inheritance from [things](Things.md), and others are circumstantial, such as the [Weather_station](Weather_station.md) ones.

### Using Virtual's in copy properties

A more complex example involves the use of virtuals for post mail handling, see below an example :  [Mailbox_alert](Mailbox_alert.md).  

Through the definition of the properties, a voice and an email message are generated when new mail arrives and an email message is sent when the mail is removed.
The email message contains camera shots from the specified camera group which will loop 2 times (2 shots per camera 4 seconds in between).

More importantly, a self invented effect_virtual "have_mail" is maintained and set high when there is new mail and set low when the mail is removed. 
This virtual flag "have_mail" is then available somewhere else to activate a light or act on other things or apps.

<!--s_insert_{"tree":"(o:Mailbox_alert)"}-->

from project.py tree:(o:Mailbox_alert)
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

<!--e_sub_toc_properties-->


## Nesting [virtual](Virtual.md) of properties? 

Nesting of [virtual](Virtual.md) properties is allowed to a few levels deep, but it is best to keep nesting levels shallow.

So you can have a virtual being controlled by an input, controlling a few outputs.

see [__a gate entrance door example__](Door.md) for a complex nesting structure and the extensive use of flags and notifications.

Although this may look like programming, you can easily add features without changing any of the programming scripts.

Please study the myproject.py example for tricks and features you may need.

<!--s_name_me-->
# method_things

<!--e_name_me-->

<!--s_descr_me-->
additional settings about a thing, adding features and logic

<!--e_descr_me-->

<!--s_name_ef-->
# effect_virtuals

<!--e_name_ef-->

<!--s_descr_ef-->
effects things can have on each others such as striking a value when another thing gets active or inactive

<!--e_descr_ef-->

<!--s_name_cp-->
# copy_things

<!--e_name_cp-->

<!--s_descr_cp-->
additional settings about a thing, adding features and logic

<!--e_descr_cp-->

