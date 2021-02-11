<!--s_name_ss-->
# Site_settings

<!--e_name_ss-->

<!--s_role_ss-->
<!--e_role_ss-->

<!--s_descr_ss-->
Defines the geographical location (needed for sunset and sunrise), the email names used and some site specific parameters such as currency and temperature scale

<!--e_descr_ss-->

<!--s_tbl_ss-->
## List of [properties](Properties.md) for __Site_settings__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | EMAIL_groups | data_dict | False | - | dictionary of email lists | 
  | EMAIL_other | str | False | - | secondary email for the 'significant other's messages | 
  | EMAIL_prime | str | False | - | primary email for all messages | 
  | THINGS_account | data_dict | False | - | TBI/Things account information such as email, password, cloud license, sharing (owner/renter), calendar, logs, .. | 
  | currency | str | False | - | 1..3 letters | 
  | degrees | str | False | - | °C or °F | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | language | str | False | - | currently only 'English.eng' for English but could be Dutch.nl or French.fr | 
  | latitude | float | False | - | -90..90 | 
  | longitude | float | False | - | -180..180 | 
  | site_id | str | False | - | the site name, is the name of the subdirectory used by site_tasker to manage the things_controllers on the site | 

## List of [Errors/Warnings](Error_Warn.md) for  __Site_settings__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | msg_version | !!{:} |  
<!--e_tbl_ss-->

<!--s_name_hs-->
# Home_settings

<!--e_name_hs-->

<!--s_role_hs-->
<!--e_role_hs-->

<!--s_descr_hs-->
App to define parameters such as home occupancy, is_holiday that are crucial aspects for most other functional apps

<!--e_descr_hs-->

<!--s_tbl_hs-->
## List of [properties](Properties.md) for __Home_settings__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | home_occupancy | Virtual_R | False | - | is a derived virtual from is_holiday, is_armed_full, is_armed_partial and the value is 0..3 : 'Day','Away','Sleep','Holiday' | 
  | icon | str | True | - | icon file for this element | 
  | is_day | Virtual | False | - | are we night (before sunrise or after sunset) or day? | 
  | is_holiday | Virtual | False | - | is holiday active? | 
  | is_reboot | Virtual | False | - | is true for 2 seconds to say the system was rebooting | 
<!--e_tbl_hs-->

