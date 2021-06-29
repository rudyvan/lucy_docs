<!--s_name-->
# Sma_driver

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
is the driver for Sunny SMA

<!--e_descr-->

<!--s_tbl-->
## List of [properties](Properties.md) for __Sma_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | notifications | ['sma_forensics', 'sma_parsing'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 
  | role_me | {tc} | False | - | role_me of 'Sma_driver', adds <sma_drv> to the roles of the specified tc | 

## List of [Notifications](Notifier.md) for  __Sma_driver__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | sma_forensics | this report runs at then end of the day to list all sma thingscontrollers data | 
  | sma_parsing | this report runs when parsing of sma thingscontrollers is complete | 

## List of [Errors/Warnings](Error_Warn.md) for  __Sma_driver__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_sma_bad | !!Sma {} does not access : {} |  
  | err_sma_dev | !!Sma {} has {} not in {} |  
  | err_sma_ns | !!Sma {} not yet supported |  
  | err_sma_type | !!Sma {} is <{}> type but should be {} |  
<!--e_tbl-->

