<!--s_name-->
# Sonos

<!--e_name-->

<!--s_role-->
<!--e_role-->

## Summary

<!--s_descr-->
is a network function to check the presence of a thing through a ping

<!--e_descr-->

Sonos has a broad range of speakers.

![sonos](sonos.jpg)

<!--s_tbl-->
## List of [properties](Properties.md) for __Sonos__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | active | valid_set_int | False | - | designate the active state for a binary thing, either 0 or 1 | 
  | descr | str | False | - | free description field for this thing | 
  | descr_01 | list-2 | False | - | description for a binary thing when payload value is 0 or 1 | 
  | duration | float | False | - | duration of the output being active/ input must be active for duration before considered active | 
  | effect_virtuals | ['Virtual', 'Virtual_A', 'Virtual_R'] | False | True | virtual things that are affected by, or can have an effect on, the value of the parent thing | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | ip | str | False | - | ip in the format of xx.xx.xx.xx | 
  | ip_action | int | True | - | - | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'inactive', 'none', 'notify+', 'payload_no'] | True | - | the notifications for pings, see [__Notifier__](Notifier.md) | 
  | override_only | bool | True | - | boolean if zone controller | 
  | ping | bool | True | - | if need to be ping | 
  | play | tuple:virtual_tuples | True | - | the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on' | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | soco_controller | bool | True | - | boolean if this Sonos speaker is considered a zone controller.  For maximum performance in big networks select a Sonos speaker that is 1)not paired, 2)good network reach, 3)not override_only, 4)not likely to be grouped.  Minimal one speaker should be zone_controller!! | 
  | sonos_type | str | True | - | - | 
  | spec_func | str | False | - | - | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 

## List of [Notifications](Notifier.md) for  __Sonos__:

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
<!--e_tbl-->

For a description of the parameters, see the example below.


## How does Sonos voice messaging work?

see also [notifier](Notifier.md).

Sonos sound is produced with the python sonos soco module https://github.com/SoCo/SoCo.

Actually 3 scenario's exist for using sonos speakers for multiroom notification messages:

1. : use party mode.  Is fast but inconvenient when watching television, your program is interupted
2. : use existing zones in place.  Is fast but when the rooms are adject, the sound echo's strangely
3. : group the zones together but excluding the playbar zone when playing television.  Play the message(s) and then restore the zones the way they were before.   Is somewhat slower, but best sound and comfort (as the TV keeps playing uninterrupted).

By default, scenario 3 is used.

The notifier will present the text to speech wave file to the zone controller to get the message out.
Inside a Flask script is used as sound file web server to respond to the sonos zone controllers play uri sound messages.

## Example Sonos configuration

Below is a list of different sonos speakers per room.

It appears that sonos connect devices are not pingable, so they are excluded.

Also the sonos playbar is excluded of being zone_controller as the sound everywhere is then strangely intermittent and not smooth.

One sonos speaker is in the kitchen on wifi and excluded from ping. 

<!--s_insert_{"tree":["(o:Sonos_driver)","(dk:veranda).*(o:Music_players)","(dk:living_lounge).*(o:Music_players)","(dk:kitchen).*(o:Music_players)","(dk:office).*(o:Music_players)"]}-->

from project.py tree:['(o:Sonos_driver)', '(dk:veranda).*(o:Music_players)', '(dk:living_lounge).*(o:Music_players)', '(dk:kitchen).*(o:Music_players)', '(dk:office).*(o:Music_players)']
```python3
# --> project.py :<dk:project,o:Project,kw:drivers,lp:6,o:Sonos_driver>

from lucy_app import *

Sonos_driver(party_mode = False)

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:veranda,o:Room,kw:contents,lp:2,o:Music_players>

from lucy_app import *

Music_players(items = [Sonos(ip = "192.168.15.161",ip_action = 0,sonos_type = "PLAY:1"),Sonos(ip = "192.168.15.160",ip_action = 0,sonos_type = "PLAY:1")])

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:living_lounge,o:Room,kw:contents,lp:6,o:Music_players>

from lucy_app import *

Music_players(items = [
        Sonos(ip = "192.168.15.114",ip_action = 0,sonos_type = "SUB"),
        Sonos(ip = "192.168.15.115",ip_action = 0,sonos_type = "PLAY:1"),
        Sonos(ip = "192.168.15.99",ip_action = 0,sonos_type = "PLAY:1"),
        Sonos(ip = "192.168.15.90",ip_action = 0,sonos_type = "PLAYBAR")])

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:kitchen,o:Room,kw:contents,lp:5,o:Music_players>

from lucy_app import *

Music_players(items = [Sonos(ip = "192.168.15.111",ip_action = 0,sonos_type = "PLAY:1"),Sonos(ip = "192.168.15.83",ip_action = 0,sonos_type = "PLAY:1")])

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:office,o:Room,kw:contents,lp:6,o:Music_players>

from lucy_app import *

Music_players(items = [Sonos(ip = "192.168.15.107",ip_action = 0,sonos_type = "PLAY:1"),Sonos(ip = "192.168.15.101",ip_action = 0,sonos_type = "PLAY:1")])

```

<!--e_insert-->

* * * 
* * * 
# Reporting Sonos Overview 

Below an overview report is presented of all the TTS (text to speech) messages aired through the sonos sound system, if volume is zero, then the message was ignored, such a report is always available but is daily emailed at midnight.

* * * 
* * * 

<!--s_insert_{"role":"notifier","suffix":"say_log"}-->


[PI-Stats_say_log.html](PI-Stats_say_log.html)

<!DOCTYPE html><html><body><h1>Voice Notifications -> PI-Stats_cum.html  2020/11/08 20:28:25</h1><table><thead><tr><th>Date</th><th>Time</th><th>SAY_id</th><th>Volume</th><th>Repeats</th><th>Room</th><th>Duration</th><th>Message</th></tr></thead><tbody><tr><td>2020-11-08</td><td>19:52:25</td><td>say_sun_light.high</td><td>30</td><td>1</td><td>OFFICE</td><td>6</td><td>&lt;prosody rate=&#x27;medium&#x27;&gt;Hi honey, it is a bright day outside, surely good for your mood&lt;/prosody&gt;</td></tr><tr><td>2020-11-08</td><td>19:51:51</td><td>say_climate.office.clim_on_0</td><td>30</td><td>2</td><td>OFFICE</td><td>5</td><td>&lt;prosody rate=&#x27;medium&#x27;&gt;Hi honey, office climatisation is de-activated&lt;/prosody&gt;</td></tr><tr><td>2020-11-08</td><td>19:50:42</td><td>say_climate_manager.comfort_1</td><td>30</td><td>1</td><td>All Sonos</td><td>5</td><td>&lt;prosody rate=&#x27;medium&#x27;&gt;Hi honey, house is set to comfort climatisation&lt;/prosody&gt;</td></tr><tr><td>2020-11-08</td><td>19:50:24</td><td>say_climate.daughter.sleep.clim_on_0</td><td>30</td><td>2</td><td>DAUGHTER</td><td>6</td><td>&lt;prosody rate=&#x27;medium&#x27;&gt;Hi honey, rebeccas room climatisation is de-activated&lt;/prosody&gt;</td></tr></tbody></table></body></html>
<!--e_insert-->
 



