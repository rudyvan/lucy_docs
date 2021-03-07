
# Prj_Parser

## Summary

Prj_parser is the core app that processes myproject.py and validates class_doc.conf as a guide to python3 process the script objects and data that Lucy can use.

This translation is essential as Lucy cannot work from the objects files directly without validation of the entries.

How is the prj_parser routine invoked?

"Prj_parser app is executed by every smart thingscontroller when the boot program completes to prepares itself for the management of the things and apps entrusted.

Prj_parser starts by reading myproject.py to build a dictionary with all things_controllers and the role they will play in servicing that project.
Then myproject.py is evaluated as any regular python3 script while creating these all the dictionaries, lists and objects that it contains and validating every entry and field.

As in any regular python3 script comments can be added and python3 syntax rules must be obeyed.
 
During parsing many error messages could be displayed, more than 200 different exist at my last count, you find the list below.

But some other issues are syntax errors reported by the prj_parser interpreter.
Most often these are syntax issues, some end colon is forgotten or tabs are used instead of spaces.

There is also a thorough check on each field, what values are allowed, is it a string field, a list or even another object.
The latest typechecking features of python3.5 are implemented : https://docs.python.org/3/library/typing.html

And finally, every app is initialized and timers and counters are set, just for the specific things_controller that is started by site_tasker. 

Config parser also produces an extensive report, with much details presented in different groupings, see below for an example.
This report is threaded, as not to delay the commencement of the things_controller of the real work.

When prj_parser is run on a controller with the role deployer, then also all the documentation is updated, see further how this works.

## More on Prj_parser

One of the more complex features of this app is generating the data for things_sync to work and the drivers that are necessary for each things_controller to obtain or set things data.

For every things_controller a list is created with all the things that this controller needs to fulfill its role and how the value for every thing will be obtained or set.
This is not for every real thing such as a light, but also all the virtual things such as flags.

The creation of virtual things and the owner of each thing is another core feature.

As an example, for every room that prj_parser reads, it will create a room object, but it will add a lot of virtual things based on what is in the room defined:

| Thing in the Room | Virtual Thing added | What it does? |
| --- | --- | --- |
| Alarm_detector | room_name^secure | is the room armed? |
| Door/Window | room_name^locked  | is the room locked?
| clim_SP/clim_Dev | room_name^clim_on | is the room climatised?
| Sensor | room_name^ plus [pref,comfort_offset,economy_offset,temp_soll,temp_ok] | the climate settings for the room, all tracked by forensics

All these things have an owner and are wanted by some things_controller(s) and that is exactly what prj_parser does.

To improve security, prj_parser evaluates who should be talking to who to allow just those controllers to communicate and refuse any other communication attempts.
This is called ip_in_accept, the list of local ip's where commands or io data can come from, see [Things_sync](Things_sync.md).

You can find all this output in the above mentioned report.


## Thing Name Generation

The things defined in site.conf must each have an unique name.  When multiple things in a spot can be defined, one can use a list or a dictionary structure.

In a list structure, the names are generated automatically and are either "{room}_{repr}{seq}", "{rm_o_key}{seq}" or "{room}{rm_o_key}{seq}" for a multi app occurence.

In a directory structure, you define the name, and the parser will help you with keyword substitution:

| Keyword   | Replacement | 
 {room}     | name of the room in lower case room |
 {cnt}      | nothing if cnt is zero else "_{}" with cnt being the number of this generated object starting at zero
 {id}       | id is name of person or movable object
 {rm_o_key} | assignation label before the dictionary or the list
 {repr}     | lower case object name
 {seq}      | nothing if seq is zero else "_{}" with seq being the sequence number in the list (only list name generation)
 {opt}      | nothing if only one instance of this app is defined else "_{}" with the app sequence number

## Doc_Gen : updating documentation

The documentation is extensive and written in the github markup language style https://guides.github.com/features/mastering-markdown.

Prj_parser generates parts of this documentation using all the information that is available in app_obj.conf based on markers in the text files.

These markers are actually html comments between braces \<\!--xxx--\> with xxx and should be defined per pair, the starting marker prefixed with ```s_``` and the closing marker with ```e_```.
The following markers can be defined:

