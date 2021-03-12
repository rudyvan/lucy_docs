<!--s_name-->
# Deployer

<!--e_name-->

<!--s_role-->
<!--e_role-->
## Summary

<!--s_descr-->
Manages and protects the things-controllers if multiple are deployed at a site and ensures automatic program version distribution and health check

<!--e_descr-->

Files to be placed in ~/bin/. When the master sends via UDP the string {"type":"cmd","role":"cmd_do","cmd":"reload_all"} to this things_controller, all things_controllers update one after another.

This script need to be rebuild with the possibilities of github and the new site_tasker module.

<!--s_tbl-->
## List of [properties](Properties.md) for __Deployer__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | role_me | {tc} | False | - | role_me of 'Deployer', adds <deploy> to the roles of the specified tc | 

## List of [Errors/Warnings](Error_Warn.md) for  __Deployer__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_bin_req | !!Bin Req <{:}> ({:}) for {:} not found |  
  | err_cpy_overwrite | !!upload overwrite for {:} not found @{:} |  
  | err_log_req | !!Log Req <{:}> ({:}) for {:} not found |  
  | err_no_deploy | !!deployer is not defined |  
  | err_rcv_bin | !!Bin Rcv for <{:}> from <{:}> failed!{:} |  
  | err_reload_files | !!Error reloading downloaded files |  
  | err_run_loop | !!Main Task(s) {:} |  
  | err_sanic_except | !!Sanic except error {:} |  
  | err_sync_call | !!wait_for func {} in {} not callable |  
  | err_task_repeat | !!Task {:} not done and re-asked |  
  | err_tim_task | !!TimerTask {:} returned exception: {:} |  
  | err_timer_bug | !!Timer {:} has {:} |  
  | err_timer_gone | !!Timer {:} unexpectedly not there |  
  | err_upl_done | !!Upload tc's completed, missing <{:}> |  
  | msg_bin_req | Bin Req <{:}> ({:}) for {:} |  
  | msg_cmd_for | CMD: {:} for {:} |  
  | msg_cmd_reload | CMD:Reload |  
  | msg_cpy_file_done | {:} copy and overwrite completed |  
  | msg_html_req | HTML Req <{:}> ({:}) for {:} |  
  | msg_log_req | Log Req <{:}> ({:}) for {:} |  
  | msg_rcv_file_done | {:} received |  
  | msg_upl_done | Upload tc's completed |  
  | msg_upl_ordered | Reload ordered to {:} |  
  | msg_upl_started | Upload all tc's Started |  
  | warn_timer_overrun | !Timer {:} has {:} |  
  | warn_timer_start | !Bounce Timer <{:}> started as output found active without timer - {:} | a bad fixup 
<!--e_tbl-->

* * * 
* * * 
# Parsing Reporting Example

* * * 
* * * 

<!--s_insert_{"role":"deploy","suffix":"ref"}-->


[imac-lucy_ref.html](imac-lucy_ref.html)
<!DOCTYPE html><html><body><h1>Report_ref -> imac-lucy_ref.html  2021/02/07 11:25:57</h1>

<!--e_insert-->

* * * 
* * *

