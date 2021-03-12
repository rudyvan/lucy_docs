<!--s_name-->
# Doorbell

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
Most doorbells drive a bell button signal and have a way to signal agreement to open or lock one or more doors.  You can also declare a doorbell inside a door.

<!--e_descr-->

In a future version a link to Slack http://www.slack.com/ will be initiated, allowing direct video communication between the doorbell and a mobile device for remote operation of the doorbell.

<!--s_tbl-->
## List of [properties](Properties.md) for __Doorbell__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | close_cmd | Input | True | - | the 'close the door' pulse from the doorbell that can trigger doors or events | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | notifications | ['ring', 'ring_away'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 
  | open_cmd | Input | True | - | the 'open the door' pulse from the doorbell that can trigger doors or events | 
  | ring_button | Input | False | - | the bell button | 
  | role_me | {tc} | False | - | role_me of 'Doorbell', adds <doorbell> to the roles of the specified tc | 

## List of [Notifications](Notifier.md) for  __Doorbell__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | ring | when the bell button is pressed | 
  | ring_away | when the bell button is pressed when home_occupation is away | 
<!--e_tbl-->

## Example doorbell

In this example 3 inputs are used, one for the bell, one for the open command and one for the close command.
When the bell button is activated, then a voice message will go through the house announcing someone at the door, an email is fired with pictures from the camera's at the entrance and an IFTTT event is fired with the name doorbell.

Further a virtual is raised 'have_ring' which activates the light_night (see [Door.md](Door.md) example configuration). 

<non generated example--s_insert_{"tree":"(dk:street).*(o:Doorbell)"}-->

from project.py tree:(dk:street).*(o:Doorbell)
```python3
--> project.py :<dk:project,o:Project,kw:property,o:House,kw:places,dk:street,o:Place,kw:contents,lp:3,o:Doors,kw:items,dk:gate,o:Door,kw:method_things,dk:doorbell,o:Doorbell>

Doorbell(
    close_cmd = Input(path = "unipi:PI-Gate,input,7"),
    notifications = {
            "ring":[
                Mail(subject='{thing+is}', to=None, cams=None, cam_groups=['cams_street'], passes=2, body_file='', files2mail=None, ceiling=None),
                Say(txt='{tts_start} someone is ringing the bell{tts_end}', ceiling=None, times=1, override=True, volume=None),
                Say(txt='{tts_prop} ring, ring the doorbell{tts_end}', ceiling=None, times=1, override=True, volume=None),
                Say(txt='{tts_prop} ding dong, ding dong{tts_end}', ceiling=None, times=1, override=True, volume=None),
                Say(txt='{tts_prop} ring, ring, someone is at the door{tts_end}', ceiling=None, times=1, override=True, volume=None),
                Cal(txt='RING_doorbell', summary='', ceiling=None),
                Ifttt(txt='door_bell', ceiling=None)],
            "ring_away":[
                Mail(subject='{thing+is}', to='{prime}', cams=None, cam_groups=['cams_street'], passes=2, body_file='', files2mail=None, ceiling=None),
                Cal(txt='RING_doorbell when away', summary='', ceiling=None)]},
    open_cmd = Input(path = "unipi:PI-Gate,input,8"),
    ring_button = Input(effect_virtuals = {
                    "have_ring":Virtual(
                            play = Effect(maker='parent', condition='become_active', effect='make_active', taker='self', delay=None, duration=None))},owned_by = "building",path = "unipi:PI-Gate,input,5"),
    role_me = "PI-Gate")

```

<--e_insert-->
