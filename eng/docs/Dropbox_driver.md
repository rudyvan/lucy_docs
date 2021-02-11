<!--s_name-->
# Dropbox_driver

<!--e_name-->

## Summary

<!--s_role-->
<!--e_role-->

<!--s_descr-->
This driver defines the dropbox handler and the dropbox paths to the folders where logs, cumulative data and program scripts is to be updated.  This updating occurs automatically at the end of the day before log files or cumulative files are refreshed for a new day

<!--e_descr-->

Storing log files and cumulative data files on raspberry memory chips is not a scalable solution.

Dropbox was chosen as remote storage for these files because a relatively easy installation scenario exists for a small raspberry computer wanting to use dropbox file storage.

## Dropbox Installation

A dropbox app needs to be created with this link:   https://www.dropbox.com/developers/apps

login to DropBox and create an “app” by clicking the “create app” button.

Then choose “Dropbox API app”, “Files and Datastores” and answer the final question “Can your app be limited to its own, private folder?” – either answer is OK, depending on your needs.

Then you need to give your app a unique name.

Visit the OAuth 2 section and generate a token.

You need to copy/paste this token in the uploader script that comes with the dropbox installation on the raspberry.
 
In this app directory you will find a subdirectory with the given name of the app.
Lucy will create in this directory some sub directories and store some files:

| Directory | What is stored? |
| --- | --- |
__logs__ | the log, err files of the deploy, data, security and climate raspberry's per date and the security pickle file with all the security logging |
__cums__ | one file per day with the cumulative history of the data and climate raspberry |


<!--s_tbl-->
## List of [properties](Properties.md) for __Dropbox_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | p_dropbox | str | False | - | path to the dropbox folder where everything need to get sync | 

## List of [Errors/Warnings](Error_Warn.md) for  __Dropbox_driver__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_mnt_failed | !!Share Mount Failed for {:} |  
<!--e_tbl-->

## Example dropbox_driver

```
[INTERFACES]
dropbox_driver={ 
    "role_me":  "PI-Data", # this raspberry uploads files to dropbox
    "p_dropbox":"/home/rudyv/Dropbox/Apps/PI-SCAN-RUDYV/"}
```