| Doc_Gen marker start | Doc_gen marker end | What it does |
| --- | --- | --- |
```s_toc_XXXX``` |  ```e_toc_XXX``` | inserts a table of content with XXXX one of [what_is,System_app, Driver, App, Base_Thing, Thing] |
```s_name``` |      ```e_name```    | name of the object
```s_role``` |      ```e_role```    | role of the object
```s_descr_o``` |   ```e_descr_o``` | adds a short description in the file of the object
```s_tbl``` |       ```e_tbl```		| adds tables :  1.the fields of the App or the Thing, 2.the list with properties, 3. the list with notifications, and 4. Errors and Warnings |
```s_sub_xxx``` |   ```e_sub_xxx```	| signals an extractable text between these to markers, see next row for how to do |
```s_insert_{"file_n":"docs/Path.md","path+":"docs/","sub":"xxx","level":+1}``` | ```e_insert``` | extracts the text from file_n between the markers (above row) and inserts it, adds (optional) a path and increases or decreases (optional) the heading level | 
```s_insert_{"file_n":"docs/Path.md","path+":"docs/"}``` | ```e_insert``` | inserts all of the file from file_n | 
```s_insert_{"role":"rrr","suffix":"sss"}``` | ```e_insert```  | insert a html file from the things_controller with role and suffix of the html file.  file not in \/docs, then is called in real time.  css data is stripped as markup does not like |
Example : ```s_insert_{"role":"deploy","suffix":"ref"}``` | ```e_insert``` | inserts or calls the file and then inserts PI_Deploy_ref.html | 
```s_insert_{"prj_parser":"c.conf","section":"s","var":"v"}``` | ```e_insert```  | insert a config element from the config file, section and var |
```s_insert_{"prj_parser":"c.conf","sections":["s1","s2"],"vars":["v1","v2"]}```  | ```e_insert```  | insert a config element from the conf file, any listed sections and any listed vars |
```s_insert_{"tree":["re"]}``` | ```e_insert```  | insert an element(s) from myproject.py file, through one or more regular expressions |
Example : ```s_insert_{"role":"deploy","suffix":"ref"}``` | ```e_insert``` | inserts or calls the file and then inserts PI_Deploy_ref.html | 
```s_insert_{"tree":["(dk:street).*(o:Mailbox_alert)","(dk:veranda).*(o:Sonos)"]}```  | ```e_insert```  | insert a mailbox alert object from the street and a sonos object from the veranda |

## Tex_Gen : generating PDF files

The output of doc_gen contains markers for the markup language to latex parser that is invoked with Tex_Gen.
Then any latex to pdf transformer such as Texmaker can be used to produce a few pdf files.

<!--s_tbl-->
## List of [properties](Properties.md) for __Prj_parser__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | notifications | ['prj_parser'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 

## List of [Notifications](Notifier.md) for  __Prj_parser__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | prj_parser | notification when Prj_parser completes | 

