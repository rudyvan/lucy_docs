<!--s_name-->
# Ping

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
is a network function to check the presence of a thing through a ping

<!--e_descr-->

<!--s_tbl-->
## List of [properties](Properties.md) for __Ping__:

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
  | ip_action | valid_set_int | False | - | ip_action=-1 (no ping), 0 (ping), 1 (ping and if lost then internet alarm) | 
  | member_of | list | True | - | a list of group names to which thing belongs | 
  | notifications | ['active', 'app_done', 'app_start', 'check_fail', 'check_ok', 'disable_off', 'disable_on', 'enable_off', 'enable_on', 'freeze_off', 'freeze_on', 'inactive', 'none', 'notify_binary+', 'payload_no'] | True | - | the notifications for pings, see [__Notifier__](Notifier.md) | 
  | play | tuple:virtual_tuples | True | - | the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on' | 
  | short | str | False | - | free (preferably short) description for this thing | 
  | spec_func | str | False | - | special function attribute | 
  | th_grp | str | False | - | the technical group to which this thing belongs, used in groupings for lists and reports | 

## List of [Notifications](Notifier.md) for  __Ping__:

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
<!--e_tbl-->

