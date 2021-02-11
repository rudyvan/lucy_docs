<!--s_name-->
# Log_driver

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
This is the logging that the apps will use to keep a trace of what is happening

<!--e_descr-->

## Summary

Every things controller maintains a detailed log of many script steps and a separate log for errors.

A major portion of the logs are also transmitted to the deployer who keeps an overall log of all.
This log is daily archived in dropbox if this driver is active.

Also the security and climate things controller have their log archived.

<!--s_tbl-->
## List of [properties](Properties.md) for __Log_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | notifications | ['log_errs', 'log_no_errs'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 

## List of [Notifications](Notifier.md) for  __Log_driver__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | log_errs |  | 
  | log_no_errs |  | 

## List of [Errors/Warnings](Error_Warn.md) for  __Log_driver__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_color | !!color {:} not recognised |  
  | err_log_not | !!log email nok, log not erased:{:} |  
  | msg_log_err |  with {:} Errors |  
  | msg_log_subj | Log File {:} |  
  | msg_new_log | New Log Started |  
<!--e_tbl-->

