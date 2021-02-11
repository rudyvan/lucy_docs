
# Entities

Below are the different entities that can be assigned to the keyword __property__ in the __Project()__ object.

<!--s_name_apartment-->
# Apartment

<!--e_name_apartment-->
<!--s_descr_apartment-->
entity object - Apartment

<!--e_descr_apartment-->
<!--s_tbl_apartment-->
## List of [properties](Properties.md) for __Apartment__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | occupants | list | True | - | list of occupants of the property | 
  | owners | list | True | - | list of owners of the property | 
  | rooms | *Places | - | True | rooms in the apartment | 
<!--e_tbl_apartment-->

<!--s_name_building-->
# Building

<!--e_name_building-->
<!--s_descr_building-->
entity object - Building

<!--e_descr_building-->
<!--s_tbl_building-->
## List of [properties](Properties.md) for __Building__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | common_places | *Place | - | True | shared rooms and places inside or outside, .. | 
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | managers | list | True | - | list of managers of the property | 
  | owners | list | True | - | list of owners of the property | 
  | private_entities | *Apartment | - | True | owner specific entities | 
<!--e_tbl_building-->

<!--s_name_business-->
# Business

<!--e_name_business-->
<!--s_descr_business-->
entity object - Business

<!--e_descr_business-->
<!--s_tbl_business-->
## List of [properties](Properties.md) for __Business__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | managers | list | True | - | list of managers of the property | 
  | owners | list | True | - | list of owners of the property | 
  | sites | *Site | - | True | sites controller by the business | 
<!--e_tbl_business-->

<!--s_name_house-->
# House

<!--e_name_house-->
<!--s_descr_house-->
entity object - House

<!--e_descr_house-->
<!--s_tbl_house-->
## List of [properties](Properties.md) for __House__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | occupants | list | True | - | list of occupants of the property | 
  | owners | list | True | - | list of owners of the property | 
  | places | *Place | - | True | rooms in the house and places outside such as the garden, the street, .. | 
<!--e_tbl_house-->

<!--s_name_site-->
# Site

<!--e_name_site-->
<!--s_descr_site-->
entity object - Site

<!--e_descr_site-->
<!--s_tbl_site-->
## List of [properties](Properties.md) for __Site__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | occupants | list | True | - | list of occupants of the property | 
  | owners | list | True | - | list of owners of the property | 
  | sites | *Site | - | True | places or rooms | 
<!--e_tbl_site-->

