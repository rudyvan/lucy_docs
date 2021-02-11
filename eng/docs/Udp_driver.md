<!--s_name-->
# Udp_driver

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
UDP Driver

<!--e_descr-->

<!--s_tbl-->
## List of [properties](Properties.md) for __Udp_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | port | int | False | - | ip port | 

## List of [Errors/Warnings](Error_Warn.md) for  __Udp_driver__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_dropbox | !!Dropbox: {:} upload failed, {:} -> {:} |  
  | err_send_failed | !!{:} Send FAILED {:} to {:} {:} for {:} |  
  | err_socket_creat | !!{:} Socket Create/Bind Failed |  
  | msg_dropbox | Dropbox: processed {:} |  
<!--e_tbl-->

