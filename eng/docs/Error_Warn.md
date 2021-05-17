# Error and Warning Messages

## Summary

Almost all messages, errors and warnings are just an id with parameters passed through a specialised script to make a message.
A dictionary contains this list of id's with some properties.

These messages have to do with apps or things and they are grouped and listed in this documentation at the right subsection automatically by prj_parser.


One of the properties is more background information on the cause of the issue.
This description needs to be completed in the different user languages and the context description needs to be generated. 

The current list is attached:

<!--s_insert_{"prj_parser":"app_obj.conf","section":"TEXT"}-->

from app_obj.conf:
```python3
[TEXT]

err="!!
err_pref="!!"
msg_version={"txt":"!!{:}", "descr":"","cat":"Site_settings"}
err_parse={"txt":"!!Parse Error: <{:}>", "descr":"","cat":"Prj_parser"}
err_cls_doc={"txt":"!!Class Docgen Error in {}: <{:}>", "descr":"","cat":"Prj_parser"}
err_ow_tpe={"txt":"!!{:} ow thing type <{:}> not implemented", "descr":"","cat":"Prj_parser"}
err_sensor_unknown={"txt":"!!Sensor {:} unknown", "descr":"","cat":"Prj_parser"}
err_clim_s={"txt":"!!Climate_manager role_follow error <{:}> <{:}>", "descr":"","cat":"Climate_manager"}
err_sp_id={"txt":"!!Climate for room <{:}> contains a clim_target <{:}> not in {:}", "descr":"","cat":"Climate_manager"}
err_ip_spec={"txt":"!!{:} spec_func is <{:}> not in: [None, 'Master', 'Echo']", "descr":"","cat":"Climate_manager"}
err_mail_key={"txt":"!!Mail Notifs with <{:}> undefined {:}", "descr":"","cat":"Climate_manager"}
err_ip_missing={"txt":"!!ip of {:} missing", "descr":"","cat":"Climate_manager"}
err_soll_ip={"txt":"!!Soll from ip <plc_grp> {:} in {:} undefined", "descr":"","cat":"Climate_manager"}
err_weekday_miss={"txt":"!!Weekday {:} not defined in {:}", "descr":"","cat":"Climate_manager"}
err_no_setpoint={"txt":"!!Setpoint {:} in {:} for {:} missing", "descr":"","cat":"Climate_manager"}
err_soll_no_mode={"txt":"!!Soll {:} has no {:} for mode {:}", "descr":"","cat":"Climate_manager"}
err_soll_no_default={"txt":"!!Soll {:} no default on/off {:} for mode {:}", "descr":"","cat":"Climate_manager"}
err_soll_not_found={"txt":"!!Soll {:} {:} {:} not found", "descr":"","cat":"Climate_manager"}
err_soll_no_time={"txt":"!!Soll {:} no time/value pair {:}", "descr":"","cat":"Climate_manager"}
err_unipi_wrong={"txt":"!!{:} attached to {:} not {:}", "descr":"","cat":"Climate_manager"}
err_type_wrong={"txt":"!!{:},type={:} not={:} as in conf", "descr":"","cat":"Climate_manager"}
err_owdevice_unknown={"txt":"!!{:} Unknown in {:}", "descr":"","cat":"Climate_manager"}
err_room_temp={"txt":"!!Room {:} sensor now below {:} °C limit with {:+06.2f} °C", "descr":"","cat":"Climate_manager"}
err_mkr_defect={"txt":"!!{:} in {:} is defect? {:>05.2f}-{:>05.2f} < {:>05.2f}", "descr":"","cat":"Climate_manager"}
err_clim_cntrl={"txt":"!!Climate for <{:}> with <{:}> verify <{:}>", "descr":"","cat":"Climate_manager"}
err_cool_heat={"txt":"!!Climatisation conf error, temp cool {:} - temp heat {:} must be > 1 °C", "descr":"","cat":"Climate_manager"}
err_attr_type={"txt":"!!Parse of {:} in {:} <{:}>", "descr":"","cat":"Climate_manager"}
msg_room_low={"txt":"Room {:} now below {:}", "descr":"","cat":"Climate_manager"}
msg_plc_now={"txt":"Room {:} now close to {:}", "descr":"","cat":"Climate_manager"}
msg_pump_act_run={"txt":"Heating Pump <{:}> Activation Run", "descr":"","cat":"Climate_manager"}
msg_mkr_working={"txt":"{:} in {:} is working {:>05.2f}-{:>05.2f} > {:>05.2f}", "descr":"","cat":"Climate_manager"}
msg_mkr_activation={"txt":"{:} {:}/{:} {:} Activation {:} mins", "descr":"","cat":"Climate_manager"}
msg_temp_config={"txt":"Temperature Config Reloaded", "descr":"","cat":"Climate_manager"}
msg_room_not_locked={"txt":"Room {:} not locked", "descr":"","cat":"Climate_manager"}
msg_room_locked={"txt":"Room {:} now locked", "descr":"","cat":"Climate_manager"}
msg_clim_nty={"txt":"Climate Slave notification skipped {:}", "descr":"","cat":"Climate_manager"}
err_clim_pr_member={"txt":"!!Transport <{}> has invalid member_of: {}, should be one of {}", "descr":"","cat":"Climate_manager"}
err_clim_mk_must={"txt":"!!Maker <{}> should be member_of transport: {}", "descr":"","cat":"Climate_manager"}
err_clim_mk_make={"txt":"!!Maker <{}> makes {}, but production can only make: {}", "descr":"","cat":"Climate_manager"}
err_clim_tr_member={"txt":"!!Maker <{}> has invalid member_of: {}, should be one of {}", "descr":"","cat":"Climate_manager"}
err_item_cumul={"txt":"!!{:} ?tc for cumul request", "descr":"","cat":"Forensics"}
msg_cum_flip={"txt":"Cumuls {:}", "descr":"","cat":"Forensics"}
msg_cum_new_day_done={"txt":"Cumul New Day resets of all tcs is completed", "descr":"","cat":"Forensics"}
err_cum_reply={"txt":"!!{:} replied for {:}?? with cumul {:}", "descr":"","cat":"Forensics"}
err_cum_req={"txt":"!!{:} wanted cumul {:}??", "descr":"","cat":"Forensics"}
err_cumul={"txt":"!!Cumul internal error for <{:}> with {:} not in {:}", "descr":"","cat":"Forensics"}
err_cum_owner={"txt":"!!Cumul request failed, no tc for <{:}>", "descr":"","cat":"Forensics"}
msg_cum_self={"txt":"cum <{:}> i have myself", "descr":"","cat":"Forensics"}
msg_cum_request={"txt":"cum <{:}> requested from {:}/{:}", "descr":"","cat":"Forensics"}
msg_cum_reply={"txt":"cum <{:}> reply from {:}/{:}", "descr":"","cat":"Forensics"}
err_forensic_sz={"txt":"!!Forensics database <{:}> size={:}, reduced to {:}", "descr":"","cat":"Forensics"}
err_deco_args={"txt":"!!FATAL function args bad for <{:}> -> <{:}>", "descr":"","cat":"Prj_parser"}
err_pi_missing={"txt":"!!FATAL {:} not in {:} defined", "descr":"","cat":"Prj_parser"}
err_hw_gws={"txt":"!!hw_gws syntax : <{:}>, error:{:}", "descr":"","cat":"Prj_parser"}
err_logic_ths={"txt":"!!Logic Error, {:} not in ths dictionary", "descr":"","cat":"Prj_parser"}
err_no_owner={"txt":"!!{:} need {:} but no owner defined", "descr":"","cat":"Prj_parser"}
err_owner_hw_gws={"txt":"!!{:} need {:} but owner {:} hw_gws? {:}", "descr":"","cat":"Prj_parser"}
err_where_keys={"txt":"!!Parsing {:}, {:}, missing definitions: {:}", "descr":"","cat":"Prj_parser"}
err_role_me={"txt":"!!Parsing {:}, {:}, ?? tc name: {:}", "descr":"","cat":"Prj_parser"}
err_room_name={"txt":"!!Parsing {:}, room {:} not defined", "descr":"","cat":"Prj_parser"}
err_el_list={"txt":"!!Parsing {:}, not in {:}", "descr":"","cat":"Prj_parser"}
err_rm_v_role={"txt":"!!Parsing System Error, room_virtual role_me <{:}> not attributed", "descr":"","cat":"Prj_parser"}
err_guider={"txt":"!!Parsing error in guider {:}", "descr":"","cat":"Prj_parser"}
err_flg_do_name={"txt":"!!Error parsing virtual play '{:}' {:}", "descr":"","cat":"Prj_parser"}
err_flg_owner={"txt":"!!Virtual tc is undetermined for {:} with {:}", "descr":"","cat":"Prj_parser"}
err_flg_smart={"txt":"!!Virtual <{:}> has a non smart tc <{:}>, unable to control", "descr":"","cat":"Prj_parser"}
err_prs_nty_tts={"txt":"!!For type {:}, message {:} not in app_data.conf", "descr":"","cat":"Prj_parser"}
err_i_make={"txt":"!!Clim_XX <{:}> in {:} has i_make {:} ? {:}", "descr":"","cat":"Prj_parser"}
err_tpe_chk={"txt":"!!<{:}> check failed: {:}/{:} has {:} not in {:}", "descr":"","cat":"Prj_parser"}
msg_duration_start={"txt":"Duration {:} -> {:}", "descr":"","cat":"Prj_parser"}
msg_duration_restart={"txt":"Duration {:} -> old {:} => new {:}", "descr":"","cat":"Prj_parser"}
msg_duration_end={"txt":"Duration {:} expired -> init of th", "descr":"","cat":"Prj_parser"}
msg_duration_ext={"txt":"Duration {:} expired -> duration restarted by extender {:}", "descr":"","cat":"Prj_parser"}
msg_delay_start={"txt":"Delay {:} {:}s started with {:}", "descr":"","cat":"Prj_parser"}
msg_delay_end={"txt":"Delay {:} expired, now update(args={} and kwargs={})", "descr":"","cat":"Prj_parser"}
err_path={"txt":"!!path <{:}> error: {:}", "descr":"","cat":"Prj_parser"}
err_path_tpe={"txt":"!!<{}>, path <{}>: tpe {} not one of {}", "descr":"","cat":"Prj_parser"}
err_path_tc_none={"txt":"!!cannot auto-fill tc name <{}> for <{}> in <{}> as not such tc is defined", "descr":"","cat":"Prj_parser"}
err_path_tc_many={"txt":"!!cannot auto-fill tc name <{}> for <{}> in <{}> as multiple tc's exist", "descr":"","cat":"Prj_parser"}
err_path_format={"txt":"!!path parameter string mismatch <{}> for <{}> : {} <> {}", "descr":"","cat":"Prj_parser"}
err_path_fmt_mis={"txt":"!!<{}>, path <{}>: format <{}> mismatch", "descr":"","cat":"Prj_parser"}
err_path_kw_mis={"txt":"!!<{}>, path <{}>: has {} with {} not in {}", "descr":"","cat":"Prj_parser"}
err_path_any={"txt":"!!<{}>, path <{}>: {} disallowed with {}", "descr":"","cat":"Prj_parser"}
err_path_all={"txt":"!!<{}>, path <{}>: {} must be {}", "descr":"","cat":"Prj_parser"}
err_path_drv={"txt":"!!<{}>, path <{}>, ?? driver {}", "descr":"","cat":"Prj_parser"}
err_path_tc={"txt":"!!<{}>, path <{}>, ?? tc <{}>", "descr":"","cat":"Prj_parser"}
err_path_owner={"txt":"!!<{}>, path <{}>, {} is not {}", "descr":"","cat":"Prj_parser"}
err_path_nr={"txt":"!!<{}>, path <{}>, {} should be integer number", "descr":"","cat":"Prj_parser"}
err_path_usb={"txt":"!!<{}>, path <{}>, <{}> not in usb_driver", "descr":"","cat":"Prj_parser"}
err_path_gw={"txt":"!!gateway? <{}>, available = <{}>", "descr":"","cat":"Prj_parser"}
msg_path_occupied={"txt":"path <{:}> is now occupied by a thing and removed from paths_free list", "descr":"","cat":"Prj_parser"}
msg_path_new={"txt":"New path found : <{:}>, paths_free is updated", "descr":"","cat":"Prj_parser"}
err_pulse_not={"txt":"!!things_sync cannot cmd=pulse for {:}", "descr":"","cat":"Prj_parser"}
err_meter_pulse={"txt":"!!{:} has no pulse_qty, {:}, ?? missing ean path type??", "descr":"","cat":"Prj_parser"}
err_nty_cond={"txt":"!!System Error in Conditional Notification: {:}", "descr":"","cat":"Prj_parser"}
err_ip_addr={"txt":"!!IP addr invalid: {:} for {:}", "descr":"","cat":"Prj_parser"}
err_currency={"txt":"!!Currency <{:}> should be like '€&euro;', 1 to 3 characters followed by that HTML currency symbol", "descr":"","cat":"Prj_parser"}
err_degrees={"txt":"!!Degrees <{:}> should be °C or °F", "descr":"","cat":"Prj_parser"}
err_sun_sr={"txt":"!!Sun Set/Rise, invalid Site_setting: <{:}>", "descr":"","cat":"Prj_parser"}
msg_udp_tcp={"txt":"notify {:} -> {:}", "descr":"","cat":"Prj_parser"}
err_msg_dpl={"txt":"!!notifier definition for msg_dpls contains non rasp :<{:}>", "descr":"","cat":"Prj_parser"}
err_acc_cntrl={"txt":"!!Access_point <{:}>/<{:}> not in {:}", "descr":"","cat":"Prj_parser"}
err_acc_right={"txt":"!!access_event <:>/<{:}> not in {:}", "descr":"","cat":"Prj_parser"}
err_door_method={"txt":"!!Door <{:}> has {:} but not {:}?", "descr":"","cat":"Prj_parser"}
err_opt_mult={"txt":"!!prj_parser, {:} only one allowed", "descr":"","cat":"Prj_parser"}
err_need_ones={"txt":"!!prj_parser, missing {:}", "descr":"","cat":"Prj_parser"}
err_short_name={"txt":"!!Concept: short <{:}> is multiple {:}, {:}", "descr":"","cat":"Prj_parser"}
err_nty_drv={"txt":"!!Notifications {:} exist, but {:} not", "descr":"","cat":"Prj_parser"}
err_things_app={"txt":"!!Things_app {:}?? for {:}?", "descr":"","cat":"Prj_parser"}
err_feeder_sec={"txt":"!!Feeder {:} and Security {:} <> ??", "descr":"","cat":"Prj_parser"}
err_usage_dict={"txt":"!!Things_app thing usage {:} is missing Qty or Unit", "descr":"","cat":"Prj_parser"}
err_duplicate={"txt":"!!Duplicate <{:}>, name <{:}>", "descr":"Twice the same object and name is only allowed for sensors","cat":"Prj_parser"}
err_say_make={"txt":"!!Cannot make Say-{} with file: {} ", "descr":"","cat":"Prj_parser"}
err_scalar_format={"txt":"!!Scalar Format <{}> scalar={}", "descr":"","cat":"Prj_parser"}
err_scalar_range={"txt":"!!Scalar Out of Bounds <{}> with {} and scalar={}", "descr":"","cat":"Prj_parser"}
err_render_do={"txt":"!!Error in rendering table_do in <{:}> : {:} {:} {:}", "descr":"","cat":"Things_additions"}
err_render_report={"txt":"!!render name {:} not in [REPORT] section of app_obj.conf, called from {:}", "descr":"","cat":"Things_additions"}
err_render_gen_prg={"txt":"!!render {:}, generator {:} is not defined in dir() : {:}", "descr":"","cat":"Things_additions"}
err_render_cols_len={"txt":"!!render {:}, generator {:}, has t={:} and not matches {:} header strings", "descr":"","cat":"Things_additions"}
err_render_logic={"txt":"!!render {:}, generator?? {:} <> {:}", "descr":"","cat":"Things_additions"}
msg_render_not={"txt":"rendering {:} canceled by if: {:}", "descr":"","cat":"Things_additions"}
err_logic={"txt":"!!Logic Error in {:}: {:}<>{:}", "descr":"","cat":"Things_additions"}
err_decode={"txt":"!!unipi Decode, ?device? {:}", "descr":"","cat":"Things_additions"}
err_repr_len={"txt":"!!decorator repr len is zero", "descr":"","cat":"Things_additions"}
err_am_i_get_my={"txt":"!!am_i_get_my error, in th {:}, <{:}> is not in {:}", "descr":"","cat":"Things_additions"}
err_mk_me={"txt":"!!mk_me error, in th {:}, <{:}> ? {:}", "descr":"","cat":"Things_additions"}
err_pickle_load={"txt":"!!pickle file reloading of <{:}> failed {:}", "descr":"","cat":"Things_additions"}
err_eds_ow={"txt":"!!Processing eds_ow error = {:} on {:}", "descr":"","cat":"Things_additions"}
err_renson={"txt":"!!Processing Renson error = {:} on {:}", "descr":"","cat":"Things_additions"}
err_unipi_nok={"txt":"!!unipi {:} {:} -> {:}/{:} {:}", "descr":"","cat":"Things_additions"}
err_upd={"txt":"!!update of {:} with {:} failed", "descr":"","cat":"Things_additions"}
err_cmd_not_cal={"txt":"!!Feeder Cmd <{:}> not callable, {:}", "descr":"","cat":"Feeder"}
err_collect_report={"txt":"!!Feeder Collect Report Cmd <{:}> not callable, {:}", "descr":"","cat":"Feeder"}
err_cmd_args={"txt":"!!IP command {:}, from {:}, callability issue {:}, args={:}, kwargs={:}, error={:}", "descr":"","cat":"Things_sync"}
err_usb_port_ok={"txt":"!!usb port ok again {:}/{:} -> {:}", "descr":"","cat":"Usb_driver"}
err_usb_port_fail={"txt":"!!usb error port {:}/{:} port? {:}", "descr":"","cat":"Usb_driver"}
err_usb_scan_th={"txt":"!!usb error scan, ?thing {:}/{:} fail {:}", "descr":"","cat":"Usb_driver"}
err_usb_scan_decode={"txt":"!!usb error scan decode {:}/{:} fail {:}", "descr":"","cat":"Usb_driver"}
warn_notify_expired={"txt":"!Reply? {:} -> {:}", "descr":"","cat":"Things_sync"}
err_ip_in_req={"txt":"!!message type error, requester={:} with <{:}> {:}", "descr":"","cat":"Things_sync"}
err_ip_in_json_req={"txt":"!!json.loads error, requester={:} with {:} {:}", "descr":"","cat":"Things_sync"}
err_ip_in_cmd={"txt":"!!IP {:} not valid cmd, requester={:} with {:}", "descr":"","cat":"Things_sync"}
err_ip_in_io={"txt":"!!IP {:} not thing name, requester={:} with {:}", "descr":"","cat":"Things_sync"}
err_ip_in_ths_i_use={"txt":"!!IP {:} not ths_i_use for me, requester={:} with {:}", "descr":"","cat":"Things_sync"}
err_ip_in_refused={"txt":"!!IP from {:} with {:} refused", "descr":"","cat":"Things_sync"}
err_ip_in_val={"txt":"!!IP from {:} for {:} with {:} is invalid value", "descr":"","cat":"Things_sync"}
msg_nty_ignored={"txt":"nty_{:} ignored due per APP <{:}> instruction", "descr":"","cat":"Notifier"}
msg_nty_ceiling={"txt":"nty_{:} ignored due ceiling instruction", "descr":"","cat":"Notifier"}
err_nty_obj={"txt":"!!Notifier {:}, <{:}>??, {:}", "descr":"","cat":"Notifier"}
err_do_nty={"txt":"!!Notification Issue {:} {:} {:}", "descr":"","cat":"Notifier"}
msg_cam_dt_ok={"txt":"{:} DT set->OK", "descr":"","cat":"Camera"}
err_cam_dt_nok={"txt":"!!{:} url: {:} DT NOK", "descr":"","cat":"Camera"}
err_cam_url={"txt":"!!CAM {:} urlopen issue={:}, error={:}", "descr":"","cat":"Camera"}
msg_cams_updated={"txt":"all camera's updated", "descr":"","cat":"Camera"}
err_email_file={"txt":"!!Email File issue {:}{:}, error={:}", "descr":"","cat":"Notifier"}
err_file_gmail={"txt":"!!Email Attachment {:} (needed-{:}MB > avail-{:}MB) -> skipped", "descr":"","cat":"Notifier"}
err_cam_failure={"txt":"!!Camera Failure {:}", "descr":"","cat":"Notifier"}
err_cam_nok={"txt":"!!Camera Pict {:} -> {:}/{:} {:}", "descr":"","cat":"Notifier"}
err_cam_type={"txt":"!!Camera Type <{:}> not in <{:}>", "descr":"every camera should have a cam_tpe that is defined in the camera_driver","cat":"Prj_parser"}
err_email_fail={"txt":"!!Email Failure - {:} - {:}", "descr":"","cat":"Notifier"}
msg_vera_cmd={"txt":"Vera cmd <{:}>...", "descr":"","cat":"Vera_driver"}
err_vera_cms={"txt":"!!Vera cmd Unknown <{:}>", "descr":"","cat":"Vera_driver"}
err_vera_fail={"txt":"!!Vera cmd Failure <{:}> {:} {:}", "descr":"","cat":"Vera_driver"}
err_vera_input={"txt":"!!Vera luup/cmds in obj/main failed <{:}>", "descr":"","cat":"Vera_driver"}
err_vera_pars={"txt":"!!Alexa {:} command for Vera {:} = {:}, does not exist", "descr":"","cat":"Vera_driver"}
err_zw_path={"txt":"!!zw path error {:}: {:}", "descr":"","cat":"Vera_driver"}
err_vera_path={"txt":"!!vera path error {:}: {:}", "descr":"","cat":"Vera_driver"}
err_vera_scene={"txt":"!!vera value_logic error for <{:}> in {:}, error = {:}", "descr":"","cat":"Vera_driver"}
err_vera_devnr={"txt":"!!vera device_nr=<{:}> dissapeared -> name={:}", "descr":"","cat":"Vera_driver"}
msg_hue_link={"txt":"<{:}>: Press link button for pairing", "descr":"","cat":"Hue_driver"}
msg_hue_username={"txt":"<{:}>: Paired as username <{:}>", "descr":"","cat":"Hue_driver"}
msg_hue_white={"txt":"<{:}> updated, <{:}> deleted as redundant", "descr":"","cat":"Hue_driver"}
msg_hue_refreshed={"txt":"<{:}> config refreshed", "descr":"","cat":"Hue_driver"}
msg_hue_request={"txt":"<{:}>: {:}", "descr":"","cat":"Hue_driver"}
err_hue_white={"txt":"!!<{:}>, <{:}> update failed <{:}>", "descr":"","cat":"Hue_driver"}
err_hue_link={"txt":"!!<{:}>: error {:}", "descr":"","cat":"Hue_driver"}
err_hue_fail={"txt":"!!hue cmd Failure <{:}> {:}", "descr":"","cat":"Hue_driver"}
err_hue_path={"txt":"!!hue path error {:}: {:}", "descr":"","cat":"Hue_driver"}
err_hue_io2id={"txt":"!!hue {:} name2id failure for {:}", "descr":"","cat":"Hue_driver"}
err_hue_write={"txt":"!!hue {:} write failure for path {:} -> {:}", "descr":"","cat":"Hue_driver"}
err_hue_scene={"txt":"!!hue {:} scene failure for path {:} scene {:} -> {:}", "descr":"","cat":"Hue_driver"}
err_hue_set={"txt":"!!hue {:} set_it failure for path {:} -> {:}", "descr":"","cat":"Hue_driver"}
err_hue_sensor={"txt":"!!hue {:} sensor read {:} not in {:} rcvd {:}", "descr":"","cat":"Hue_driver"}
err_hue_scene_nf={"txt":"!!hue {:} scene <{:}> not found for {:}/{:}", "descr":"","cat":"Feeder"}
warn_hue_scene={"txt":"!hue {:} scene <{:}> not standard for {:} in {:}", "descr":"","cat":"Feeder"}
err_gas_kw={"txt":"!!Google/Apple Siri keyword {:} for {:} not found in Hue", "descr":"","cat":"My_assistant"}
msg_ikea_refreshed={"txt":"Ikea Gateway <{:}> config refreshed", "descr":"","cat":"Ikea_driver"}
msg_ikea_rebooted={"txt":"Ikea Gateway <{:}> rebooted, result {:}", "descr":"","cat":"Ikea_driver"}
err_ikea_light_c={"txt":"!!ikea dev <{:}> no light control", "descr":"","cat":"Ikea_driver"}
err_alexa_parsing={"txt":"!!Alexa parsing {:} - {:}", "descr":"","cat":"Feeder"}
err_socket_creat={"txt":"!!{:} Socket Create/Bind Failed", "descr":"","cat":"Udp_driver"}
err_send_failed={"txt":"!!{:} Send FAILED {:} to {:} {:} for {:}", "descr":"","cat":"Udp_driver"}
err_dropbox={"txt":"!!Dropbox: {:} upload failed, {:} -> {:}", "descr":"","cat":"Udp_driver"}
msg_dropbox={"txt":"Dropbox: processed {:}", "descr":"","cat":"Udp_driver"}
msg_rcv_file_done={"txt":"{:} received", "descr":"","cat":"Deployer"}
msg_cpy_file_done={"txt":"{:} copy and overwrite completed", "descr":"","cat":"Deployer"}
err_cpy_overwrite={"txt":"!!upload overwrite for {:} not found @{:}", "descr":"","cat":"Deployer"}
err_no_deploy={"txt":"!!deployer is not defined", "descr":"","cat":"Deployer"}
err_show_data={"txt":"!!show txt split fail 'date time tc_n:' not in {:} {:}", "descr":"","cat":"Notifier"}
err_show_who={"txt":"!!show message, who is {:}?? {:}", "descr":"","cat":"Notifier"}
err_show_mismatch={"txt":"!!show message, who<>ip mismatch {:} <> {:} in {:}", "descr":"","cat":"Notifier"}
err_ws_forecast={"txt":"!!Weather forecast plugin missing", "descr":"","cat":"Weather_station"}
err_accu_weather={"txt":"!!Weather forecast update accu_weather fail <{:}>", "descr":"","cat":"Weather_station"}
err_wunderground={"txt":"!!Weather forecast update wunderground fail <{:}>", "descr":"","cat":"Weather_station"}
err_fc_p0={"txt":"!!Weather forecast period 0 missing", "descr":"","cat":"Weather_station"}
err_na_station={"txt":"!!Netatmo {:} ws, {:}", "descr":"","cat":"Weather_station"}
err_na_mail_id={"txt":"!!Netatmo mail id unmatch {:} <> {:}", "descr":"","cat":"Weather_station"}
err_na_home_id={"txt":"!!Netatmo Home id is not available", "descr":"","cat":"Weather_station"}
err_na_tags={"txt":"!!Netatmo Tags def mismatch: {:}", "descr":"","cat":"Weather_station"}
err_na_ws_data={"txt":"!!No Netatmo weather station available", "descr":"","cat":"Weather_station"}
err_na_ws_wind={"txt":"!!Netatmo wind types supported are only km/h or beaufort, not {:} (1 is mph, 2 is ms, 4 is knot)", "descr":"","cat":"Weather_station"}
msg_na_token={"txt":"Netatmo Token valid till {:}", "descr":"","cat":"Weather_station"}
err_requests_fail={"txt":"!!http-{:}({:}) failure: {:}", "descr":"","cat":"Weather_station"}
msg_ws_temp={"txt":"-> {:}°C", "descr":"","cat":"Weather_station"}
msg_dw_was_closed={"txt":"{:} was closed, command ignored", "descr":"","cat":"Door"}
msg_dw_was_open={"txt":"{:} was open, command ignored", "descr":"","cat":"Door"}
msg_dw_check_cmd={"txt":"!MSG {:} got {:} cmd, {:} secs ago but now still {:} -> cmd repeated", "descr":"","cat":"Door"}
msg_dw_keep={"txt":"!MSG {:} got pulse2{:} cmd, but keep_{:} is active", "descr":"","cat":"Door"}
msg_upl_done={"txt":"Upload tc's completed", "descr":"","cat":"Deployer"}
err_upl_done={"txt":"!!Upload tc's completed, missing <{:}>", "descr":"","cat":"Deployer"}
msg_upl_started={"txt":"Upload all tc's Started", "descr":"","cat":"Deployer"}
msg_upl_ordered={"txt":"Reload ordered to {:}", "descr":"","cat":"Deployer"}
msg_cmd_reload={"txt":"CMD:Reload", "descr":"","cat":"Deployer"}
msg_cmd_for={"txt":"CMD: {:} for {:}", "descr":"","cat":"Deployer"}
err_reload_files={"txt":"!!Error reloading downloaded files", "descr":"","cat":"Deployer"}
msg_virtual_play={"txt":"PLAY '{}' on '{}' with '{}' --> {}", "descr":"","cat":"Virtual"}
event_unarm_brief={"txt":"Scene trigger: unarm briefly for {:}", "descr":"","cat":"Things_additions"}
event_arm_brief={"txt":"Scene trigger: arm after briefly unarm", "descr":"","cat":"Things_additions"}
event_unarm_brief_no={"txt":"Scene trigger: unarm briefly for {:} not needed", "descr":"","cat":"Things_additions"}
err_event_pars={"txt":"!!Scene Error: {:}", "descr":"","cat":"Things_additions"}
msg_th_run={"txt":"APP {:}.{:}", "descr":"","cat":"Notifier"}
msg_th_method={"txt":"METH {:}.{:}", "descr":"","cat":"Notifier"}
msg_th_upd={"txt":"UPD {:}", "descr":"","cat":"Notifier"}
msg_th_set={"txt":"SET {:} {:}", "descr":"","cat":"Notifier"}
msg_log_subj={"txt":"Log File {:}", "descr":"","cat":"Log_driver"}
msg_log_err={"txt":" with {:} Errors", "descr":"","cat":"Log_driver"}
msg_new_log={"txt":"New Log Started", "descr":"","cat":"Log_driver"}
err_log_not={"txt":"!!log email nok, log not erased:{:}", "descr":"","cat":"Log_driver"}
err_color={"txt":"!!color {:} not recognised", "descr":"","cat":"Log_driver"}
err_run_loop={"txt":"!!Main Task(s) {:}", "descr":"","cat":"Deployer"}
err_task_repeat={"txt":"!!Task {:} not done and re-asked", "descr":"","cat":"Deployer"}
err_tim_task={"txt":"!!TimerTask {:} returned exception: {:}", "descr":"","cat":"Deployer"}
err_timer_bug={"txt":"!!Timer {:} has {:}", "descr":"","cat":"Deployer"}
warn_timer_overrun={"txt":"!Timer {:} has {:}", "descr":"","cat":"Deployer"}
err_timer_gone={"txt":"!!Timer {:} unexpectedly not there", "descr":"","cat":"Deployer"}
warn_timer_start={"txt":"!Bounce Timer <{:}> started as output found active without timer - {:}", "descr":"a bad fixup","cat":"Deployer"}
err_sync_call={"txt":"!!wait_for func {} in {} not callable", "descr":"","cat":"Deployer"}
warn_IP_NOK={"txt":"!IP ping for {:}/{:} Failed", "descr":"","cat":"Network_controller"}
msg_IP_OK={"txt":"IP ping success for {:}/{:} -> {:} sec", "descr":"","cat":"Network_controller"}
err_internet_lost={"txt":"!!Internet access failure!!", "descr":"","cat":"Network_controller"}
msg_internet_there={"txt":"Internet access restored!", "descr":"","cat":"Network_controller"}
irr_pump_act_run={"txt":"Irr Activ Pump Run {:} secs", "descr":"","cat":"Irrigation_manager"}
irr_run_depressure={"txt":"Irr Depressurising {:} secs/channel", "descr":"","cat":"Irrigation_manager"}
irr_run_depr_exist={"txt":"!!Irr Depressure is running, action prohibited", "descr":"","cat":"Irrigation_manager"}
irr_time_base={"txt":"!!Irrigation time base {:} : invalid", "descr":"","cat":"Irrigation_manager"}
irr_app_txt={"txt":"{:} with default {:} min/chan", "descr":"","cat":"Irrigation_manager"}
err_email_psw={"txt":"!!EMAIL addr and pasw retrieval failed from /etc/ssmtp/ssmtp.conf", "descr":"","cat":"Prj_parser"}
err_cfg_read={"txt":"!!Config Read Error : <{:}> / <{:}> error :<{:}>", "descr":"","cat":"Prj_parser"}
err_mnt_failed={"txt":"!!Share Mount Failed for {:}", "descr":"","cat":"Dropbox_driver"}
err_soco={"txt":"!!SoCo is not imported, please do : sudo pip3 install soco", "descr":"","cat":"Sonos_driver"}
err_tts_invalid={"txt":"!!TTS item is not defined in conf: {:}", "descr":"","cat":"Sonos_driver"}
err_sonos_req={"txt":"!!Sonos Req <{:}> ({:}) for {:} not found", "descr":"","cat":"Sonos_driver"}
err_sonos={"txt":"!!Sonos TTS Crash {:}", "descr":"","cat":"Sonos_driver"}
err_sonos_task={"txt":"!!Sonos Task {:}", "descr":"","cat":"Sonos_driver"}
war_tts_room={"txt":"! room {:} not found in Sonos zones {:}", "descr":"","cat":"Sonos_driver"}
msg_tts_play={"txt":"TTS request of {:}", "descr":"","cat":"Sonos_driver"}
msg_sonos_req={"txt":"Sonos Req <{:}> ({:}) for {:}", "descr":"","cat":"Sonos_driver"}
msg_sonos_skip={"txt":"Sonos Skipped <{:}> ({:})", "descr":"","cat":"Sonos_driver"}
msg_sonos_queue={"txt":"Sonos Queue Retrieved: {:}", "descr":"","cat":"Sonos_driver"}
msg_tts_off={"txt":"TTS item ignored due to voice is off {:}", "descr":"","cat":"Sonos_driver"}
msg_tts_played={"txt":"TTS item played : {:}", "descr":"","cat":"Sonos_driver"}
msg_tts_override={"txt":"TTS <{:}> has No Matter What", "descr":"","cat":"Sonos_driver"}
msg_sonos_room={"txt":"TTS room <{:}> -> <{:}>, play {:} l={:} s={:}s, t={:}", "descr":"","cat":"Sonos_driver"}
msg_sonos={"txt":"TTS play <{:}> l={:} s={:}s, t={:}", "descr":"","cat":"Sonos_driver"}
msg_sonos_env={"txt":"SONOS {:}", "descr":"","cat":"Sonos_driver"}
msg_tts_notif={"txt":"SAY nty added :{:} -> {:} {:} times, {:} utterance", "descr":"","cat":"Sonos_driver"}
msg_papirus={"txt":"papirus screen -> {:} from {:}", "descr":"","cat":"Notifier"}
msg_dpl={"txt":"msg screen -> {:} from {:}", "descr":"","cat":"Notifier"}
msg_sun={"txt":"sun rises at {:} and sets at {:}", "descr":"","cat":"Things_additions"}
err_value_logic={"txt":"!!value_logic for <{:}> is not valid: {:}", "descr":"","cat":"Prj_parser"}
err_vl_item={"txt":"!! value_logic for {:} in {:}: {:}", "descr":"","cat":"Prj_parser"}
err_vl_cal_kwargs={"txt":"!! value_logic callable <{:}> has arguments <{:}> : {:}", "descr":"","cat":"Prj_parser"}
msg_vl_payload_no={"txt":"value_logic -> payload no for <{:}> : {:}", "descr":"","cat":"Prj_parser"}
msg_vl_list_xxx={"txt":"value_logic -> update <{:}> : {:} now {:} {:}", "descr":"","cat":"Prj_parser"}
msg_vl_delay_xxx={"txt":"value_logic -> delay <{:}> : {:} active {:} {:} secs countdown", "descr":"","cat":"Prj_parser"}
msg_vl_delay_can={"txt":"value_logic -> delay <{:}> : {:} {:} cancelled", "descr":"","cat":"Prj_parser"}
msg_si_type={"txt":"SecInt System Type is <{:}>", "descr":"","cat":"Security_system"}
warn_si_missing={"txt":"!SecInt Definitions: if <{:}>, also <{:}> should exist", "descr":"","cat":"Security_system"}
err_safe_ways={"txt":"!!SecInt safe_ways <{:}> should be [exit_way, entry_way, sleep_way]", "descr":"","cat":"Security_system"}
err_safe_items={"txt":"!!SecInt safe_ways undefined item(s) <{:}>", "descr":"","cat":"Security_system"}
err_zones={"txt":"!!SecInt zones <{:}> should be [ignore_zones, always_zones, partial_zones]", "descr":"","cat":"Security_system"}
err_zone_items={"txt":"!!SecInt zones undefined item(s) <{:}>", "descr":"","cat":"Security_system"}
err_zone_access={"txt":"!!Door/Window <{:}> zones <{:}> undefined zone <{:}>", "descr":"","cat":"Security_system"}
msg_alarm_eminent={"txt":"{:} opened in sleep_way, alarm_delay {:}s started", "descr":"","cat":"Security_system"}
msg_alarm_by_eminent={"txt":"Alarm delay {:} secs expired, {:}", "descr":"","cat":"Security_system"}
msg_spec_alarm={"txt":"!alarm type={:}, {:} opened/closed", "descr":"","cat":"Security_system"}
msg_now_armed={"txt":"as {:} is closed, security is now armed", "descr":"","cat":"Security_system"}
msg_dw_armed={"txt":"While Armed: in ignore/unarm zone dw: {:}->{:}", "descr":"","cat":"Security_system"}
msg_master_trigger={"txt":"master trigger {:}", "descr":"","cat":"Security_system"}
msg_now_armed_emt={"txt":"arm delay {:} secs expired", "descr":"","cat":"Security_system"}
msg_lights_off_armed={"txt":"Lights OFF in armed Zones", "descr":"","cat":"Security_system"}
msg_sirens_test={"txt":"Sirens Test", "descr":"","cat":"Things_additions"}
err_ask_vfy={"txt":"!!Amazon SkillsHandler Request Verification Failed: <{:}> <{:}> <{:}>", "descr":"","cat":"My_assistant"}
err_ask_sd={"txt":"!!Amazon SkillsHandler Skills Dispatch Failed: <{:}> <{:}> <{:}>", "descr":"","cat":"My_assistant"}
msg_hue_on={"txt":"{:} via {:}/{:}/{:}/{:} -> ON", "descr":"","cat":"My_assistant"}
msg_hue_off={"txt":"{:} via {:}/{:}/{:}/{:} -> OFF", "descr":"","cat":"My_assistant"}
msg_hue_bright={"txt":"{:} via {:}/{:}/{:}/{:} -> ON + BRIGHT {:}", "descr":"","cat":"My_assistant"}
err_alexa_what={"txt":"!!Hue item misses 'what' or 'what_on' in {:}", "descr":"","cat":"My_assistant"}
msg_upnp_started={"txt":"UPNP: Responder on {:}/{:}...", "descr":"","cat":"My_assistant"}
err_alexa_crashed={"txt":"!!HUE_EMUL via {:}/{:}/{:}/{:} Crashed", "descr":"","cat":"My_assistant"}
err_upnp={"txt":"!!UPNP Responder socket.error {!s}", "descr":"","cat":"My_assistant"}
msg_upnp_reply={"txt":"UPNP: {:} -> {:}", "descr":"","cat":"My_assistant"}
msg_hue_index={"txt":"{:}-> Hue index.html read", "descr":"","cat":"My_assistant"}
msg_hue_cfg={"txt":"{:}-> Hue Config Request, usr <{:}>", "descr":"","cat":"My_assistant"}
err_hue_rcv={"txt":"!!{:} PUT {:} not in [on,off,bri]/state: {:}", "descr":"","cat":"My_assistant"}
warn_hue_rcv={"txt":"!HUE_EMUL {:} GET {:} but is not a known item", "descr":"","cat":"My_assistant"}
msg_hue_rcv_get={"txt":"{:} {:} {:} {:}", "descr":"","cat":"My_assistant"}
err_hue_req={"txt":"!!hue emul: Rcvd <{:}> this <{:}>,  returned error <{:}>, <{:}> / type <{:}>", "descr":"","cat":"My_assistant"}
msg_hue_name={"txt":"HUE_EMUL: <{:}> requested id, app:{:},device:{:}, i returned <{:}>", "descr":"","cat":"My_assistant"}
msg_hue_all={"txt":"HUE_EMUL: <{:}/{:}> requested all", "descr":"","cat":"My_assistant"}
msg_no_hue={"txt":"This pi is not Hue Bridge Emulator", "descr":"","cat":"My_assistant"}
msg_hue_light_req={"txt":"HUE_EMUL: <{:}> wanted <{:}/{:}> state, i returned <{:}/{:}>", "descr":"","cat":"My_assistant"}
msg_hue_light_set={"txt":"HUE_EMUL: <{:}> ordered <{:}/{:}> to <{:}>", "descr":"","cat":"My_assistant"}
msg_light_cmd={"txt":"Lights of rooms <{:}> to <{:}> : <{:}>", "descr":"","cat":"Light_manager"}
err_wc_miss={"txt":"!! missing wincover_manager with {:}, {:}", "descr":"","cat":"Wincover_manager"}
msg_winc_cmd={"txt":"Wincovers of rooms <{:}> to <{:}> : <{:}>", "descr":"","cat":"Wincover_manager"}
err_sanic_except={"txt":"!!Sanic except error {:}", "descr":"","cat":"Deployer"}
msg_log_req={"txt":"Log Req <{:}> ({:}) for {:}", "descr":"","cat":"Deployer"}
err_log_req={"txt":"!!Log Req <{:}> ({:}) for {:} not found", "descr":"","cat":"Deployer"}
msg_bin_req={"txt":"Bin Req <{:}> ({:}) for {:}", "descr":"","cat":"Deployer"}
msg_html_req={"txt":"HTML Req <{:}> ({:}) for {:}", "descr":"","cat":"Deployer"}
err_bin_req={"txt":"!!Bin Req <{:}> ({:}) for {:} not found", "descr":"","cat":"Deployer"}
err_rcv_bin={"txt":"!!Bin Rcv for <{:}> from <{:}> failed!{:}", "descr":"","cat":"Deployer"}
err_gmail_import={"txt":"!!Gmail API requires API imports", "descr":"","cat":"Google_driver"}
err_gmail_cred={"txt":"!!Gmail API credentials failed", "descr":"","cat":"Google_driver"}
msg_gmail_cred={"txt":"Gmail: saving creds to {:}", "descr":"","cat":"Google_driver"}
err_gmail_kw={"txt":"!!Gmail event keyword {:} for {:} not found in Hue", "descr":"","cat":"Google_driver"}
msg_gmail_kw={"txt":"Gmail Event : {:} played to {:} <{:}>", "descr":"","cat":"Google_driver"}
msg_cal_notif={"txt":"CAL nty added :{:} -> {:}/{:}", "descr":"","cat":"Google_driver"}
err_gmail_note={"txt":"!!Gmail Notes login error or IMAP not enabled, {:}", "descr":"","cat":"Google_driver"}
war_gmail_note={"txt":"!Gmail Session or Socket expired, new login required, {:} {:}", "descr":"","cat":"Google_driver"}
msg_siri_note={"txt":"gmail siri note received : <{:}>", "descr":"","cat":"Feeder"}
msg_apple_siri={"txt":"Apple siri gmail notes as voice commands checking started", "descr":"","cat":"Feeder"}
msg_gas_req={"txt":"Google Assistant: <{:}> <{:}>", "descr":"","cat":"My_assistant"}
err_gas_ky={"txt":"!!Google Assistant Secret Key error: <{:}> <{:}>", "descr":"","cat":"My_assistant"}
err_gas_json={"txt":"!!Google Assistant JSON error: <{:}> <{:}> <{:}>", "descr":"","cat":"My_assistant"}
msg_gas_kw={"txt":"Google Assistant: {:} played to {:} <{:}>", "descr":"","cat":"My_assistant"}
err_a_k_role={"txt":"!!access key role is {:} and must be {:}", "descr":"","cat":"Access_manager"}
err_event_crash={"txt":"!!Event <{:}> crashed", "descr":"","cat":"Scenes_app"}
msg_acc_key_no_access={"txt":"Access Key {:} no entry access", "descr":"","cat":"Access_manager"}
err_acc_dir_select={"txt":"!!Account_controller <{:}> is select and comma after <{:}> not in {:}", "descr":"","cat":"Access_manager"}
err_acc_templ={"txt":"!!Access Rights for <{:}>, template <{:}> is not defined in rights_templates: {:}", "descr":"","cat":"Access_manager"}
msg_acc_key_gcal={"txt":"Access Key {:} for {:} no access in google calendar", "descr":"","cat":"Access_manager"}
msg_acc_entry_ok={"txt":"{:}/{:} entry by {:}/{:}", "descr":"","cat":"Access_manager"}
msg_acc_exit_ok={"txt":"{:}/{:} exit by {:}/{:}", "descr":"","cat":"Access_manager"}
err_drv_msg={"txt":"!!{:} driver error wrapper expects msg list, not {:}", "descr":"","cat":"Things_sync"}
err_ws_crash={"txt":"!!Websocket crash: <{:}> {:}{:}", "descr":"","cat":"Things_sync"}
err_ws_sanic={"txt":"!!Websocket Sanic crash: <{:}> {:}{:}", "descr":"","cat":"Things_sync"}
err_scan_crash={"txt":"!!Scan crashed of <{:}> {:}{:}", "descr":"","cat":"Things_sync"}
err_scan_gone={"txt":"!!Scan of <{:}>  now OK!", "descr":"","cat":"Things_sync"}
err_read_crash={"txt":"!!Read of <{:}> crashed, a={:}, kw={:}", "descr":"","cat":"Things_sync"}
err_read_gone={"txt":"!!Read of <{:}> now OK!", "descr":"","cat":"Things_sync"}
err_write_crash={"txt":"!!Write to <{:}> crashed, a={:}, kw={:}", "descr":"","cat":"Things_sync"}
err_write_gone={"txt":"!!Write to <{:}> now OK!", "descr":"","cat":"Things_sync"}
err_get_crash={"txt":"!!{:} http-get crashed, a={:}, kw={:}", "descr":"","cat":"Things_sync"}
err_get_gone={"txt":"!!{:} http-get now OK!", "descr":"","cat":"Things_sync"}
warn_retry={"txt":"!{:}, retry {:}, err {:}, kw={:}{:}", "descr":"","cat":"Things_sync"}
msg_ws_connect={"txt":"Websocket: {:} is connected {:}", "descr":"","cat":"Things_sync"}
msg_ws_reject={"txt":"Websocket: {:} is rejected {:}", "descr":"","cat":"Things_sync"}
msg_ws_closed={"txt":"Websocket: {:} is closed {:}", "descr":"","cat":"Things_sync"}
err_dk_val={"txt":"!!Daikin {:} unexpected parameter <{:}> with <{:}>", "descr":"","cat":"Daikin_driver"}
err_dk_write={"txt":"!!Daikin {:} write error {:} with {:}", "descr":"","cat":"Daikin_driver"}
msg_dk_write={"txt":"!Daikin {:} write delayed {:} with {:} as not yet scanned", "descr":"","cat":"Daikin_driver"}
msg_dk_off={"txt":"!Daikin {:} is switched off as {:} mins idle", "descr":"","cat":"Daikin_driver"}
err_dk_tmp={"txt":"!!Daikin {:} write error {:} with {:} as no actual room temperature", "descr":"","cat":"Daikin_driver"}
err_dk_get_fail={"txt":"!!Daikin Requests Get Failure {:} {:}", "descr":"","cat":"Daikin_driver"}
msg_dk_set_cntrl={"txt":"Daikin {:} set_control <{:}>", "descr":"","cat":"Daikin_driver"}
err_dk_set_cntrl={"txt":"!!Daikin {:} set_control failed <{:}>", "descr":"","cat":"Daikin_driver"}
err_dk_tpe={"txt":"!!Daikin {:} {:}", "descr":"","cat":"Daikin_driver"}
msg_dk_gen={"txt":"Initiating Multiple Daikin(s) : {:}", "descr":"","cat":"Daikin_driver"}
err_b_role={"txt":"!!btle role is {:} and must be {:}", "descr":"","cat":"Btle_driver"}
err_b_tc_n={"txt":"!!btle gateway <{:}> is not a defined tc <{:}>", "descr":"","cat":"Btle_driver"}
err_b_pi_la={"txt":"!!btle leaver <{:}> is also defined in btle_arrivals list <{:}>", "descr":"","cat":"Btle_driver"}
err_b_sock={"txt":"!!btle socket cannot be opened!!", "descr":"","cat":"Btle_driver"}
err_b_drivers={"txt":"!!btle drivers for <{}> not installed!!", "descr":"","cat":"Btle_driver"}
err_b_par={"txt":"!!Beacon {:}-{:} has wrong {:} pars <{:}> != <{:}>", "descr":"","cat":"Btle_driver"}
msg_b_gw={"txt":"Beacon: {:} -> {:}", "descr":"","cat":"Btle_driver"}
msg_b_found={"txt":"Found Beacon {:} - {:} at {:}", "descr":"","cat":"Btle_driver"}
msg_b_lost={"txt":"Lost Beacon {:} - {:}/{:}", "descr":"","cat":"Btle_driver"}
msg_b_detected={"txt":"Discovered Beacon {:} - {:}/{:}", "descr":"","cat":"Btle_driver"}
msg_b_no_event={"txt":"Beacon {:} : no event defined for <{:}>", "descr":"","cat":"Access_manager"}
msg_b_gcal={"txt":"Beacon {:} for {:} no access in google calendar", "descr":"","cat":"Access_manager"}
msg_b_entry_ok={"txt":"{:} entry by beacon {:}/{:}", "descr":"","cat":"Access_manager"}
msg_b_exit_ok={"txt":"{:} exit by beacon {:}/{:}", "descr":"","cat":"Access_manager"}
msg_b_found_ign={"txt":"Beacon {:} : ignored as not discovered on {:}", "descr":"","cat":"Access_manager"}
err_ifttt_p_fail={"txt":"!!IFTTT <{:}> POST fail", "descr":"","cat":"Ifttt_driver"}
err_ifttt_g_fail={"txt":"!!IFTTT <{:}> GET fail", "descr":"","cat":"Ifttt_driver"}
msg_ifttt_ok={"txt":"IFTTT <{:}> with <{:}> : <{:}>", "descr":"","cat":"Ifttt_driver"}
err_ssi_secret={"txt":"!!web_secret missing in forensics", "descr":"","cat":"Ifttt_driver"}
err_ssi_ky={"txt":"!!Webserver SSI Secret Key error: <{:}><{:}>,data <{:}>", "descr":"","cat":"Ifttt_driver"}
err_cert_missing={"txt":"!!Missing Certificate File : <{:}>", "descr":"","cat":"Ifttt_driver"}
err_sms_to={"txt":"!!SMS invalid phone <{:}> in <{:}> in sms_driver", "descr":"","cat":"Sms_driver"}
msg_sms_sending={"txt":"SMS sending to {:}, {:} chars...", "descr":"","cat":"Sms_driver"}
msg_sms_snd={"txt":"SMS sent {:}, <{:}>", "descr":"","cat":"Sms_driver"}
err_sms_snd={"txt":"!!SMS error {:}, <{:}>, stat=<{:}>", "descr":"","cat":"Sms_driver"}
msg_sms_rcv_started={"txt":"SMS receiver process started", "descr":"","cat":"Sms_driver"}
msg_sms_rcving={"txt":"SMS receiving...", "descr":"","cat":"Sms_driver"}
msg_sms_rcv={"txt":"SMS received {:} {:}", "descr":"","cat":"Sms_driver"}
err_sms_rcv={"txt":"!!SMS from {:} not in {:}, {:}", "descr":"","cat":"Sms_driver"}
msg_sms_ign={"txt":"SMS dropped by do_sms, {:}", "descr":"","cat":"Sms_driver"}
err_sms_modem={"txt":"!!SMS modem not found, usb power restart", "descr":"","cat":"Sms_driver"}
err_sms_file={"txt":"!!SMS modem file <{:}> not exists", "descr":"","cat":"Sms_driver"}
msg_sms_notif={"txt":"SMS nty added :{:} -> {:}/{:}", "descr":"","cat":"Sms_driver"}
err_ikea_module={"txt":"!!IKEA pytradfri python module not installed, needed for <{:}>", "descr":"","cat":"Ikea_driver"}
msg_ikea_start={"txt":"IKEA pytradfri started for <{:}>", "descr":"","cat":"Ikea_driver"}
err_ikea_path={"txt":"!!IKEA path {:} missing {:}", "descr":"","cat":"Ikea_driver"}
err_shelly_tpe={"txt":"!!shelly {:} has white channel but is color_light", "descr":"","cat":"Light_manager"}
err_shelly_scene={"txt":"!!shelly {:} invalid scene {:}", "descr":"","cat":"Light_manager"}
err_shelly_get={"txt":"!!Shelly {:} requests get error {:} {:}", "descr":"","cat":"Light_manager"}
msg_shelly_get={"txt":"Shelly {:} ok for {:} {:}", "descr":"","cat":"Light_manager"}
msg_shelly_scene={"txt":"Shelly {:} {:} activated", "descr":"","cat":"Light_manager"}
err_mb_type={"txt":"!!Modbus {} is <{}> type but should be {}", "descr":"","cat":"Modbus_driver"}
err_mb_bad={"txt":"!!Modbus {} does not access : {}", "descr":"","cat":"Modbus_driver"}
err_mb_dev={"txt":"!!Modbus {} has {} not in {}", "descr":"","cat":"Modbus_driver"}
err_mb_ns={"txt":"!!Modbus {} not yet supported", "descr":"","cat":"Modbus_driver"}
err_storage_measure={"txt":"!!Utility Storage <{}>: either availability OR occupancy, yet: {:}", "descr":"","cat":"Utilities"}
err_mtr_attr={"txt":"!!Meter <{}> has {:} not in {:}", "descr":"","cat":"Utilities"}
msg_docs_gen={"txt":"DOC_GEN:started", "descr":"","cat":"Prj_parser"}
msg_docs_gen_new={"txt":"DOC_GEN:app files -> {:} docs new/updated", "descr":"","cat":"Prj_parser"}
msg_docs_new_toc={"txt":"DOC_GEN:contents table = new", "descr":"","cat":"Prj_parser"}
msg_docs_old_toc={"txt":"DOC_GEN:contents table = unchanged", "descr":"","cat":"Prj_parser"}
msg_docs_all={"txt":"DOC_GEN:making {:}", "descr":"","cat":"Prj_parser"}
err_doc_gen={"txt":"!!Doc_gen {:}", "descr":"","cat":"Prj_parser"}
err_doc_gen_cat={"txt":"!!Doc_gen 'cat' issue with {:} / {:} not in {:}", "descr":"","cat":"Prj_parser"}
err_doc_gen_xxx={"txt":"!!Doc_gen '{:}' file {:} ??, referred in {:}", "descr":"","cat":"Prj_parser"}
err_doc_gen_sub={"txt":"!!Doc_gen sub {:} not found in file {:}", "descr":"","cat":"Prj_parser"}
err_doc_gen_sect={"txt":"!!Doc_gen section/tree {:} in {:} not found in {:}", "descr":"","cat":"Prj_parser"}
err_doc_gen_tree={"txt":"!!Doc_gen tree elements <{:}> not found in tree", "descr":"","cat":"Prj_parser"}
err_doc_gen_txt={"txt":"!!Doc_gen items {:} missing in class_doc.conf ['CLASS']", "descr":"","cat":"Prj_parser"}
err_doc_gen_str={"txt":"!!Doc_gen err/warn : key {:} missing in {:}", "descr":"","cat":"Prj_parser"}
err_tts_token={"txt":"!!MS Bing txt2speech err access token {:}/{:}", "descr":"","cat":"Text2speech_driver"}
err_tts_syn={"txt":"!!MS Bing txt2speech err synthetization {:}/{:}/{:}", "descr":"","cat":"Text2speech_driver"}
msg_tts_created={"txt":"TTS Created {:} --> {:}", "descr":"","cat":"Text2speech_driver"}
err_tts_supplier={"txt":"!!text2speech_driver definition missing, cannot synthesize", "descr":"","cat":"Text2speech_driver"}

```

<!--e_insert-->
