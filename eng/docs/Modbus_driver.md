<!--s_name-->
# Modbus_driver

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
is the driver for Modbus

<!--e_descr-->

<!--s_tbl-->
## List of [properties](Properties.md) for __Modbus_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | notifications | ['modbus_parsing'] | True | - | extensive list of notifications, see [__Notifier__](Notifier.md) | 

## List of [Notifications](Notifier.md) for  __Modbus_driver__:

  | Notification Suffix | When invoked? |
  | --- | --- | 
  | modbus_parsing | when this report runs | 

## List of [Errors/Warnings](Error_Warn.md) for  __Modbus_driver__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_mb_bad | !!Modbus {} does not access : {} |  
  | err_mb_dev | !!Modbus {} has {} not in {} |  
  | err_mb_ns | !!Modbus {} not yet supported |  
  | err_mb_type | !!Modbus {} is <{}> type but should be {} |  
<!--e_tbl-->

