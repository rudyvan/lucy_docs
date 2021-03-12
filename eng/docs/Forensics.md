<!--s_name-->
# Forensics

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
Collects and reports cumulative data of all Things for a 24 hours period and assigns to every things_controller access to updated status reports linked to its role

<!--e_descr-->

<!--s_tbl-->
## List of [properties](Properties.md) for __Forensics__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | notifications | ['cumuls'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 
  | role_me | {tc} | False | - | role_me of 'Forensics', adds <forensics> to the roles of the specified tc | 
  | web_interface | bool | False | - | will the output of every html generated file also be made available on port xx by every pi | 
  | web_port | int | False | - | port for the http web services | 
  | web_request | str | False | - | is the python3 format file and should contain the keywords {ip}, {port}, {file_req} | 
  | web_secret | str | False | - | (currently disabled) if an empty string, then the web_secret defaults to the secret_key of ifttt_driver | 

## List of [Notifications](Notifier.md) for  __Forensics__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | cumuls | when this report runs | 

## List of [Errors/Warnings](Error_Warn.md) for  __Forensics__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_cum_owner | !!Cumul request failed, no tc for <{:}> |  
  | err_cum_reply | !!{:} replied for {:}?? with cumul {:} |  
  | err_cum_req | !!{:} wanted cumul {:}?? |  
  | err_cumul | !!Cumul internal error for <{:}> with {:} not in {:} |  
  | err_item_cumul | !!{:} ?tc for cumul request |  
  | msg_cum_flip | Cumuls {:} |  
  | msg_cum_new_day_done | Cumul New Day resets of all tcs is completed |  
  | msg_cum_reply | cum <{:}> reply from {:}/{:} |  
  | msg_cum_request | cum <{:}> requested from {:}/{:} |  
  | msg_cum_self | cum <{:}> i have myself |  
<!--e_tbl-->