## List of [Errors/Warnings](Error_Warn.md) for  __Prj_parser__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_acc_cntrl | !!Access_point <{:}>/<{:}> not in {:} |  
  | err_acc_right | !!access_event <:>/<{:}> not in {:} |  
  | err_cam_type | !!Camera Type <{:}> not in <{:}> | every camera should have a cam_tpe that is defined in the camera_driver 
  | err_cfg_read | !!Config Read Error : <{:}> / <{:}> error :<{:}> |  
  | err_cls_doc | !!Class Docgen Error in {}: <{:}> |  
  | err_currency | !!Currency <{:}> should be like '€&euro;', 1 to 3 characters followed by that HTML currency symbol |  
  | err_deco_args | !!FATAL function args bad for <{:}> -> <{:}> |  
  | err_degrees | !!Degrees <{:}> should be °C or °F |  
  | err_doc_gen | !!Doc_gen {:} |  
  | err_doc_gen_cat | !!Doc_gen 'cat' issue with {:} / {:} not in {:} |  
  | err_doc_gen_sect | !!Doc_gen section/tree {:} in {:} not found in {:} |  
  | err_doc_gen_str | !!Doc_gen err/warn : key {:} missing in {:} |  
  | err_doc_gen_sub | !!Doc_gen sub {:} not found in file {:} |  
  | err_doc_gen_tree | !!Doc_gen tree elements <{:}> not found in tree |  
  | err_doc_gen_txt | !!Doc_gen items {:} missing in class_doc.conf ['CLASS'] |  
  | err_doc_gen_xxx | !!Doc_gen '{:}' file {:} ??, referred in {:} |  
  | err_door_method | !!Door <{:}> has {:} but not {:}? |  
  | err_duplicate | !!Duplicate <{:}>, name <{:}> | Twice the same object and name is only allowed for sensors 
  | err_el_list | !!Parsing {:}, not in {:} |  
  | err_email_psw | !!EMAIL addr and pasw retrieval failed from /etc/ssmtp/ssmtp.conf |  
  | err_feeder_sec | !!Feeder {:} and Security {:} <> ?? |  
  | err_flg_do_name | !!Error parsing virtual play '{:}' {:} |  
  | err_flg_owner | !!Virtual tc is undetermined for {:} with {:} |  
  | err_flg_smart | !!Virtual <{:}> has a non smart tc <{:}>, unable to control |  
  | err_guider | !!Parsing error in guider {:} |  
  | err_i_make | !!Clim_XX <{:}> in {:} has i_make {:} ? {:} |  
  | err_ip_addr | !!IP addr invalid: {:} for {:} |  
  | err_logic_ths | !!Logic Error, {:} not in ths dictionary |  
  | err_msg_dpl | !!notifier definition for msg_dpls contains non rasp :<{:}> |  
  | err_need_ones | !!prj_parser, missing {:} |  
  | err_no_owner | !!{:} need {:} but no owner defined |  
  | err_nty_drv | !!Notifications {:} exist, but {:} not |  
  | err_opt_mult | !!prj_parser, {:} only one allowed |  
  | err_ow_tpe | !!{:} ow thing type <{:}> not implemented |  
  | err_owner_ths_hw | !!{:} need {:} but owner {:} ths_hw? {:} |  
  | err_parse | !!Parse Error: <{:}> |  
  | err_path | !!path <{:}> error: {:} |  
  | err_path_all | !!<{}>, path <{}>: {} must be {} |  
  | err_path_any | !!<{}>, path <{}>: {} disallowed with {} |  
  | err_path_drv | !!<{}>, path <{}>, ?? driver {} |  
  | err_path_fmt_mis | !!<{}>, path <{}>: format <{}> mismatch |  
  | err_path_format | !!path parameter string mismatch <{}> for <{}> : {} <> {} |  
  | err_path_kw_mis | !!<{}>, path <{}>: has {} with {} not in {} |  
  | err_path_nr | !!<{}>, path <{}>, {} should be integer number |  
  | err_path_owner | !!<{}>, path <{}>, {} is not {} |  
  | err_path_tc | !!<{}>, path <{}>, ??tc <{}> |  
  | err_path_tc_many | !!cannot auto-fill tc name <{}> for <{}> in <{}> as multiple tc's exist |  
  | err_path_tc_none | !!cannot auto-fill tc name <{}> for <{}> in <{}> as not such tc is defined |  
  | err_path_tpe | !!<{}>, path <{}>: tpe {} not one of {} |  
  | err_path_usb | !!<{}>, path <{}>, <{}> not in usb_driver |  
  | err_pi_missing | !!FATAL {:} not in {:} defined |  
  | err_prs_nty_tts | !!For type {:}, message {:} not in app_data.conf |  
  | err_pulse_not | !!things_sync cannot cmd=pulse for {:} |  
  | err_rm_v_role | !!Parsing System Error, room_virtual role_me <{:}> not attributed |  
  | err_role_me | !!Parsing {:}, {:}, ?? tc name: {:} |  
  | err_room_name | !!Parsing {:}, room {:} not defined |  
  | err_say_make | !!Cannot make Say-{} with file: {}  |  
  | err_sensor_unknown | !!Sensor {:} unknown |  
  | err_short_name | !!Concept: short <{:}> is multiple {:}, {:} |  
  | err_sun_sr | !!Sun Set/Rise, invalid Site_setting: <{:}> |  
  | err_things_app | !!Things_app {:}?? for {:}? |  
  | err_ths_hw | !!ths_hw syntax : <{:}>, error:{:} |  
  | err_tpe_chk | !!<{:}> check failed: {:}/{:} has {:} not in {:} |  
  | err_usage_dict | !!Things_app thing usage {:} is missing Qty or Unit |  
  | err_value_logic | !!value_logic for <{:}> is not valid: {:} |  
  | err_vl_cal_kwargs | !! value_logic callable <{:}> has arguments <{:}> : {:} |  
  | err_vl_item | !! value_logic for {:} in {:}: {:} |  
  | err_where_keys | !!Parsing {:}, {:}, missing definitions: {:} |  
  | msg_delay_end | Delay {:} expired, now update(args={} and kwargs={}) |  
  | msg_delay_start | Delay {:} {:}s started with {:} |  
  | msg_docs_all | DOC_GEN:making {:} |  
  | msg_docs_gen | DOC_GEN:started |  
  | msg_docs_gen_new | DOC_GEN:app files -> {:} docs new/updated |  
  | msg_docs_new_toc | DOC_GEN:contents table = new |  
  | msg_docs_old_toc | DOC_GEN:contents table = unchanged |  
  | msg_duration_end | Duration {:} expired -> init of th |  
  | msg_duration_ext | Duration {:} expired -> duration restarted by extender {:} |  
  | msg_duration_restart | Duration {:} -> old {:} => new {:} |  
  | msg_duration_start | Duration {:} -> {:} |  
  | msg_path_new | New path found : <{:}>, paths_free is updated |  
  | msg_path_occupied | path <{:}> is now occupied by a thing and removed from paths_free list |  
  | msg_udp_tcp | notify {:} -> {:} |  
  | msg_vl_delay_can | value_logic -> delay <{:}> : {:} {:} cancelled |  
  | msg_vl_delay_xxx | value_logic -> delay <{:}> : {:} active {:} {:} secs countdown |  
  | msg_vl_list_xxx | value_logic -> update <{:}> : {:} now {:} {:} |  
  | msg_vl_payload_no | value_logic -> payload no for <{:}> : {:} |  
<!--e_tbl-->

* * *
* * *
# Parsing Reporting Example

Detailed device reporting is generated by every things_controller when site_tasker starts, but comes emailed from the things_controller with the role : 'deployer'.

* * *
* * *

<!--s_insert_{"role":"deploy","suffix":"ref"}-->


[imac-lucy_ref.html](imac-lucy_ref.html)
<!DOCTYPE html><html><body><h1>Report_ref -> imac-lucy_ref.html  2021/02/07 11:25:57</h1>

<!--e_insert-->

* * *
* * *

