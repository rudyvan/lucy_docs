<!--s_name-->
# Text2speech_driver

<!--e_name-->

<!--s_role-->
<!--e_role-->

## Summary

<!--s_descr-->
contains the parameters for the text to speech parameters and credentials, for Microsoft speech services, for a free subscription to speech services, 5000 messages per month goto https://account.windowsazure.com

<!--e_descr-->

Currently Microsoft Bing is implemented, but it is relatively easy to add others.

When the deployer initiates, it will check if all the say messages have a corresponding fully actual wave file and if not they will be generated so that no delay exists for one of these messages to play out.

These wave files are placed in the subdirectory tts on the raspberry memory card.

<!--s_tbl-->
## List of [properties](Properties.md) for __Text2speech_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | role_me | {tc} | False | - | role_me of 'Notifier', adds <notifier> to the roles of the specified tc | 
  | speech_gender | str | False | - | Female or Male | 
  | speech_key1 | str | False | - | important to set right as it contains the credentials for getting an access token | 
  | speech_key2 | str | True | - | is currently not used, legacy | 
  | speech_lang | str | False | - | en-GB, en-US, ..  see the list when subscribing | 
  | speech_token | str | False | - | path to get a token (valid 10 mins), do not change | 
  | speech_ttsHost | str | False | - | path to the tts engine, do not change | 
  | speech_voice | str | False | - | Microsoft Server Speech Text to Speech Voice (en-GB, Susan, Apollo) | 
  | tts_supplier | valid_list | False | - | one of the predefined text 2 speech suppliers | 

## List of [Errors/Warnings](Error_Warn.md) for  __Text2speech_driver__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_tts_supplier | !!text2speech_driver definition missing, cannot synthesize |  
  | err_tts_syn | !!MS Bing txt2speech err synthetization {:}/{:}/{:} |  
  | err_tts_token | !!MS Bing txt2speech err access token {:}/{:} |  
  | msg_tts_created | TTS Created {:} --> {:} |  
<!--e_tbl-->

## Example text2speech_driver

sensitive data (keys and account) are blanked out for privacy reasons.

```
[APPS]
    text2speech_driver={            
		# contains the parameters for the text to speech parameters and credentials
        # below are the text to speech parameters for a free subscription to Microsoft bing speech services, 5000 messages per month
        # goto https://account.windowsazure.com subscribe and copy the key1 below 
        "tts_supplier":"MS-Bing",
        "bing_account":"rudyv",                # not used
        "bing_subscr": "XXXXXXXXXXXXXXXXXXX",  # not used
        "bing_key1":   "XXXXXXXXXXXXXXXXXXX",
        "bing_key2":   "XXXXXXXXXXXXXXXXXXX",  # not used
        "bing_ttsHost":"speech.platform.bing.com",
        "bing_lang":   "en-GB",
        "bing_gender": "Female",
        "bing_voice":  "Microsoft Server Speech Text to Speech Voice (en-GB, Susan, Apollo)"}
```