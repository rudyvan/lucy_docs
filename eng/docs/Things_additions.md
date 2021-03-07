<!--s_name-->
# Things_additions

<!--e_name-->

<!--s_role-->
<!--e_role-->

## Summary

<!--s_sub_toc_th_a-->

Imagine you can specify somewhere what data is to be collected about every thing you have in the home.

Such data could be:
* ownership : maybe some of the things are not owned by yourself, but by the owner of the building
* utility_usage : some things use electricity, then you specify Watts, other things use water for irrigation, and then you have liters/minute
* an alternative label : one wire temperature sensors all look the same
* any other information need or app that will be released

With the above data you can estimate power and water consumption for all the things in scope because your home controller knows when they are active.
Both apps Forensics and Utility_usage work together to get this overview accomplished.

Other properties could be more than data, say a sirens test associated with a siren thing.

This is what things_apps stands for, to allow you to define the data or app for your things or just one Thing.

<!--e_sub_toc_th_a-->

The app data is somewhat particular as the entry validation is specified.

<!--s_descr-->
Some Apps have something to do with specific things (such as a sirens_test with an Alarm_siren) or you need to define an App that collects data for every thing defined, then this App is the one to use

<!--e_descr-->

<!--s_tbl-->
## List of [properties](Properties.md) for __Things_additions__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | items | data_dict | False | - | Some Apps have something to do with specific things (such as a sirens_test with an Alarm_siren) or you need to define an App that collects data for every thing defined, then this App is the one to use | 

## List of [Errors/Warnings](Error_Warn.md) for  __Things_additions__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_am_i_get_my | !!am_i_get_my error, in th {:}, <{:}> is not in {:} |  
  | err_decode | !!unipi Decode, ?device? {:} |  
  | err_eds_ow | !!Processing eds_ow error = {:} on {:} |  
  | err_event_pars | !!Scene Error: {:} |  
  | err_logic | !!Logic Error in {:}: {:}<>{:} |  
  | err_mk_me | !!mk_me error, in th {:}, <{:}> ? {:} |  
  | err_pickle_load | !!pickle file reloading of <{:}> failed {:} |  
  | err_render_cols_len | !!render {:}, generator {:}, has t={:} and not matches {:} header strings |  
  | err_render_do | !!Error in rendering table_do in <{:}> : {:} {:} {:} |  
  | err_render_gen_prg | !!render {:}, generator {:} is not defined in dir() : {:} |  
  | err_render_logic | !!render {:}, generator?? {:} <> {:} |  
  | err_render_report | !!render name {:} not in [REPORT] section of app_obj.conf, called from {:} |  
  | err_renson | !!Processing Renson error = {:} on {:} |  
  | err_repr_len | !!decorator repr len is zero |  
  | err_unipi_nok | !!unipi {:} {:} -> {:}/{:} {:} |  
  | err_upd | !!update of {:} with {:} failed |  
  | event_arm_brief | Scene trigger: arm after briefly unarm |  
  | event_unarm_brief | Scene trigger: unarm briefly for {:} |  
  | event_unarm_brief_no | Scene trigger: unarm briefly for {:} not needed |  
  | msg_render_not | rendering {:} canceled by if: {:} |  
  | msg_sirens_test | Sirens Test |  
  | msg_sun | sun rises at {:} and sets at {:} |  
<!--e_tbl-->

Thing specific things_apps are a piece of code attached to a Thing, think of it as structured properties.

Currently the following things specific apps exist:

  | things_apps | Device | Description |
  | --- | --- | --- |
  | unarm_briefly | Virtual | use with caution as this works on any virtual, and this event briefly disables the alarm |
  | sirens_test | Alarm_siren | triggers a sirens test event every 1st day of new month at 12am |

## Example of __unarm_briefly__

In the below example, a daily routine is run by the security manager at sunrise and sunset when the security system is not partly armed (house not in sleep mode).
This daily routine involves opening and closing the curtains through the vera_driver (these are zwave curtains).

However, should the alarm be active, then the curtains invoke a false alarm trigger, hence the event to briefly unarm to allow the curtains to close without generating alarm.

From a security standpoint this can be a risk, but the time of not armed is only a few seconds.

If is_armed_partial (we are sleeping in the house), then daily routine does not run as then i prefer the curtains to stay closed until i disable the alarm.


```
security_system={               # advanced interface and definition of a security system, either stand alone or integrated as a master or slave subsystem 
    ...
    "daily_routine":        Virtual("app", value_logic={"is_armed_partial":True,"is_day":"True","is_not_day":"False"}, 
        things_app="unarm_briefly", # unarm briefly for the curtains not to trigger an alarm, in my setup this does not work if is_armed_partial (sleeping)
        properties={
			"vera_active":  {"txt":"vera_open_curtains"},   # open the curtains at sunrise, close at sunset but not if is_armed_partial (sleep mode)
			"vera_normal":  {"txt":"vera_close_curtains"}}),
	...
```

## Example of __sirens_test__

Here a sirens test event will happen every 1st day of new month at 12am.

<!--s_insert_{"tree":"(dk:hall.upstairs).*(o:Security)"}-->

from project.py tree:(dk:hall.upstairs).*(o:Security)
```python3
# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:hall.upstairs,o:Room,kw:contents,lp:0,o:Security>

from lucy_app import *

Security(fire_detectors = [Fire_detector(path = "unipi:PI-Light,input,3")],sirens = [Alarm_siren(
                copy_things = {
                        "carbon_copy":Output(path = "zw:Vera_plus,buttonset,173,Status1")},
                notifications = {
                        "app_done":Log(txt='Sirens testing completed', ceiling=None),
                        "app_start":Say(txt='{tts_start} beware, now follows a monthly sirens test, report urgently if it stays silent {tts_end}', ceiling=None, times=2, override=True, volume=35)},
                path = "unipi:PI-Light,relay,1",
                things_app = "sirens_test")],zone = "sleep")

```

<!--e_insert-->
