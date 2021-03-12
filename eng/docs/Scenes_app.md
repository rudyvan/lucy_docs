<!--s_name-->
# Scenes_app

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
TBI/Scenes App, containing scenes that can be triggered in a calendar, by sms, by email, by twitter, by IFTTT, by Vera, by UDP, by TCP.  The scene id's are the key for the feeder to know what to do when the event_id is received through one of the feeder's channels

<!--e_descr-->

<!--s_tbl-->
## List of [properties](Properties.md) for __Scenes_app__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | do_scenes | Virtual | False | - | = virtual, when reset, scenes will be ignored as are triggers (unless No_Matter_What) | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | role_me | {tc} | False | - | role_me of 'Scenes_app', adds <scenes> to the roles of the specified tc | 
  | scenes | dict | False | - | TBI/a dictionary of a list of commands that will be run in sequence, just like access_scenes in Access_manager | 

## List of [Errors/Warnings](Error_Warn.md) for  __Scenes_app__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_event_crash | !!Event <{:}> crashed |  
<!--e_tbl-->

