#!/usr/bin/python3
# encoding=utf-8
from lucy import *

class Project:
    ''' Start Entity Project

    start entity object - Project

    - **parameters** and **types**

    :param settings: home, site and app settings for this project in a list
    :param drivers: all drivers in this project in a list
    :param apps: all apps in this project in a list
    :param property: the entity in this project such as a Building, an Apartment, a House or just a Site
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type settings:  ['Home_settings', 'Site_settings', 'Things_additions']
    :type drivers:  *_Driver
    :type apps:  *_App
    :type property:  *_Entity
    :type fav:  str
    :type icon:  str
    '''
    pass

class Apartment:
    ''' Entity Apartment

    entity object - Apartment

    - **parameters** and **types**

    :param rooms: rooms in the apartment
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param occupants: list of occupants of the property
    :param owners: list of owners of the property
    :type rooms:  *Places
    :type fav:  str
    :type icon:  str
    :type occupants:  list
    :type owners:  list
    '''
    pass

class Building:
    ''' Entity Building

    entity object - Building

    - **parameters** and **types**

    :param common_places: shared rooms and places inside or outside, ..
    :param private_entities: owner specific entities
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param managers: list of managers of the property
    :param owners: list of owners of the property
    :type common_places:  *Place
    :type private_entities:  *Apartment
    :type fav:  str
    :type icon:  str
    :type managers:  list
    :type owners:  list
    '''
    pass

class Business:
    ''' Entity Business

    entity object - Business

    - **parameters** and **types**

    :param sites: sites controller by the business
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param managers: list of managers of the property
    :param owners: list of owners of the property
    :type sites:  *Site
    :type fav:  str
    :type icon:  str
    :type managers:  list
    :type owners:  list
    '''
    pass

class House:
    ''' Entity House

    entity object - House

    - **parameters** and **types**

    :param places: rooms in the house and places outside such as the garden, the street, ..
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param occupants: list of occupants of the property
    :param owners: list of owners of the property
    :type places:  *Place
    :type fav:  str
    :type icon:  str
    :type occupants:  list
    :type owners:  list
    '''
    pass

class Site:
    ''' Entity Site

    entity object - Site

    - **parameters** and **types**

    :param sites: places or rooms
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param occupants: list of occupants of the property
    :param owners: list of owners of the property
    :type sites:  *Site
    :type fav:  str
    :type icon:  str
    :type occupants:  list
    :type owners:  list
    '''
    pass

class Btle_driver:
    ''' Btle_driver in Driver

    Bluetooth low energy beacons! They are used to provide access and registration to the house for cars and motor's or for other mobile services (heart monitoring..)

    - **parameters** and **types**

    :param role_me: role_me of 'Btle_driver', adds <beacon> to the roles of the specified tc
    :param notifications: notifications whereby {id} is the device equipped with a btle tag, see [__Notifier__](Notifier.md)
    :param btle_blackout: virtual to blackout all btle devices
    :param btle_entry_blackout: virtual to blackout arrival of btle devices
    :param btle_exit_blackout: virtual to blackout leavers of btle devices
    :param btle_gw_entry: list of names of tc btle gateways furthest from the home to first notice the arrival of btle devices wanting to enter
    :param btle_gw_exit: list of names of tc btle gateways closest in the home to first notice the wakeup of btle devices that are going to exit
    :param btle_gw_other: list of names of tc btle gateways used for other purposes than access beacons
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'b_none': 'person/device not recognised notification', '{id}.b_entry': 'person/device entry notification', '{id}.b_exit': 'person/device exit notification', '{id}.b_detected': 'beacon discovered notification, only if scenes are to be executed', '{id}.b_lost': 'beacon lost notification, only if scenes are to be executed', '{id}.b_refused': 'person/device entry refused notification'}
    :type btle_blackout:  Virtual
    :type btle_entry_blackout:  Virtual
    :type btle_exit_blackout:  Virtual
    :type btle_gw_entry:  data_list
    :type btle_gw_exit:  data_list
    :type btle_gw_other:  data_list
    :type fav:  str
    :type icon:  str
    '''
    pass

class Camera_driver:
    ''' Camera_driver in Driver

    Driver for interfacing with camera's for pictures (pic), video (vid) and date/time (datim) setting.  Per cameratype the url's should be defined

    - **parameters** and **types**

    :param cam_types: per cam_tpe define a dictionary with url's for pic, vid and datim (picture, video and date/time setting).   Use keywords for format_map such as {ip}, {port}, {user}, which are camera specific, and {pwd} - derived from your system, and for datim {ntp_server} - from network_controller and {time_zone} which will be the time offset when you set the camera time. Monitor with Fiddler when changing manually a camera setting and then you have the string to use
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type cam_types:  dict
    :type fav:  str
    :type icon:  str
    '''
    pass

class Daikin_driver:
    ''' Daikin_driver in Driver

    This driver enables the daikin room airconditioners to be used in the climatization app as room coolers, heaters, ventilators or air dryers

    - **parameters** and **types**

    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param idle_time_off: minutes time elapse to shutdown the unit when the room temp stays above (for heating or below for cooling) the soll temperature, then switch it off, is also a time override in case manually activated by an app or remote control.
    :param skip_if_multi: skip activating the unit if for that room for that mode (cooling or heating) multiple energy sources exist and if powerful mode is not needed
    :param streamer_mode: io streamer mode decomposes and removes allergens such as mould, mites, and pollen, along with any unpleasant odours that may have infiltrated your home.  Not all units support this mode and then this is ignored.
    :param C_diff_off: difference between the SetPoint °C and the room °C to switch off the unit when the room °C is below (cooling) or above (heating) wanted temp
    :param C_diff_powerful: difference between the SetPoint °C and the room °C to activate the powerful mode when the room °C is above (cooling) or below (heating) wanted temp.  Not all units suppoer powerful mode and then this is ignored.
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type notifications:  {'daikin_parsing': 'when this report runs'}
    :type idle_time_off:  int
    :type skip_if_multi:  bool
    :type streamer_mode:  bool
    :type C_diff_off:  float
    :type C_diff_powerful:  float
    :type fav:  str
    :type icon:  str
    '''
    pass

class Dropbox_driver:
    ''' Dropbox_driver in Driver

    This driver defines the dropbox handler and the dropbox paths to the folders where logs, cumulative data and program scripts is to be updated.  This updating occurs automatically at the end of the day before log files or cumulative files are refreshed for a new day

    - **parameters** and **types**

    :param role_me: role_me of 'Dropbox_driver', adds <dropbox> to the roles of the specified tc
    :param p_dropbox: path to the dropbox folder where everything need to get sync
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type p_dropbox:  str
    :type fav:  str
    :type icon:  str
    '''
    pass

class Google_driver:
    ''' Google_driver in Driver

    This is the google calendar driver to read the calendar and read person and device credentials (f.i. is entrance allowed?) and to execute events such as holidays, heating up guest rooms, triggering irrigation or lights for special occasions

    - **parameters** and **types**

    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param application_name: the 'given' google calendar application name
    :param client_secret_file: the file name of the oath secret file
    :param scopes: is the path to the google api scope
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type notifications:  {'cal_log': 'generated calendar events, when this report runs', 'gmail_events': 'when this report runs'}
    :type application_name:  str
    :type client_secret_file:  str
    :type scopes:  str
    :type fav:  str
    :type icon:  str
    '''
    pass

class Hue_driver:
    ''' Hue_driver in Driver

    This is the Philips Hue driver, to interface to the Philips Hue bridge that drives all the Hue devices

    - **parameters** and **types**

    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param hue_port: the Philips Hue bridges port, they are default 80
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type notifications:  {'hue_parsing': 'when this report runs'}
    :type hue_port:  int
    :type fav:  str
    :type icon:  str
    '''
    pass

class Ifttt_driver:
    ''' Ifttt_driver in Driver

    IFTTT IF THIS THEN THAT driver, both as a trigger with 'maker' and as an google assistant applet processor, These allow ok Google to work, see instructions and the trigger url and reverse web hook url

    - **parameters** and **types**

    :param role_me: role_me of 'Ifttt_driver', adds <IFTTT> to the roles of the specified tc
    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param google_assistant: for the IFTTT applet with google assistant and webhooks
    :param request_port: the port to map from your router to the security role computer which will watch this port for incoming IFTTT messages
    :param reverse_url: the url needed to reach the security things_controller
    :param secret_key: private secret
    :param skip_ifttt_in: the virtual that allows or prohibit incoming IFTTT maker messages
    :param skip_ifttt_out: the virtual that allows or prohibit outgoing IFTTT triggers
    :param trigger_url: the url needed to reach the IFTTT maker trigger
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'ifttt_log': 'when this report runs'}
    :type google_assistant:  bool
    :type request_port:  int
    :type reverse_url:  str
    :type secret_key:  str
    :type skip_ifttt_in:  Virtual
    :type skip_ifttt_out:  Virtual
    :type trigger_url:  str
    :type fav:  str
    :type icon:  str
    '''
    pass

class Ikea_driver:
    ''' Ikea_driver in Driver

    This is the IKEA Tradfri driver, to interface to the IKEA Tradfri light gateways that drives all the Tradfri devices

    - **parameters** and **types**

    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type notifications:  {'ikea_parsing': 'when this report runs'}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Ip_building_driver:
    ''' Ip_building_driver in Driver

    is the driver for the IP-Building modules

    - **parameters** and **types**

    :param role_me: role_me of 'Ip_building_driver', adds <ip_building> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Log_driver:
    ''' Log_driver in Driver

    This is the logging that the apps will use to keep a trace of what is happening

    - **parameters** and **types**

    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type notifications:  {'log_errs': '', 'log_no_errs': ''}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Loxone_driver:
    ''' Loxone_driver in Driver

    is the driver for the loxone master module ip interface

    - **parameters** and **types**

    :param role_me: role_me of 'Loxone_driver', adds <loxone> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Netatmo_wlc_driver:
    ''' Netatmo_wlc_driver in Driver

    Netatmo welcome system driver -> make a different id compared with the netatmo weather station.  Netatmo Welcome: name your netatmo welcome camera and tags.

    - **parameters** and **types**

    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param netatmo_client_id: Your client ID from Netatmo app registration at http://dev.netatmo.com/dev/listapps
    :param netatmo_client_secret: Your client app secret
    :param netatmo_home: specify yr netatmo home name
    :param netatmo_password: ''= same as your email notification
    :param netatmo_user_name: ''= default is your email notification address
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type notifications:  {'na_welcome': 'when this report runs'}
    :type netatmo_client_id:  str
    :type netatmo_client_secret:  str
    :type netatmo_home:  str
    :type netatmo_password:  str
    :type netatmo_user_name:  str
    :type fav:  str
    :type icon:  str
    '''
    pass

class Netatmo_ws_driver:
    ''' Netatmo_ws_driver in Driver

    Netatmo weather station driver -> make a different id compared with the netatmo welcome system.  Name your inhouse and outhouse station to the room where they are placed, e.g. 'garden','office' and rainmeter / windmeter for these modules

    - **parameters** and **types**

    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param netatmo_client_id: Your client ID from Netatmo app registration at http://dev.netatmo.com/dev/listapps
    :param netatmo_client_secret: Your client app secret
    :param netatmo_password: ''= same as your email notification
    :param netatmo_user_name: ''= default is your email notification address
    :param netatmo_home: ''= default is the first station if you have defined many, else name your desired station
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type notifications:  {'ws_air_quality': '', 'ws_gust': '', 'ws_humidity': '', 'ws_noise': '', 'ws_pressure': '', 'ws_rain_1': '', 'ws_rain_24': '', 'ws_report': '', 'ws_rf_stat': '', 'ws_wifi_stat': '', 'ws_wind': ''}
    :type netatmo_client_id:  str
    :type netatmo_client_secret:  str
    :type netatmo_password:  str
    :type netatmo_user_name:  str
    :type netatmo_home:  str
    :type fav:  str
    :type icon:  str
    '''
    pass

class One_wire_driver:
    ''' One_wire_driver in Driver

    Handles the 1 wire sensors, 1 wire devices and iButtons

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type fav:  str
    :type icon:  str
    '''
    pass

class Piface_driver:
    ''' Piface_driver in Driver

    Reads and writes binary inputs and outputs on the piface hat

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type fav:  str
    :type icon:  str
    '''
    pass

class Sms_driver:
    ''' Sms_driver in Driver

    GSM SMS driver, both as a notification sender of messages as a receiver of remote commands, via the hologram nova modem, see http://hologram.io

    - **parameters** and **types**

    :param role_me: role_me of 'Sms_driver', adds <sms> to the roles of the specified tc
    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param do_sms: the virtual that allows or prohibit sms messages.  This virtual is ignored if override is true in the sms message dictionary
    :param sms_from: authorised sources of sms messages, whereby phone is an E.164 formatted string with a '+' sign.  If empty then all sources are allowed
    :param sms_rcv: the bash command string for receiving a message, if empty then no sms receiving will happen
    :param sms_snd: the bash command string for sending a message, whereby phone is an E.164 formatted string with a '+' sign whereto the msg sms message will be sent
    :param sms_tags: tags that work like formatting in strings in python
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'sms_log': 'when this report runs'}
    :type do_sms:  Virtual
    :type sms_from:  data_list
    :type sms_rcv:  str
    :type sms_snd:  str
    :type sms_tags:  data_dict
    :type fav:  str
    :type icon:  str
    '''
    pass

class Sonos_driver:
    ''' Sonos_driver in Driver

    The Sonos Driver to play notifications through a sonos setup.   Define the sonos speakers with the Sonos() thing!

    - **parameters** and **types**

    :param role_me: role_me of 'Sonos_driver', adds <sonos> to the roles of the specified tc
    :param party_mode: Create and disolve a party mode group for multi-room messages?  If yes, there is more time needed for grouping and ungrouping, but all the speakers work synchroneously.  It is recommended to use party mode with only a few speakers.
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type party_mode:  bool
    :type fav:  str
    :type icon:  str
    '''
    pass

class Tcp_driver:
    ''' Tcp_driver in Driver

    TCP Driver

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param port: ip port
    :type fav:  str
    :type icon:  str
    :type port:  int
    '''
    pass

class Text2speech_driver:
    ''' Text2speech_driver in Driver

    contains the parameters for the text to speech parameters and credentials, for Microsoft speech services, for a free subscription to speech services, 5000 messages per month goto https://account.windowsazure.com

    - **parameters** and **types**

    :param speech_gender: Female or Male
    :param speech_key1: important to set right as it contains the credentials for getting an access token
    :param speech_key2: is currently not used, legacy
    :param speech_lang: en-GB, en-US, ..  see the list when subscribing
    :param speech_token: path to get a token (valid 10 mins), do not change
    :param speech_ttsHost: path to the tts engine, do not change
    :param speech_voice: Microsoft Server Speech Text to Speech Voice (en-GB, Susan, Apollo)
    :param tts_supplier: one of the predefined text 2 speech suppliers
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type speech_gender:  str
    :type speech_key1:  str
    :type speech_key2:  str
    :type speech_lang:  str
    :type speech_token:  str
    :type speech_ttsHost:  str
    :type speech_voice:  str
    :type tts_supplier:  valid_list
    :type fav:  str
    :type icon:  str
    '''
    pass

class Unipi_driver:
    ''' Unipi_driver in Driver

    Reads and writes binary and analog inputs and outputs on the unipi and neutron hats using evok, see http://www.unipi.technology

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type fav:  str
    :type icon:  str
    '''
    pass

class Udp_driver:
    ''' Udp_driver in Driver

    UDP Driver

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param port: ip port
    :type fav:  str
    :type icon:  str
    :type port:  int
    '''
    pass

class Usb_driver:
    ''' Usb_driver in Driver

    Driver for interfacing with usb serial devices.

    - **parameters** and **types**

    :param usb_paths: Per usb_path the port, baudrate and other parameters of the serial port should be defined. Use a dictionary with keywords as in use of the python serial module for open such as {port}, {baudrate}, {bytesize}, {parity}, {stopbits},.. If the port name ends with *, then the first matching portname will be used instead of an exact name.
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type usb_paths:  dict
    :type fav:  str
    :type icon:  str
    '''
    pass

class Vera_driver:
    ''' Vera_driver in Driver

    The driver to vera devices used for zwave communications and the scene's used for voice triggering.  Vera has the most complete and open zwave and zigbee gateway on the market, supporting the most diverse zwave things

    - **parameters** and **types**

    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param alexa_cmds: these become voice commands for Alexa by the security role pi sent to vera
    :param vera_cmds: the vera control commands - need to be mapped with the scene/device number used within Vera
    :param vera_port: the port for access to the vera device
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type notifications:  {'vera_parsing': 'when this report runs'}
    :type alexa_cmds:  dict
    :type vera_cmds:  dict
    :type vera_port:  int
    :type fav:  str
    :type icon:  str
    '''
    pass

class Access_keys:
    ''' Access_keys in App

    is a dictionary of access keys for persons with access keys or vehicles with btle tags that define the access rights granted by the controller where the access key is registered

    - **parameters** and **types**

    :param keys: is a dictionary of access keys for persons with access keys or vehicles with btle tags that define the access rights granted by the controller where the access key is registered
    :param rights_templates: is a dictionary of right templates that links a template to a list of access rights
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type keys:  ['Access']
    :type rights_templates:  data_dict
    :type fav:  str
    :type icon:  str
    '''
    pass

class Access_manager:
    ''' Access_manager in App

    Defines access for people or items such as cars.  For people access_point's register incoming and outgoing persons and grant access given proper credentials. For items, bluetooth low energy keys can be used.  This App defines the access keys and what they do, and the respective notifications and ifttt hooks

    - **parameters** and **types**

    :param role_me: role_me of 'Access_manager', adds <access> to the roles of the specified tc
    :param notifications: notifications whereby {id} is the device or person, see [__Notifier__](Notifier.md)
    :param access_scenes: a dict with scenes events for entering/leaving the premises or controlling access to any particular room
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'a_none': 'person/device not recognised notification', '{id}.a_entry': 'person/device entry notification', '{id}.a_exit': 'person/device exit notification', '{id}.a_refused': 'person/device entry refused notification'}
    :type access_scenes:  data_dict
    :type fav:  str
    :type icon:  str
    '''
    pass

class Climate_manager:
    ''' Climate_manager in App

    The Climatisation App manages all the multi room climate systems and individual climate makers working solo for a room

    - **parameters** and **types**

    :param role_me: role_me of 'Climate_manager', adds <m.clim> to the roles of the specified tc
    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param climate_comfort_mode: virtual to capture the current climate comfort mode : 'Economy','Normal' or 'Comfort' at a global level, as rooms can be put into an individual climate mode.  Economy (comfort) means that a value is subtracted (added) to every rooms setpoint
    :param climate_mode: virtual to capture the climate system state : 'Cooling','Off' or 'Heating'.  The climate system is off when the outside temperature is within comfort boundaries and there is no need for climatisation
    :param cold_priority_temp: above this temperature, cooling is activated, even when the room is off
    :param heat_priority_frost: is the temp of the room in which it becomes a heat_room_is_priority room notwithstanding its status defined below
    :param holiday_sp: holiday absence minimum safeguards, is a dict with keys: warm_sp, cold_sp, dry_sp, moist_sp, dark_sp, light_sp
    :param is_cooling: virtual to capture if the climate system is in cooling mode
    :param is_cooling_temp: temperature outside above, then cooling will be activated
    :param is_dry: virtual to capture if the climate system is dry and needs humidification
    :param is_heating: virtual to capture if the climate system is in heating mode
    :param is_heating_temp: temperature outside below, then heating will be activated, just make sure that is_cooling_temp is higher than is_heating_temp
    :param is_humid: virtual to capture if the climate system is humid and needs drying
    :param is_lum_dark: virtual to capture if the climate system is dark and needs lightening
    :param is_lum_light: virtual to capture if the climate system is light and needs darkening
    :param role_followers: list of names of tc's that are climate slaves, all the same processing but driving outputs is disabled as this is exclusive for the master.  They are good to show on a display what happens...
    :param sp_presets: dictionary of climate setpoint presets
    :param C_outdoor_cm: outside temperature sensor, lower temperature means the more warm the boiler water has to become before the boiler is deactivated
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'climate_report': 'notification when the climate report is issued', 'comfort_0': 'climate comfort mode is disabled', 'comfort_1': 'climate comfort mode is enabled', 'economy_0': 'climate economy mode is disabled', 'economy_1': 'climate economy mode is enabled', '{room}.humid_ok_0': 'humidity for the room is nok', '{room}.humid_ok_1': 'humidity for the room is ok', '{room}.temp_ok_0': 'temperature for the room is nok', '{room}.temp_ok_1': 'temperature for the room is ok', '{room}.lum_ok_0': 'light intensity for the room is nok', '{room}.lum_ok_1': 'light intensity for the room is ok', '{room}.clim_on_0': 'climate for the room is disabled', '{room}.clim_on_1': 'climate for the room is enabled', '{room}.comfort_0': 'climate comfort mode for the room is disabled', '{room}.comfort_1': 'climate comfort mode for the room is enabled', '{room}.economy_0': 'climate economy mode for the room is disabled', '{room}.economy_1': 'climate economy mode for the room is enabled'}
    :type climate_comfort_mode:  Virtual_R
    :type climate_mode:  Virtual_R
    :type cold_priority_temp:  float
    :type heat_priority_frost:  float
    :type holiday_sp:  data_dict
    :type is_cooling:  Virtual
    :type is_cooling_temp:  float
    :type is_dry:  Virtual
    :type is_heating:  Virtual
    :type is_heating_temp:  float
    :type is_humid:  Virtual
    :type is_lum_dark:  Virtual
    :type is_lum_light:  Virtual
    :type role_followers:  data_list
    :type sp_presets:  data_dict
    :type C_outdoor_cm:  Sensor
    :type fav:  str
    :type icon:  str
    '''
    pass

class Prj_parser:
    ''' Prj_parser in App

    This is the home configuration compiler and syntax checker, it generates the binary objects that the apps will work from

    - **parameters** and **types**

    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type notifications:  {'prj_parser': 'notification when Prj_parser completes'}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Deployer:
    ''' Deployer in App

    Manages and protects the things-controllers if multiple are deployed at a site and ensures automatic program version distribution and health check

    - **parameters** and **types**

    :param role_me: role_me of 'Deployer', adds <deploy> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Feeder:
    ''' Feeder in App

    This App processes incoming commands from various sources and checks eligibility.  Sources for the feeder could be Vera, TCP, UDP, IFTTT, Calendar, email, SMS, twitter,... Also included is the master and other things_controllers who need a service.  The feeder generates a report with all the possible commands with parameters and if and who can execute such command.

    - **parameters** and **types**

    :param role_me: role_me of 'Feeder', adds <feeder> to the roles of the specified tc
    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param access_trigger: this is the instruction python3 format for feeder in one of the channels for access, put {access} where the person's or vehicle name should appear
    :param can_feed: virtual to allow the feeder to work
    :param can_feed_cal: virtual to allow the feeder to work from calendar
    :param can_feed_ifttt: virtual to allow the feeder to work from ifttt
    :param can_feed_mail: virtual to allow the feeder to work from mail
    :param can_feed_sms: virtual to allow the feeder to work from sms
    :param can_feed_tcp: virtual to allow the feeder to work from tcp
    :param can_feed_udp: virtual to allow the feeder to work from udp
    :param channels: list of the feeder authorized channels
    :param event_trigger: this is the instruction format for the feeder in the google calendar event or google email subject field or one of the other channels. It should prefix the action string, and __an exclamation point in front of the action string reverses the meaning, makes it 'not'__.  Example:  @ALEXA@=Holiday  where Holiday is an alexa intent that will set <on>/<off> at the beginning/end of the event. Also an inversion is allowed: @ALEXA@=!Holiday
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'feeder': 'feeder commands are decorated python functions and this report lists the result for this tc', 'feeder_log': 'logging of received feeder commands'}
    :type access_trigger:  str
    :type can_feed:  Virtual
    :type can_feed_cal:  Virtual
    :type can_feed_ifttt:  Virtual
    :type can_feed_mail:  Virtual
    :type can_feed_sms:  Virtual
    :type can_feed_tcp:  Virtual
    :type can_feed_udp:  Virtual
    :type channels:  data_list
    :type event_trigger:  str
    :type fav:  str
    :type icon:  str
    '''
    pass

class Home_settings:
    ''' Home_settings in App

    App to define parameters such as home occupancy, is_holiday that are crucial aspects for most other functional apps

    - **parameters** and **types**

    :param role_me: role_me of 'Home_settings', adds <home_settings> to the roles of the specified tc
    :param home_occupancy: is a derived virtual from is_holiday, is_armed_full, is_armed_partial and the value is 0..3 : 'Day','Away','Sleep','Holiday'
    :param is_day: are we night (before sunrise or after sunset) or day?
    :param is_holiday: is holiday active?
    :param is_reboot: is true for 2 seconds to say the system was rebooting
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type home_occupancy:  Virtual_R
    :type is_day:  Virtual
    :type is_holiday:  Virtual
    :type is_reboot:  Virtual
    :type fav:  str
    :type icon:  str
    '''
    pass

class Irrigation_manager:
    ''' Irrigation_manager in App

    The Irrigation App, whereby based on past and furture rain precipitation plant watering is optimized

    - **parameters** and **types**

    :param role_me: role_me of 'Irrigation_manager', adds <irrigation> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Light_manager:
    ''' Light_manager in App

    Defines the things_controller managing the light process and steering the Hue bridges, the IKEA tradfri gateways and any Vera light devices

    - **parameters** and **types**

    :param role_me: role_me of 'Light_manager', adds <light> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class My_assistant:
    ''' My_assistant in App

    Advanced voice control with Amazon's Alexa, ok_Google, Siri Notes and for instructions from calendar and mail and for the Apps that are enabled to receive voice instructions

    - **parameters** and **types**

    :param role_me: role_me of 'My_assistant', adds <my_assistant> to the roles of the specified tc
    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param bridge_prefix: the emulated bridge name will appear in the iphone hue app with this prefix and its role
    :param i_use: is the list of the voice assistants suppliers you use and the instructions to your butler in google calendar or via email (= To Be Done)
    :param link_button: when this virtual is up, then adding users (just like a real hue bridge) is allowed
    :param may_do: is the list of the functional apps that your butler may serve
    :param port: should be an unique port number not in use elsewhere, and as Hue bridges have themselves port 80 as default, Amazon Echo will detect them only if at 80
    :param siri_notes: use apple siri as voice control input, by creating a note in gmail that is the voice command
    :param siri_users: tuples of email address and password so to access the 'notes' section for commands, by default the main email, paswd is automatically included
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'hue_emul': '', 'hue_emul_log': '', 'voice_bad': ''}
    :type bridge_prefix:  str
    :type i_use:  valid_set
    :type link_button:  Virtual
    :type may_do:  valid_set
    :type port:  int
    :type siri_notes:  bool
    :type siri_users:  data_list
    :type fav:  str
    :type icon:  str
    '''
    pass

class Network_controller:
    ''' Network_controller in App

    Protects the ip network. Scans all devices for ping latency, a summary is emailed at midnight

    - **parameters** and **types**

    :param role_me: role_me of 'Network_controller', adds <network> to the roles of the specified tc
    :param notifications: possible notifications, see [__Notifier__](Notifier.md)
    :param IP_WAN: wan ip address
    :param gateway: lan gateway ip addr
    :param internet_lost: the virtual that will be raised if the internet is lost, there should be a ping device defined with ip_action=1 such as : 'Internet': Ping('8.8.8.8',ip_action=1)
    :param internet_ping_repeat: the frequency that the internet_ping object will be inserted in every Ping series
    :param internet_ping_name: the name of the Ping('8.8.8.8',ip_action=1) object that must be defined somewhere
    :param ntp_server: ntp server ip addr
    :param power_ok: the input to be connected with the grid, obviously this things_controller should be connected to a battery
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'internet_lost': '', 'internet_ok': '', 'network': '', 'ping_lost': '', 'ping_ok': ''}
    :type IP_WAN:  ip
    :type gateway:  ip
    :type internet_lost:  Virtual
    :type internet_ping_repeat:  int
    :type internet_ping_name:  str
    :type ntp_server:  ip
    :type power_ok:  Input
    :type fav:  str
    :type icon:  str
    '''
    pass

class Notifier:
    ''' Notifier in App

    Is the App to deliver all outgoing notifications to displays, buzzers, voice output or any other notification channel defined and available through a driver

    - **parameters** and **types**

    :param role_me: role_me of 'Notifier', adds <notifier> to the roles of the specified tc
    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param buzzers: list of buzzer(s) that go off when notification is played
    :param do_say: = virtual, when reset, sound will not play and the sound request is ignored (unless No_Matter_What)
    :param do_buzzers: = virtual, when reset, buzzers stay silent (unless No_Matter_What)
    :param msg_dpls: things_controllers that will act as message displays, f.i. to be place next to the television
    :param tts_tags: tags that work like formatting in strings in python
    :param tts_port: port for the http tts file web services, choose not to interfere with other ports such as the hue emulation port
    :param tts_request: accepted web requests, this string is a python3 format string and should contain {ip}, {port} and {wav_file} keyword
    :param tts_volume: on a scale of 100
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'say_log': '', 'timers': ''}
    :type buzzers:  ['Output']
    :type do_say:  Virtual
    :type do_buzzers:  Virtual
    :type msg_dpls:  data_list
    :type tts_tags:  data_dict
    :type tts_port:  int
    :type tts_request:  str
    :type tts_volume:  int
    :type fav:  str
    :type icon:  str
    '''
    pass

class Scenes_app:
    ''' Scenes_app in App

    TBI/Scenes App, containing scenes that can be triggered in a calendar, by sms, by email, by twitter, by IFTTT, by Vera, by UDP, by TCP.  The scene id's are the key for the feeder to know what to do when the event_id is received through one of the feeder's channels

    - **parameters** and **types**

    :param role_me: role_me of 'Scenes_app', adds <scenes> to the roles of the specified tc
    :param do_scenes: = virtual, when reset, scenes will be ignored as are triggers (unless No_Matter_What)
    :param scenes: TBI/a dictionary of a list of commands that will be run in sequence, just like access_scenes in Access_manager
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type do_scenes:  Virtual
    :type scenes:  dict
    :type fav:  str
    :type icon:  str
    '''
    pass

class Security_manager:
    ''' Security_manager in App

    This App defines all the security settings and notifications that all security systems inherit

    - **parameters** and **types**

    :param role_me: role_me of 'Security_manager', adds <security> to the roles of the specified tc
    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'alarm_intrusion': '', 'alarm_loop': '', 'alarm_stopped': '', 'armed_dws_open': '', 'burglar': '', 'burglar_stopped': '', 'fire': '', 'fire_stopped': '', 'panic': '', 'panic_stopped': '', 'security_actuals': '', 'security_history': '', 'security_warn': '', 'tamper': '', 'tamper_stopped': '', '{room}.alarm': '', '{room}.burglar': '', '{room}.dw': '', '{room}.fire': ''}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Site_settings:
    ''' Site_settings in App

    Defines the geographical location (needed for sunset and sunrise), the email names used and some site specific parameters such as currency and temperature scale

    - **parameters** and **types**

    :param role_me: role_me of 'Site_settings', adds <key_data> to the roles of the specified tc
    :param EMAIL_groups: dictionary of email lists
    :param EMAIL_other: secondary email for the 'significant other's messages
    :param EMAIL_prime: primary email for all messages
    :param THINGS_account: TBI/Things account information such as email, password, cloud license, sharing (owner/renter), calendar, logs, ..
    :param currency: 1..3 letters
    :param degrees: °C or °F
    :param language: currently only 'English.eng' for English but could be Dutch.nl or French.fr
    :param latitude: -90..90
    :param longitude: -180..180
    :param site_id: the site name, is the name of the subdirectory used by site_tasker to manage the things_controllers on the site
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type EMAIL_groups:  data_dict
    :type EMAIL_other:  str
    :type EMAIL_prime:  str
    :type THINGS_account:  data_dict
    :type currency:  str
    :type degrees:  str
    :type language:  str
    :type latitude:  float
    :type longitude:  float
    :type site_id:  str
    :type fav:  str
    :type icon:  str
    '''
    pass

class Site_tasker:
    ''' Site_tasker in App

    the app that allows certain roles to assume a multi site role

    - **parameters** and **types**

    :param role_me: role_me of 'Site_tasker', adds <system> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Things_additions:
    ''' Things_additions in App

    Some Apps have something to do with specific things (such as a sirens_test with an Alarm_siren) or you need to define an App that collects data for every thing defined, then this App is the one to use

    - **parameters** and **types**

    :param items: Some Apps have something to do with specific things (such as a sirens_test with an Alarm_siren) or you need to define an App that collects data for every thing defined, then this App is the one to use
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type items:  data_dict
    :type fav:  str
    :type icon:  str
    '''
    pass

class Things_forensics:
    ''' Things_forensics in App

    Collects and reports cumulative data of all Things for a 24 hours period and assigns to every things_controller access to updated status reports linked to its role

    - **parameters** and **types**

    :param role_me: role_me of 'Things_forensics', adds <things_forensics> to the roles of the specified tc
    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param web_interface: will the output of every html generated file also be made available on port xx by every pi
    :param web_port: port for the http web services
    :param web_request: is the python3 format file and should contain the keywords {ip}, {port}, {file_req}
    :param web_secret: (currently disabled) if an empty string, then the web_secret defaults to the secret_key of ifttt_driver
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'cumuls': 'when this report runs'}
    :type web_interface:  bool
    :type web_port:  int
    :type web_request:  str
    :type web_secret:  str
    :type fav:  str
    :type icon:  str
    '''
    pass

class Things_sync:
    ''' Things_sync in App

    The process of ensuring that the as_is and to_be state of a Thing is there where it needs to be for the system to work as a whole

    - **parameters** and **types**

    :param role_me: role_me of 'Things_sync', adds <system> to the roles of the specified tc
    :param ws_port: port for the web_socket services
    :param ws_url: url for the web_socket services, must contain ip and port formatters
    :param UDP_port: port for the http UDP things_sync service, used on special authority such as master and vera tc's
    :param TCP_port: port for the http TCP things_sync service
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type ws_port:  int
    :type ws_url:  str
    :type UDP_port:  int
    :type TCP_port:  int
    :type fav:  str
    :type icon:  str
    '''
    pass

class Wincover_manager:
    ''' Wincover_manager in App

    Manages and contain options for the defined Door and Window coverings

    - **parameters** and **types**

    :param role_me: role_me of 'Wincover_manager', adds <wincover> to the roles of the specified tc
    :param raining_wc: Input device, active when the sensor is wet.  There is a small heater that dries the sensor, to become inactive when it is dry
    :param sun_light_switch: Input device to monitor light strength level and flip a switch if it is strong enough
    :param sun_light_wc: is an analog light sensor with output 0..10V
    :param wind_speed_wc: an input that generates counter data, the input must allow for counter mode
    :param wind_switch: Input device to monitor wind strength level and flip a switch if it is too strong
    :param winter_months: number of the months list with default winter mode
    :param C_outdoor_wc: an outside temp sensor
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type raining_wc:  Input
    :type sun_light_switch:  Input
    :type sun_light_wc:  Sensor
    :type wind_speed_wc:  Wind_speed
    :type wind_switch:  Input
    :type winter_months:  data_list
    :type C_outdoor_wc:  Sensor
    :type fav:  str
    :type icon:  str
    '''
    pass

class Room:
    ''' Room in Place

    This defines a room and contains room specific information

    - **parameters** and **types**

    :param say: verbose name of the place and is thus used with the assistant
    :param contents: what is inside the room
    :param room_virtuals: Room Virtuals are prescribed in their structure and store information about room occupancy aspects such as if the room is in use or not.  These settings can be influenced by other virtuals such that you can build user interface panels easily as in the examples
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type say:  str
    :type contents:  list
    :type room_virtuals:  {'role_me': 'm.clim', '{room}^is_locked': {'doc': 'is the room locked, all doors and windows closed?', 'insert_kws': {'descr': 'Room Locked?'}, 'optional': False, 'type': 'Virtual'}, '{room}^is_occupied': {'doc': 'is the occupied or abandoned, if abandoned then ^do_lights_off for lights and ^clim_on climatizing to save energy when is_occupied becomes inactive', 'insert_kws': {'descr': 'Room Occupied?'}, 'optional': True, 'type': 'Virtual'}}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Place:
    ''' Place

    This defines a place and contains place specific information

    - **parameters** and **types**

    :param say: verbose name of the place and is thus used with the assistant
    :param contents: what is inside the place
    :param room_virtuals: Room Virtuals are prescribed in their structure and store information about room occupancy aspects such as if the room is in use or not.  These settings can be influenced by other virtuals such that you can build user interface panels easily as in the examples
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type say:  str
    :type contents:  list
    :type room_virtuals:  {'role_me': 'm.clim', '{room}^is_locked': {'doc': 'is the room locked, all doors and windows closed?', 'insert_kws': {'descr': 'Room Locked?'}, 'optional': False, 'type': 'Virtual'}, '{room}^is_occupied': {'doc': 'is the occupied or abandoned, if abandoned then ^do_lights_off for lights and ^clim_on climatizing to save energy when is_occupied becomes inactive', 'insert_kws': {'descr': 'Room Occupied?'}, 'optional': True, 'type': 'Virtual'}}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Access_ways:
    ''' Access_ways in App_plc

    Define a list or a dict of one or multiple instances of Access_point or Access_trigger

    - **parameters** and **types**

    :param items: Define a list or a dict of one or multiple instances of Access_point or Access_trigger
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type items:  ['Access_point', 'Access_trigger']
    :type fav:  str
    :type icon:  str
    '''
    pass

class Cameras:
    ''' Cameras in App_plc

    Defining IP camera's and camera groups. Pictures will be taken at specified events through notifications and the camera group memberships

    - **parameters** and **types**

    :param items: Defining IP camera's and camera groups. Pictures will be taken at specified events through notifications and the camera group memberships
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type items:  *Camera
    :type fav:  str
    :type icon:  str
    '''
    pass

class Climate:
    ''' Climate in App_plc

    Defines the valves, sensors, climate devices such as heaters, coolers, ventilation and humidification regulators and there settings in sleep, away, holiday or day mode

    - **parameters** and **types**

    :param notifications: extensive list of notifications and they overrule what is defined in the climate_manager APP, see [__Notifier__](Notifier.md)
    :param clim_makers: clim_SW (switch) is a binary on/off climate switch, the better word is a valve.  you can add a temperature sensor which measures the passing through cooling or heating liquids.  clim_SP is a climate device that has a (temperature) set-point setting, it is therefore an analog device. clim_DM is a climate dimmer, a better word would be a mortised valve.
    :param clim_sensors: the sensor of the room measuring '%H','Lux','mmB','dP°C','CO2','CO'..., or a a binary classical thermostat = sensor_switch
    :param clim_targets: a dictionary of {warm_sp,cold_sp,vent_sp,humid_sp} dictionaries with a set-point string that can be a preset or a dictionary with detailed °C,%H,%V statements based on time of day, home occupancy, comfort settings
    :param room_is_priority: rooms with room_is_priority climate control get dealt with before all the rest when there are a lot of rooms needing energy.  This can be useful returning home in winter after holiday, give room_is_priority to living and sleeping rooms
    :param room_virtuals: Room Virtuals are prescribed in their structure and stores information about room aspects such as if climatisation is enabled, preferences (comfort, economy).  These settings can be influenced by other virtuals such that you can build user interface panels easily as in the examples
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param my_assistant: a flag if voice (alexa) can activate this thing
    :type notifications:  {'{room}_clim_on_0': 'climate for the room is disabled', '{room}_clim_on_1': 'climate for the room is enabled', '{room}_comfort_0': 'climate comfort mode for the room is disabled', '{room}_comfort_1': 'climate comfort mode for the room is enabled', '{room}_economy_0': 'climate economy mode for the room is disabled', '{room}_economy_1': 'climate economy mode for the room is enabled'}
    :type clim_makers:  ['Clim_SW', 'Clim_SP', 'Clim_DM', 'Clim_ANY']
    :type clim_sensors:  ['Sensor', 'Sensor_switch']
    :type clim_targets:  data_dict
    :type room_is_priority:  bool
    :type room_virtuals:  {'role_me': 'm.clim', '{room}^air_ok': {'doc': 'is the air in the room ok', 'i_read': ['!', '°C', '%H', '%L', 'Lux'], 'insert_kws': {'descr': 'Room Air Quality ok?'}, 'optional': True, 'type': 'Virtual'}, '{room}^clim_on': {'doc': 'is the room climatised', 'init_state': 1, 'insert_kws': {'descr': 'Room Climatised?'}, 'type': 'Virtual'}, '{room}^clim_pref': {'doc': 'current climate preference, Economy, Normal or Comfort setting, automatically created when clim_sensors exist that read °C', 'i_read': ['°C'], 'init_state': 0, 'insert_kws': {'short': 'ClimPref?', 'descr': 'Room Climate Preference', 'descr_range': 'Economy,Standard,Comfort', 'digital_range': '-1,0,1'}, 'optional': False, 'type': 'Virtual_R'}, '{room}^comfort_offset': {'doc': 'is the °C offset for comfort mode for the room, automatically created when clim_sensors exist that read °C', 'i_read': ['°C'], 'init_state': 0, 'insert_kws': {'descr': 'Comfort Offset °C', 'i_read': '°C'}, 'optional': True, 'type': 'Virtual_A'}, '{room}^economy_offset': {'doc': 'is the °C offset for economy mode for the room, automatically created when clim_sensors exist that read °C', 'i_read': ['°C'], 'init_state': 0, 'insert_kws': {'descr': 'Economy Offset °C', 'i_read': '°C'}, 'optional': True, 'type': 'Virtual_A'}, '{room}^humid_ok': {'doc': 'is the humidity of the room ok, automatically created when clim_sensors exist that read %H', 'i_read': ['%H'], 'insert_kws': {'descr': 'Room Humidity above target?'}, 'optional': True, 'type': 'Virtual'}, '{room}^humid_soll': {'doc': 'is the target humidity for the room, automatically created when clim_sensors exist that read %H', 'i_read': ['%H'], 'insert_kws': {'descr': 'Room Humidity Target', 'i_read': '%H'}, 'optional': True, 'type': 'Virtual_A'}, '{room}^light_ok': {'doc': 'is the luminosity of the room ok, automatically created when clim_sensors exist that read %L', 'i_read': ['%L', 'Lux'], 'insert_kws': {'descr': 'Room Luminosity above target?'}, 'optional': True, 'type': 'Virtual'}, '{room}^light_soll': {'doc': 'is the target light intensity for the room, automatically created when clim_sensors exist that read %L', 'i_read': ['%L', 'Lux'], 'insert_kws': {'descr': 'Room Light Target', 'i_read': '%L'}, 'optional': True, 'type': 'Virtual_A'}, '{room}^temp_ok': {'doc': 'is the temperature of the room ok, automatically created when clim_sensors exist that read °C', 'i_read': ['°C'], 'insert_kws': {'descr': 'Room Temperature above target?'}, 'optional': True, 'type': 'Virtual'}, '{room}^temp_soll': {'doc': 'is the target temperature for the room, automatically created when clim_sensors exist that read °C', 'i_read': ['°C'], 'insert_kws': {'descr': 'Room Temperature Target', 'i_read': '°C'}, 'optional': True, 'type': 'Virtual_A'}, '{room}^vent_soll': {'doc': 'is the target ventilation % for the room', 'insert_kws': {'descr': 'Room Ventilation Target'}, 'optional': True, 'type': 'Virtual_A'}}
    :type fav:  str
    :type icon:  str
    :type my_assistant:  bool
    '''
    pass

class Climate_system:
    ''' Climate_system in App_plc

    Climate Systems are typically multi room systems that drive multiple makers in multiple rooms with a central energy source such as a boiler and a pump to drive the energy around. This opposed to solo makers, which impact a climate just in one room and do not have not a multi system to back them. This App controls boilers, pumps, hvac devices in a classical radiator or underfloor heating (or combined) and everything else to give you excellent climate comfort given the context of comfort, standard or economy, the rooms that are in scope and the home occupancy, normal day, away, sleeping or on holiday

    - **parameters** and **types**

    :param role_me: role_me of 'Climate_system', adds <m.clim> to the roles of the specified tc
    :param air_removal: when active, the pump and boiler are automatically stopped and all valves are opened to allow air removal in optimal circumstances
    :param clim_SW_periodic_on: is the long idle activation for the clim_SW, the climate makers switches
    :param production: climate production devices such as gas/electricity boilers, heaters
    :param storage: climate storage devices such as hot water tanks
    :param transport: climate transport devices such as pumps, valves, motor valves
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type air_removal:  Virtual
    :type clim_SW_periodic_on:  Virtual
    :type production:  ['Clim_energy_SW', 'Clim_energy_DM', 'Input']
    :type storage:  ['Clim_SW', 'Clim_SP', 'Clim_DM', 'Clim_ANY']
    :type transport:  ['Output', 'Motor']
    :type fav:  str
    :type icon:  str
    '''
    pass

class Control:
    ''' Control in App_plc

    Generic Motor and Output setting such as swimpool pumps, wine cellar temperatures and any other things to control

    - **parameters** and **types**

    :param items: Generic Motor and Output setting such as swimpool pumps, wine cellar temperatures and any other things to control
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param my_assistant: a flag if voice (alexa) can activate this thing
    :type items:  ['Output', 'Motor', 'Switch']
    :type fav:  str
    :type icon:  str
    :type my_assistant:  bool
    '''
    pass

class Doorbell:
    ''' Doorbell in App_plc

    Most doorbells drive a bell button signal and have a way to signal agreement to open or lock one or more doors.  You can also declare a doorbell inside a door.

    - **parameters** and **types**

    :param role_me: role_me of 'Doorbell', adds <doorbell> to the roles of the specified tc
    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param ring_button: the bell button
    :param close_cmd: the 'close the door' pulse from the doorbell that can trigger doors or events
    :param open_cmd: the 'open the door' pulse from the doorbell that can trigger doors or events
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'ring': 'when the bell button is pressed', 'ring_away': 'when the bell button is pressed when home_occupation is away'}
    :type ring_button:  Input
    :type close_cmd:  Input
    :type open_cmd:  Input
    :type fav:  str
    :type icon:  str
    '''
    pass

class Doors:
    ''' Doors in App_plc

    A door? Is it not a simple input that states if the door is closed or not? A door can have a raft of method_things including all types of notifications, lights or triggers to open or close the door. To name a few method_things; optical beams to open or close the door, light to open, to close, a light when opening or closing or a night light. Or a timer on the open or close duration that triggers something. Or to define which area the door/window gives access to which is used in the security App

    - **parameters** and **types**

    :param items: A door? Is it not a simple input that states if the door is closed or not? A door can have a raft of method_things including all types of notifications, lights or triggers to open or close the door. To name a few method_things; optical beams to open or close the door, light to open, to close, a light when opening or closing or a night light. Or a timer on the open or close duration that triggers something. Or to define which area the door/window gives access to which is used in the security App
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type items:  *Door
    :type fav:  str
    :type icon:  str
    '''
    pass

class Home_utilities:
    ''' Home_utilities in App_plc

    Measures and reports utility consumption for heating, cooling, cooking, water, ... by reading utility meters and sensors.  It also reports solar and wind energy production and consumption and recharge of the home battery.

    - **parameters** and **types**

    :param role_me: role_me of 'Home_utilities', adds <m.clim> to the roles of the specified tc
    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param consumers: is a dictionary of consumers which counts when something is heating, taking energy, such as cooking, room heating or hot water tub.  CURRENTLY NOT IMPLEMENTED
    :param meters: is a dictionary of meters which counts when something is heating, taking energy, such as cooking, room heating or hot water tub.  CURRENTLY NOT IMPLEMENTED
    :param producers: is a dictionary of utility producers which generate water, electricity (solar panels), gas.  CURRENTLY NOT IMPLEMENTED
    :param sensors: is a dictionary of sensors which measures when something is heating, taking energy, such as cooking, room heating or hot water tub.  CURRENTLY NOT IMPLEMENTED
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'power': '', 'power_cam_shot': ''}
    :type consumers:  ['Utility_consumers']
    :type meters:  ['Utility_meter', 'Utility_pulse_meter', 'Flow_meter']
    :type producers:  ['Utility_producers']
    :type sensors:  ['Sensor']
    :type fav:  str
    :type icon:  str
    '''
    pass

class Ip_ping:
    ''' Ip_ping in App_plc

    Register network devices with special parameters for non pingable items and 'special' ip addresses. Devices defined with their ip address such as sonos, camera's and things_controllers are automatically added to the ip_ping list

    - **parameters** and **types**

    :param items: Register network devices with special parameters for non pingable items and 'special' ip addresses. Devices defined with their ip address such as sonos, camera's and things_controllers are automatically added to the ip_ping list
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type items:  *Ping
    :type fav:  str
    :type icon:  str
    '''
    pass

class Irrigation_points:
    ''' Irrigation_points in App_plc

    Irrigation point for water delivery to plants, with the normalized duration irrigation time in minutes

    - **parameters** and **types**

    :param items: Irrigation point for water delivery to plants, with the normalized duration irrigation time in minutes
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type items:  *Irr
    :type fav:  str
    :type icon:  str
    '''
    pass

class Irrigation_system:
    ''' Irrigation_system in App_plc

    Interface to the garden irrigation pump(s), activation/deactivation buttons and the watering valves

    - **parameters** and **types**

    :param role_me: role_me of 'Irrigation_system', adds <irr> to the roles of the specified tc
    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param dry_days_max: max number of days without rain to have irrigation (zaps remaining rain decay).  It is very difficult to estimate rain infiltration and having a cut off helps..
    :param irr_act_button: the button to press to activate the irrigation, overriding winter shutdown conditions.  A long press (> 2 secs) cancels the irrigation, a short press stops watering the active point, and moves to the next watering point. 
    :param irr_all_out_dg: if outside temp goes below this value, the pump is shutdown and all valves opened
    :param irr_daily_at: daily irrigation trigger time, clock is checked every minute - do not change formatting 'hh:mm' in 24 hour format, also alternatively google calendar can be used to irrigation trigger start
    :param irr_deact_button: the button to press to cancel irrigation
    :param irr_fcst_min_dg: day low temp forecast, below this value, no irrigation
    :param irr_flow_sensor: a irrigation water flow sensor, a feedback to working or faulty irrigation because the script can check when water should or should not flow.  The check happens at the first watering point
    :param irr_flow_meter: a irrigation water flow meter, measuring water consumption with a hall effect sensor
    :param irr_time_base: time in minutes, the basis irrigation time used for rain decay adjustment, do not change
    :param irr_water_supply: the output(s) to switch the pump
    :param irr_water_valve: the output(s) to the main water valve(s)
    :param winter_months: number of the month list with default winter mode
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'irr_cancelled': '', 'irr_completed': '', 'irr_depressurised': '', 'irr_flow_nok': '', 'irr_freezing': '', 'irr_ignored': '', 'irr_rain_decay': 'merges rain duration plus previous rain decay and highest temperature today into a new, equivalent, rain duration', 'irr_new_time': '', 'irr_rain_forecast': '', 'irr_soil_wet': '', 'irr_started': '', 'irr_too_cold': '', 'irr_too_wet': '', 'irr_winter_mode': ''}
    :type dry_days_max:  int
    :type irr_act_button:  Button
    :type irr_all_out_dg:  int
    :type irr_daily_at:  str
    :type irr_deact_button:  Button
    :type irr_fcst_min_dg:  int
    :type irr_flow_sensor:  Input
    :type irr_flow_meter:  Flow_meter
    :type irr_time_base:  int
    :type irr_water_supply:  Output
    :type irr_water_valve:  Output
    :type winter_months:  data_list
    :type fav:  str
    :type icon:  str
    '''
    pass

class Lights:
    ''' Lights in App_plc

    All types of light, dimmable and binary with a special option to have toggle lights with a light sensor

    - **parameters** and **types**

    :param room_lights: None
    :param room_virtuals: Room Virtuals are prescribed in their structure and store information about room light aspects such as if any or all the lights are on and virtuals which can alter the lights.  These settings can be influenced by other virtuals such that you can build user interface panels easily as in the examples
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param my_assistant: a flag if voice (alexa) can activate this thing
    :type room_lights:  ['Dimmer', 'Output', 'Light', 'Color_light', 'Dim_light', 'Motor']
    :type room_virtuals:  {'role_me': 'light', '{room}^do_lights_off': {'doc': 'make all the lights off in the room?', 'insert_kws': {'descr': 'Cmd Room Dark', 'duration': 1}, 'optional': True, 'type': 'Virtual'}, '{room}^do_lights_on': {'doc': 'make all the lights on in the room?', 'insert_kws': {'descr': 'Cmd All Room Lights On', 'duration': 1}, 'optional': True, 'type': 'Virtual'}, '{room}^is_any_light_off': {'doc': 'is any light off in the room?', 'insert_kws': {'descr': 'Any Room Light Off?'}, 'optional': True, 'type': 'Virtual'}, '{room}^is_any_light_on': {'doc': 'is any light on in the room?', 'insert_kws': {'descr': 'Any Room Light On?'}, 'optional': True, 'type': 'Virtual'}}
    :type fav:  str
    :type icon:  str
    :type my_assistant:  bool
    '''
    pass

class Mailbox_alert:
    ''' Mailbox_alert in App_plc

    To notify incoming and outgoing regular post mail through a magnetic or optical switch in the mailbox

    - **parameters** and **types**

    :param role_me: role_me of 'Mailbox_alert', adds <mail> to the roles of the specified tc
    :param mail_in: the input to register incoming post mail
    :param mail_out: the input to register post mail that is being removed
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type mail_in:  Input
    :type mail_out:  Input
    :type fav:  str
    :type icon:  str
    '''
    pass

class Monitor:
    ''' Monitor in App_plc

    Device monitoring such as waste water levels, wine cellar temperatures and any other things data to watch and to notify if set boundaries are crossed

    - **parameters** and **types**

    :param items: Device monitoring such as waste water levels, wine cellar temperatures and any other things data to watch and to notify if set boundaries are crossed
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type items:  ['Input', 'Sensor', 'Sensor_switch']
    :type fav:  str
    :type icon:  str
    '''
    pass

class Music_players:
    ''' Music_players in App_plc

    Any of the music_players supported such as sonos

    - **parameters** and **types**

    :param items: Any of the music_players supported such as sonos
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type items:  *Sonos
    :type fav:  str
    :type icon:  str
    '''
    pass

class Phone_dialer:
    ''' Phone_dialer in App_plc

    This is the driver to an old fashioned phone dialer to deliver preset voice messages in case of fire, alarm or loss of internet or power

    - **parameters** and **types**

    :param role_me: role_me of 'Phone_dialer', adds <phone> to the roles of the specified tc
    :param pho_input: Dialer input virtual, the dial sequence is stopped with key 5 on the receiver phone
    :param pho_say_burglar: Dialer to invoke in case of a burglar alarm, the dial sequence is stopped with key 5 on the receiver phone
    :param pho_say_fire: Dialer to invoke in case of fire, the dial sequence is stopped with key 5 on the receiver phone
    :param pho_say_internet_lost: Dialer to invoke in case the internet is lost, the dial sequence is stopped with key 5 on the receiver phone
    :param pho_say_power_lost: Dialer to invoke in case of electricity power interruption, the dial sequence is stopped with key 5 on the receiver phone
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type pho_input:  Input
    :type pho_say_burglar:  Output
    :type pho_say_fire:  Output
    :type pho_say_internet_lost:  Output
    :type pho_say_power_lost:  Output
    :type fav:  str
    :type icon:  str
    '''
    pass

class Security:
    ''' Security in App_plc

    This App is defined per room and contains the Fire/Alarm detectors and sirens and the zones linked to the place or room

    - **parameters** and **types**

    :param notifications: extensive list of notifications, see [__Notifier__](Notifier.md)
    :param alarm_detectors: list (name is generated) or dictionary (you give name) of Alarm detector's
    :param fire_detectors: list (name is generated) or dictionary (you give name) of Fire detector's
    :param room_virtuals: Room Virtuals are prescribed in their structure and store information about room security aspects such as if the room is closed or secure.  These settings can be influenced by other virtuals such that you can build user interface panels easily as in the examples
    :param sirens: list (name is generated) or dictionary (you give name) of Alarm_siren's
    :param zone: one of the predefined zones
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type notifications:  {'{room}_alarm': '', '{room}_burglar': '', '{room}_dw': '', '{room}_fire': ''}
    :type alarm_detectors:  *Alarm_detector
    :type fire_detectors:  *Fire_detector
    :type room_virtuals:  {'role_me': 'security', '{room}^is_alarm': {'doc': 'are the room alarm detectors flagging alarm?', 'insert_kws': {'descr': 'Room in Alarm?'}, 'optional': True, 'type': 'Virtual'}, '{room}^is_fire': {'doc': 'are the room fire_detectors flagging fire?', 'insert_kws': {'descr': 'Room in Fire?'}, 'optional': True, 'type': 'Virtual'}, '{room}^is_secure': {'doc': 'is the room secure, covered by being armed?', 'insert_kws': {'descr': 'Room Secured?'}, 'optional': False, 'type': 'Virtual'}}
    :type sirens:  *Alarm_siren
    :type zone:  valid_list
    :type fav:  str
    :type icon:  str
    '''
    pass

class Security_system:
    ''' Security_system in App_plc

    Advanced interface and definition of a security system, either stand alone or integrated as a master or slave subsystem. The role drives the alarm and fire detectors and the whole security logic

    - **parameters** and **types**

    :param role_me: role_me of 'Security_system', adds <security> to the roles of the specified tc
    :param blackout_mode: is for blocking new alarms after an alarm is reset and this for a given time
    :param daily_routine: to use as a copy virtual of is_day
    :param do_alarm: virtual to set the alarm
    :param do_arm_at_close: virtual to arm the alarm when the particular door closes
    :param do_arm_full: virtual to arm the always and partial zones without the eminent delay
    :param do_arm_full_req: virtual to arm the always and partial zones using the eminent delay
    :param do_arm_partial: virtual to arm the always zones but not the partial zones without eminent delay
    :param do_arm_partial_req: virtual to arm the always zones but not the partial zones with eminent delay
    :param do_burglar: virtual to set the burglar alarm
    :param do_fire: virtual to set the fire alarm
    :param do_panic: virtual to set the panic alarm
    :param do_tamper: virtual to set the tamper alarm
    :param do_unarm: virtual to unarm the alarm
    :param is_alarm: status virtual are we in alarm mode, either is_fire or is_burglar or is_tamper or is_panic
    :param is_alarm_eminent: alarm will set as 'alarm_delay' expires, triggered by entry_way item becoming inactive
    :param is_arm_eminent: arm will set as 'arm_delay' expires or exit_way item becomes active
    :param is_armed: status virtual are we armed either completely or without the partial zones
    :param is_armed_full: status virtual are we fully armed including the partial zones. In value_logic this virtual can be aliased by 'away'
    :param is_armed_partial: status virtual are we partially armed, so without the partial zones. In value_logic this virtual can be aliased by 'sleep'
    :param is_burglar: status virtual do we have a burglar alarm situation (uses zones and is_arm_eminent and is_alarm_eminent)
    :param is_fire: status virtual do we have a fire alarm situation (this gives immediate alarm)
    :param is_panic: status virtual do we have a panic alarm situation (this is a silent alarm type -> no sirens)
    :param is_tamper: status virtual do we have a tamper alarm situation (this gives immediate alarm, no is_alarm_eminent)
    :param light_alarm: light when an alarm has been triggered
    :param light_armed: light when alarm is armed
    :param light_armed_warn: warning light that alarm will become armed, during the arm_delay
    :param light_fire: light when fire alarm is activated 
    :param maintenance_mode: 0..3 ['OFF','Ignore Master','Ignore Slave','Silent_only']
    :param master_r_armed_always: the master system request us to arm the always zones
    :param master_r_armed_partial: the master system requests to arm the partial zones
    :param master_r_burglar: the master system requests to signal burglar alarm
    :param master_r_fire: the master system requests to signal fire alarm
    :param master_r_panic: the master system requests to signal panic alarm
    :param master_r_tamper: the master system requests to signal tamper alarm
    :param o_alarm: output is active during an alarm, either is_fire or is_burglar or is_tamper or is_panic
    :param o_armed: output is active when armed either full, either partial
    :param o_armed_full: output is active when armed fully
    :param o_armed_partial: output is active when armed partially
    :param o_burglar: output is active during a burglar alarm
    :param o_fire: output is active during fire alarm
    :param o_panic: output is active during a panic alarm
    :param o_tamper: output is active during a tamper alarm
    :param partial_zone_index: if multiple partial_zones_x (x=index) exist, then this virtual chooses the one to use
    :param safe_ways: a dict with exit_way, entry_way as keys for a list of devices to ignore on exit or cause alarm eminent on entry
    :param si_system_type: security system type: -1=slave, 0=whole, 1=master 
    :param slave_s_alarm: the slave is instructed to state alarm
    :param slave_s_arm_full: the slave is instructed to arm all the zones (this or the toggle should be present)
    :param slave_s_arm_full_t: the slave is instructed to arm all the zones (this or the toggle should be present)
    :param slave_s_arm_partial: the slave is instructed to arm the alarm except the partial zones (this or the toggle should be present)
    :param slave_s_arm_partial_t: the slave is instructed to arm the alarm except the partial zones (this or the toggle should be present)
    :param slave_s_burglar: the slave is instructed to state burglar
    :param slave_s_fire: the slave is instructed to state fire
    :param slave_s_panic: the slave is instructed to state panic
    :param slave_s_tamper: the slave is instructed to state tamper
    :param zones: a dict with ignore_zones, always_zones, partial_zones for a list of zones to ignore, always to arm, or not to arm if do_arm_partial
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type blackout_mode:  Virtual
    :type daily_routine:  Virtual
    :type do_alarm:  Virtual
    :type do_arm_at_close:  Virtual
    :type do_arm_full:  Virtual
    :type do_arm_full_req:  Virtual
    :type do_arm_partial:  Virtual
    :type do_arm_partial_req:  Virtual
    :type do_burglar:  Virtual
    :type do_fire:  Virtual
    :type do_panic:  Virtual
    :type do_tamper:  Virtual
    :type do_unarm:  Virtual
    :type is_alarm:  Virtual
    :type is_alarm_eminent:  Virtual
    :type is_arm_eminent:  Virtual
    :type is_armed:  Virtual
    :type is_armed_full:  Virtual
    :type is_armed_partial:  Virtual
    :type is_burglar:  Virtual
    :type is_fire:  Virtual
    :type is_panic:  Virtual
    :type is_tamper:  Virtual
    :type light_alarm:  Light
    :type light_armed:  Light
    :type light_armed_warn:  Light
    :type light_fire:  Light
    :type maintenance_mode:  Virtual_R
    :type master_r_armed_always:  Input
    :type master_r_armed_partial:  Input
    :type master_r_burglar:  Input
    :type master_r_fire:  Input
    :type master_r_panic:  Input
    :type master_r_tamper:  Input
    :type o_alarm:  Output
    :type o_armed:  Output
    :type o_armed_full:  Output
    :type o_armed_partial:  Output
    :type o_burglar:  Output
    :type o_fire:  Output
    :type o_panic:  Output
    :type o_tamper:  Output
    :type partial_zone_index:  Virtual_R
    :type safe_ways:  data_dict
    :type si_system_type:  Virtual_R
    :type slave_s_alarm:  Output
    :type slave_s_arm_full:  Output
    :type slave_s_arm_full_t:  Output
    :type slave_s_arm_partial:  Output
    :type slave_s_arm_partial_t:  Output
    :type slave_s_burglar:  Output
    :type slave_s_fire:  Output
    :type slave_s_panic:  Output
    :type slave_s_tamper:  Output
    :type zones:  data_dict
    :type fav:  str
    :type icon:  str
    '''
    pass

class Things_controllers:
    ''' Things_controllers in App_plc

    This structure defines a Things Controller such as 'Raspberry','Ubuntu','MAC_OS','Arduino','Vera','Hue','Ikea','Ow_eds','Unipi_Evok'

    - **parameters** and **types**

    :param items: This structure defines a Things Controller such as 'Raspberry','Ubuntu','MAC_OS','Arduino','Vera','Hue','Ikea','Ow_eds','Unipi_Evok'
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type items:  ['Raspi', 'Ubuntu', 'MAC_OS', 'Arduino', 'Vera', 'Hue', 'Ikea', 'Ow_eds', 'Unipi_Evok', 'Daikin', 'IP_Building', 'Loxone', 'Renson']
    :type fav:  str
    :type icon:  str
    '''
    pass

class Weather_station:
    ''' Weather_station in App_plc

    wunderground and darksky is used for the weather forecast, Netatmo weather station is used for the wind, rain and other semi real time data. The role involves the weather forecast, weather station (wind, rain, sunshine) and irrigation based on forecast.  Several direct input sensors are supported for rain, wind, temperature, humidity and soil moisture

    - **parameters** and **types**

    :param role_me: role_me of 'Weather_station', adds <weather> to the roles of the specified tc
    :param notifications: soil sensor is moist/dry, rain sensor raining,temp now going below/above zero, the weather station report, the weather forecast wunderground call failed or report succeeded. , see also [__Notifier__](Notifier.md)
    :param accu_weather_http: is the accu weather python3 http format string for obtaining a location key
    :param accu_weather_f: is the accu weather python3 http format string for obtaining a 5 days forecast
    :param accu_weather_key: accu weather key : see www.accuweather.com; this is the free key which is private to us and allows weather forecasts to be collected.  The site_id is used to obtain a location key and with that the weather forecast
    :param air_pressure: an analog pressure sensor mbar (milli bar)
    :param air_quality: an analog air sensor ppm (parts per million)
    :param darksky_http: darksky weather forecast, and longitude and latitude, see https://darksky.net/dev/
    :param darksky_secret: the darksky weather forecast secret, see https://darksky.net/dev/
    :param humidity: an analog humidity sensor 0..100% humidity
    :param rain_gauge: an input that generates counter data from the gauge, the input must allow for counter mode
    :param raining: input device, active when the sensor is wet.  There is a small heater that dries the sensor, to become inactive when it is dry
    :param soil_dry: Input device to monitor when the soil is dry and needs watering
    :param soil_moist_sensor: an analog moist sensor 0..100%
    :param sun_light: an analog light sensor 0..300.000 Lux, 0..100%
    :param wind_speed: an input that generates counter data from the wind-fan, the input must allow for counter mode, wind_gust is derived from wind_speed
    :param wunder_http: is the python3 format string with 2 formatters, where the first is the wunder_key, the second is wunder_location
    :param wunder_key: wunderground key : this is the free key which is private to us and allows weather forecasts to be collected
    :param wunder_location: wunderground location, see the website https://www.wunderground.com/
    :param C_outdoor: outside temperature sensor
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type notifications:  {'ws_frc_failed': '', 'ws_frc_report': '', 'ws_report': ''}
    :type accu_weather_http:  str
    :type accu_weather_f:  str
    :type accu_weather_key:  str
    :type air_pressure:  Sensor
    :type air_quality:  Sensor
    :type darksky_http:  str
    :type darksky_secret:  str
    :type humidity:  Sensor
    :type rain_gauge:  Rain_gauge
    :type raining:  Input
    :type soil_dry:  Input
    :type soil_moist_sensor:  Sensor
    :type sun_light:  Sensor
    :type wind_speed:  Wind_speed
    :type wunder_http:  str
    :type wunder_key:  str
    :type wunder_location:  str
    :type C_outdoor:  Sensor
    :type fav:  str
    :type icon:  str
    '''
    pass

class Windows:
    ''' Windows in App_plc

    A door? Is it not a simple input that states if the door is closed or not? A door can have a raft of method_things including all types of notifications, lights or triggers to open or close the door. To name a few method_things; optical beams to open or close the door, light to open, to close, a light when opening or closing or a night light. Or a timer on the open or close duration that triggers something. Or to define which area the door/window gives access to which is used in the security App

    - **parameters** and **types**

    :param items: A door? Is it not a simple input that states if the door is closed or not? A door can have a raft of method_things including all types of notifications, lights or triggers to open or close the door. To name a few method_things; optical beams to open or close the door, light to open, to close, a light when opening or closing or a night light. Or a timer on the open or close duration that triggers something. Or to define which area the door/window gives access to which is used in the security App
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type items:  ['Window', 'Win_cover']
    :type fav:  str
    :type icon:  str
    '''
    pass

class Access:
    ''' Access

    Access description, works also for the derived classes

    - **parameters** and **types**

    :param rights: the rights is a dict with the names of the Access_points and the scene that is to be called.  An entry 'rights_template':'name of template' will be substituted with the entries of that rights_template
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type rights:  data_dict
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Ble_gw_th:
    ''' Ble_gw_th

    is an internal generated thing for every beacon for every gateway to hold the rssi value or zero when lost

    - **parameters** and **types**

    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param threshold: the minimum value that an analog input must change before the value is considered changed
    :param play: the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on'
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    :type threshold:  float
    :type play:  tuple:virtual_tuples
    '''
    pass

class Access_point:
    ''' Access_point

    Access points are devices that read iButtons, smart cards, finger print scanners, facial recognition devices and emit an access key string to the security guardian that is interpreted for access rights and consequential access scene execution.  Access controllers follow the propriety data exchange protocol with the security things_controller and have a direction: enter, exit or select

    - **parameters** and **types**

    :param method_things: special methods of this thing, mostly realised through things
    :param direction: is the direction of the access point : exit/entry or both
    :param notifications: access controllers nty's, see [__Notifier__](Notifier.md)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type method_things:  {'access_green': {'doc': {'descr': 'is the led acceptance light to signal that the access registration was accepted', 'short': 'access_green'}, 'optional': True, 'type': 'Light'}, 'access_red': {'doc': {'descr': 'is the led refusal light to signal that the access registration was rejected', 'short': 'access_red'}, 'optional': True, 'type': 'Light'}}
    :type direction:  valid_list
    :type notifications:  {'active': 'when payload is an access code', 'inactive': 'when payload is empty', 'access_try': 'when access through a code is requested'}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Access_trigger:
    ''' Access_trigger

    Access trigger are inputs and when activated, they submit an access_scene id to the security guardian for scene processing

    - **parameters** and **types**

    :param method_things: special methods of this thing, mostly realised through things
    :param direction: is the direction of the access point : exit/entry or both
    :param access_scene: is the direction of the access point : exit/entry or both
    :param notifications: access trigger nty's, see [__Notifier__](Notifier.md)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type method_things:  {'access_green': {'doc': {'descr': 'is the led acceptance light to signal that the access trigger was accepted', 'short': 'access_green'}, 'optional': True, 'type': 'Light'}, 'access_red': {'doc': {'descr': 'is the led refusal light to signal that the access trigger was rejected', 'short': 'access_red'}, 'optional': True, 'type': 'Light'}}
    :type direction:  valid_list
    :type access_scene:  str
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Alarm_detector:
    ''' Alarm_detector

    Input description, works also for the derived classes

    - **parameters** and **types**

    :param detector_type: is the detector type such as burglar, tamper, alarm,..
    :param notifications: the notifications for inputs, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type detector_type:  valid_list
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Alarm_siren:
    ''' Alarm_siren

    Alarm_siren description, works also for the derived classes

    - **parameters** and **types**

    :param notifications: the notifications for Alarm_siren, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param method_things: special methods of this thing, mostly realised through things
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type method_things:  {'activate_button': {'doc': {'descr': 'activates the output if inactive', 'short': 'activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'de_activate_button': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'on_off_relay': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Output', 'Light']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}, 'toggle_button': {'doc': {'descr': 'is an input to toggle the output state', 'short': 'toggle_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Button:
    ''' Button

    Input description, works also for the derived classes

    - **parameters** and **types**

    :param notifications: the notifications for inputs, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Camera:
    ''' Camera

    is a network function to check the presence of a thing through a ping

    - **parameters** and **types**

    :param ip_action: -
    :param spec_func: special function attribute
    :param cam_tpe: key in the Camera_driver dict cam_types
    :param file_id: 2 characted file id
    :param user: user name for the login
    :param pwd: password for the login
    :param notifications: the notifications for pings, see [__Notifier__](Notifier.md)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param ip: ip in the format of xx.xx.xx.xx
    :param port: ip port
    :param play: the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on'
    :type ip_action:  int
    :type spec_func:  str
    :type cam_tpe:  str
    :type file_id:  str
    :type user:  str
    :type pwd:  str
    :type notifications:  {'active': 'when payload is active', 'none': 'value of the Virtual is None', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    :type ip:  str
    :type port:  int
    :type play:  tuple:virtual_tuples
    '''
    pass

class Clim_ANY:
    ''' Clim_ANY

    Climate Anything, clim_ANY is a climate device that has a string setting and value can be set with value_logic.  For example fan direction could be something to define and hold here in combination with value_logic is this climate maker multi purpose friend

    - **parameters** and **types**

    :param method_things: special methods of this thing, mostly realised through things
    :param i_make: the type of environmental impact that this thing makes
    :param notifications: similar for the notifications for Sensors, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type method_things:  {'C_fluid': {'doc': {'descr': 'this measures the °C fluid temperature', 'short': '°C_fluid'}, 'optional': True, 'type': ['Sensor']}, 'C_in': {'doc': {'descr': 'this measures the °C fluid input temperature', 'short': '°C_in'}, 'optional': True, 'type': ['Sensor']}, 'C_out': {'doc': {'descr': 'this measures the °C fluid output temperature', 'short': '°C_out'}, 'optional': True, 'type': ['Sensor']}}
    :type i_make:  str
    :type notifications:  {'high': 'when payload reaches high', 'low': 'when payload reaches low', 'normal': 'when payload becomes lower than high or higher than low', 'active': 'when payload is non zero', 'inactive': 'when payload is zero', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    '''
    pass

class Clim_DM:
    ''' Clim_DM

    Climate Dimmer, clim_DM is a climate device that has a 0% to 100% setting and value can be set with value_logic.  Typically this is for 3 way or motorised valves that can be more opened automatically with the outside temperature as more hot water can be channeled through instead of being looped back.  Other purposes are in combination with i_make='wind','vent','fan' and in combination with value_logic is this climate maker multi purpose friend

    - **parameters** and **types**

    :param method_things: special methods of this thing, mostly realised through things
    :param notifications: similar for the notifications for Sensors, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param i_make: the type of environmental impact that this thing makes
    :param icon: icon file for this element
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param threshold: the minimum value that an analog input must change before the value is considered changed
    :type method_things:  {'C_fluid': {'doc': {'descr': 'this measures the °C fluid temperature', 'short': '°C_fluid'}, 'optional': True, 'type': ['Sensor']}, 'C_in': {'doc': {'descr': 'this measures the °C fluid input temperature', 'short': '°C_in'}, 'optional': True, 'type': ['Sensor']}, 'C_out': {'doc': {'descr': 'this measures the °C fluid output temperature', 'short': '°C_out'}, 'optional': True, 'type': ['Sensor']}}
    :type notifications:  {'high': 'when payload reaches high', 'low': 'when payload reaches low', 'active': 'when payload is non zero', 'normal': 'when payload becomes lower than high or higher than low', 'inactive': 'when payload is zero', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type i_make:  str
    :type icon:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    :type threshold:  float
    '''
    pass

class Clim_SP:
    ''' Clim_SP

    Climate Setpoint, Clim_SP is a climate device that has a (temperature) set-point setting, it is therefore an analog device

    - **parameters** and **types**

    :param method_things: special methods of this thing, mostly realised through things
    :param notifications: similar for the notifications for Sensors, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param i_make: the type of environmental impact that this thing makes
    :param icon: icon file for this element
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param threshold: the minimum value that an analog input must change before the value is considered changed
    :type method_things:  {'C_fluid': {'doc': {'descr': 'this measures the °C fluid temperature', 'short': '°C_fluid'}, 'optional': True, 'type': ['Sensor']}, 'C_in': {'doc': {'descr': 'this measures the °C fluid input temperature', 'short': '°C_in'}, 'optional': True, 'type': ['Sensor']}, 'C_out': {'doc': {'descr': 'this measures the °C fluid output temperature', 'short': '°C_out'}, 'optional': True, 'type': ['Sensor']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}}
    :type notifications:  {'deicing': 'temperature becomes positive', 'freezing': 'temperature becomes below zero', 'positive': 'when payload reaches positive or zero coming from a negative payload', 'negative': 'when payload reaches negative, coming from a positive payload', 'high': 'when payload reaches high', 'low': 'when payload reaches low', 'normal': 'when payload becomes lower than high or higher than low', 'active': 'when payload is not zero', 'inactive': 'when payload is zero', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type i_make:  str
    :type icon:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    :type threshold:  float
    '''
    pass

class Clim_SW:
    ''' Clim_SW

    Climate Switch, Clim_SW (switch) is a binary on/off climate switch such as an on/off valve.  you can add a temperature sensor which measures the passing through cooling or heating liquids

    - **parameters** and **types**

    :param method_things: special methods of this thing, mostly realised through things
    :param notifications: the notifications for outputs, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param i_make: the type of environmental impact that this thing makes
    :param icon: icon file for this element
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :type method_things:  {'C_fluid': {'doc': {'descr': 'this measures the °C fluid temperature', 'short': '°C_fluid'}, 'optional': True, 'type': ['Sensor']}, 'C_in': {'doc': {'descr': 'this measures the °C fluid input temperature', 'short': '°C_in'}, 'optional': True, 'type': ['Sensor']}, 'C_out': {'doc': {'descr': 'this measures the °C fluid output temperature', 'short': '°C_out'}, 'optional': True, 'type': ['Sensor']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}}
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type i_make:  str
    :type icon:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type duration:  int
    :type descr_01:  list-2
    '''
    pass

class Clim_energy_DM:
    ''' Clim_energy_DM

    Climate energy Dimmer, is a device that has a 0% to 100% setting and value can be set with value_logic.  Typically this is for heat/cool pump generation. Specify i_make.

    - **parameters** and **types**

    :param notifications: similar for the notifications for Sensors, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param method_things: special methods of this thing, mostly realised through things
    :param fav: is this a favorite element
    :param i_make: the type of environmental impact that this thing makes
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param value_app: app logic to determine the payload based programming logic and input parameters
    :param descr: free description field for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param threshold: the minimum value that an analog input must change before the value is considered changed
    :type notifications:  {'high': 'when payload reaches high', 'low': 'when payload reaches low', 'normal': 'when payload becomes lower than high or higher than low', 'active': 'when payload is non zero', 'inactive': 'when payload is zero', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type method_things:  {'activate_button': {'doc': {'descr': 'activates the output if inactive', 'short': 'activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'de_activate_button': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'on_off_relay': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Output', 'Light']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}, 'toggle_button': {'doc': {'descr': 'is an input to toggle the output state', 'short': 'toggle_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}}
    :type fav:  str
    :type i_make:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type value_app:  tuple:value_app_tuples
    :type descr:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    :type threshold:  float
    '''
    pass

class Clim_energy_SW:
    ''' Clim_energy_SW

    Climate energy Switch, is a binary on/off switch for gas or electricity heaters or coolers. Specify i_make.

    - **parameters** and **types**

    :param method_things: special methods of this thing, mostly realised through things
    :param notifications: the notifications for outputs, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param i_make: the type of environmental impact that this thing makes
    :param icon: icon file for this element
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param value_app: app logic to determine the payload based programming logic and input parameters
    :param descr: free description field for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :type method_things:  {'activate_button': {'doc': {'descr': 'activates the output if inactive', 'short': 'activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'de_activate_button': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'on_off_relay': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Output', 'Light']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}, 'toggle_button': {'doc': {'descr': 'is an input to toggle the output state', 'short': 'toggle_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}}
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type i_make:  str
    :type icon:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type value_app:  tuple:value_app_tuples
    :type descr:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type duration:  int
    :type descr_01:  list-2
    '''
    pass

class Color_light:
    ''' Color_light

    Color_light description, works also for the derived classes

    - **parameters** and **types**

    :param notifications: the notifications for Color_light, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param method_things: special methods of this thing, mostly realised through things
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param threshold: the minimum value that an analog input must change before the value is considered changed
    :param my_assistant: a flag if voice (alexa) can activate this thing
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type method_things:  {'activate_button': {'doc': {'descr': 'activates the output if inactive', 'short': 'activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'de_activate_button': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'on_off_relay': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Output', 'Light']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}, 'toggle_button': {'doc': {'descr': 'is an input to toggle the output state', 'short': 'toggle_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    :type threshold:  float
    :type my_assistant:  bool
    '''
    pass

class Dim_light:
    ''' Dim_light

    Dim_light description, works also for the derived classes

    - **parameters** and **types**

    :param notifications: the notifications for Dim_light, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param method_things: special methods of this thing, mostly realised through things
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param threshold: the minimum value that an analog input must change before the value is considered changed
    :param my_assistant: a flag if voice (alexa) can activate this thing
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type method_things:  {'activate_button': {'doc': {'descr': 'activates the output if inactive', 'short': 'activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'de_activate_button': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'on_off_relay': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Output', 'Light']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}, 'toggle_button': {'doc': {'descr': 'is an input to toggle the output state', 'short': 'toggle_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    :type threshold:  float
    :type my_assistant:  bool
    '''
    pass

class Dimmer:
    ''' Dimmer

    Dimmer description, works also for the derived classes such as Motor, Dim_light and Color_light

    - **parameters** and **types**

    :param notifications: the notifications for dimmers, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param method_things: special methods of this thing, mostly realised through things
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param threshold: the minimum value that an analog input must change before the value is considered changed
    :param my_assistant: a flag if voice (alexa) can activate this thing
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type method_things:  {'activate_button': {'doc': {'descr': 'activates the output if inactive', 'short': 'activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'de_activate_button': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'on_off_relay': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Output', 'Light']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}, 'toggle_button': {'doc': {'descr': 'is an input to toggle the output state', 'short': 'toggle_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    :type threshold:  float
    :type my_assistant:  bool
    '''
    pass

class Door:
    ''' Door

    Door and Window methods are the same

    - **parameters** and **types**

    :param notifications: door nty's, see [__Notifier__](Notifier.md)
    :param method_things: special methods of this thing, mostly realised through things
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param my_assistant: a flag if voice (alexa) can activate this thing
    :type notifications:  {'active': 'when payload is active', 'conflict_oc': 'error as door is registered to be open and closed at the same time', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications', 'open_max': 'door is open for the specified maximum duration', 'ring': 'when the doorbell is pressed', 'ring_away': 'when the doorbell is pressed when away', 'trigger': 'door is triggered', 'trigger_no': 'door is trigger but opening is refused'}
    :type method_things:  {'access': {'doc': {'descr': 'zone list where the door give access to', 'short': 'access'}, 'optional': True, 'type': 'data_list'}, 'beam2close': {'doc': {'descr': 'optical beam, if tripped the door closes after 3 seconds', 'short': 'beam2close'}, 'optional': True, 'type': 'Optical'}, 'beam2open': {'doc': {'descr': 'optical beam, if tripped the door opens if beam_can_open', 'short': 'beam2open'}, 'optional': True, 'type': 'Optical'}, 'beam_can_close': {'doc': {'descr': 'actually is not needed as a switch can be put in series with the optical close beam which is similar to a constantly interrupted beam', 'short': 'beam_can_close'}, 'optional': True, 'type': ['Switch', 'Optical', 'Virtual']}, 'beam_can_open': {'doc': {'descr': 'a switch that allows the optical open beam to work, it does not prevent ', 'short': 'beam_can_open'}, 'optional': True, 'type': ['Switch', 'Optical', 'Virtual']}, 'is_opened': {'doc': {'descr': 'f.i. a magnetic contact that registers that the door/window is fully opened', 'short': 'is_opened'}, 'optional': True, 'type': 'Input'}, 'keep_closed': {'doc': {'descr': 'all requests to open the dw are ignored', 'short': 'keep_closed'}, 'optional': True, 'type': ['Switch', 'Virtual']}, 'keep_opened': {'doc': {'descr': 'all requests to close the dw are ignored', 'short': 'keep_opened'}, 'optional': True, 'type': ['Switch', 'Virtual']}, 'light_deco': {'doc': {'descr': 'is on when the door is not closed', 'short': 'light_deco'}, 'optional': True, 'type': 'Light'}, 'light_green': {'doc': {'descr': 'is on when the door is fully open', 'short': 'light_green'}, 'optional': True, 'type': 'Light'}, 'light_night': {'doc': {'descr': 'is on when the f_night is on and till xx seconds after close', 'short': 'light_night'}, 'optional': True, 'type': 'Light'}, 'light_not_closed': {'doc': {'descr': 'is on when the door is not closed', 'short': 'light_not_closed'}, 'optional': True, 'type': 'Light'}, 'light_red': {'doc': {'descr': 'is on when the door is not closed and not fully open (door is moving)', 'short': 'light_red'}, 'optional': True, 'type': 'Light'}, 'light_warn': {'doc': {'descr': 'is on when the door is moving', 'short': 'light_warn'}, 'optional': True, 'type': 'Light'}, 'lights_off_at_close': {'doc': {'descr': "if this virtual is up and the door closes, then all the lights will go off in the room.The virtual is then 'consumed' and goes off", 'short': 'lights_off_at_close'}, 'optional': True, 'type': 'Virtual'}, 'lights_off_at_open': {'doc': {'descr': "if this virtual is up and the door opens, then all the lights will go on in the room.  The virtual is then 'consumed' and goes off", 'short': 'lights_off_at_open'}, 'optional': True, 'type': 'Virtual'}, 'lights_on_at_close': {'doc': {'descr': "if this virtual is up and the door closes, then all the lights will go on in the room. The virtual is then 'consumed' and goes off", 'short': 'lights_on_at_close'}, 'optional': True, 'type': 'Virtual'}, 'lights_on_at_open': {'doc': {'descr': "if this virtual is up and the door opens, then all the lights will go on in the room.  The virtual is then 'consumed' and goes off", 'short': 'lights_on_at_open'}, 'optional': True, 'type': 'Virtual'}, 'pulse2close': {'doc': {'descr': 'pulse to close the door', 'short': 'pulse2close'}, 'optional': True, 'type': 'Output'}, 'pulse2open': {'doc': {'descr': 'pulse to open the door', 'short': 'pulse2open'}, 'optional': True, 'type': 'Output'}, 'step2open_close': {'doc': {'descr': 'step pulse to close the door when door is open or open the door when the door is closed', 'short': 'step2open_close'}, 'optional': True, 'type': 'Output'}, 'ring_button': {'doc': {'descr': 'the bell button', 'short': 'door bell_button'}, 'optional': True, 'type': 'Input'}, 'cmd_close': {'doc': {'descr': "the 'close the door' command from the doorbell that can trigger doors or events. It activates pulse2close if the door/window is open and pulse2close is not active.", 'short': 'cmd_close from a doorbell'}, 'optional': True, 'type': 'Input'}, 'cmd_open': {'doc': {'descr': "the 'open the door' command from the doorbell that can trigger doors or events.  It activates pulse2open if the door/window is closed and pulse2open is not active.", 'short': 'cmd_open from a doorbell'}, 'optional': True, 'type': 'Input'}, 'cmd_close_ign': {'doc': {'descr': "the 'close the door' command from the doorbell that is ignored by the app", 'short': 'cmd_close_ign from a doorbell'}, 'optional': True, 'type': 'Input'}, 'cmd_open_ign': {'doc': {'descr': "the 'open the door' command from the doorbell that is ignored by the app", 'short': 'cmd_open_ign from a doorbell'}, 'optional': True, 'type': 'Input'}, 'time_auto_close': {'doc': {'descr': 'time in seconds that the door will close automatically after optical close was triggered', 'short': 'time_auto_close'}, 'optional': True, 'type': 'int'}, 'time_check_close': {'doc': {'descr': 'time in seconds to check that the door is closed after a pulse2close to repeat the close command', 'short': 'time_check_close'}, 'optional': True, 'type': 'int'}, 'time_check_open': {'doc': {'descr': 'time in seconds to check that the door is open after a pulse2open to repeat the open command', 'short': 'time_check_open'}, 'optional': True, 'type': 'int'}, 'time_open_max': {'doc': {'descr': 'timer starts when door/window opens, and used for nty_open_max purposes', 'short': 'time_open_max'}, 'optional': True, 'type': 'int'}}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    :type my_assistant:  bool
    '''
    pass

class Fire_detector:
    ''' Fire_detector

    Input description, works also for the derived classes

    - **parameters** and **types**

    :param notifications: the notifications for inputs, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Input:
    ''' Input

    Input description, works also for the derived classes

    - **parameters** and **types**

    :param notifications: the notifications for inputs, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Irr:
    ''' Irr

    Irr description, works also for the derived classes

    - **parameters** and **types**

    :param time_run: normalised time in minutes to irrigate (actual irrigation duration is adjusted)
    :param notifications: the notifications for Irr, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param method_things: special methods of this thing, mostly realised through things
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type time_run:  int
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type method_things:  {'activate_button': {'doc': {'descr': 'activates the output if inactive', 'short': 'activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'de_activate_button': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'on_off_relay': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Output', 'Light']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}, 'toggle_button': {'doc': {'descr': 'is an input to toggle the output state', 'short': 'toggle_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Light:
    ''' Light

    Light description, works also for the derived classes

    - **parameters** and **types**

    :param notifications: the notifications for Light, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param method_things: special methods of this thing, mostly realised through things
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param my_assistant: a flag if voice (alexa) can activate this thing
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type method_things:  {'activate_button': {'doc': {'descr': 'activates the output if inactive', 'short': 'activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'de_activate_button': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'on_off_relay': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Output', 'Light']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}, 'toggle_button': {'doc': {'descr': 'is an input to toggle the output state', 'short': 'toggle_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    :type my_assistant:  bool
    '''
    pass

class Mail:
    ''' Mail

    Input description, works also for the derived classes

    - **parameters** and **types**

    :param notifications: the notifications for inputs, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Motor:
    ''' Motor

    Motor description, works also for the derived classes

    - **parameters** and **types**

    :param notifications: the notifications for Motor, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param method_things: special methods of this thing, mostly realised through things
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param value_app: app logic to determine the payload based programming logic and input parameters
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param threshold: the minimum value that an analog input must change before the value is considered changed
    :param my_assistant: a flag if voice (alexa) can activate this thing
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type method_things:  {'activate_button': {'doc': {'descr': 'activates the output if inactive', 'short': 'activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'de_activate_button': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'on_off_relay': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Output', 'Light']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}, 'toggle_button': {'doc': {'descr': 'is an input to toggle the output state', 'short': 'toggle_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type value_app:  tuple:value_app_tuples
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    :type threshold:  float
    :type my_assistant:  bool
    '''
    pass

class Optical:
    ''' Optical

    Input description, works also for the derived classes

    - **parameters** and **types**

    :param notifications: the notifications for inputs, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Output:
    ''' Output

    Output description, works also for the derived classes

    - **parameters** and **types**

    :param notifications: the notifications for outputs, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param method_things: special methods of this thing, mostly realised through things
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param my_assistant: a flag if voice (alexa) can activate this thing
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type method_things:  {'activate_button': {'doc': {'descr': 'activates the output if inactive', 'short': 'activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'de_activate_button': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'on_off_relay': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Output', 'Light']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}, 'toggle_button': {'doc': {'descr': 'is an input to toggle the output state', 'short': 'toggle_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    :type my_assistant:  bool
    '''
    pass

class Ping:
    ''' Ping

    is a network function to check the presence of a thing through a ping

    - **parameters** and **types**

    :param ip_action: ip_action=-1 (no ping), 0 (ping), 1 (ping and if lost then internet alarm)
    :param spec_func: special function attribute
    :param notifications: the notifications for pings, see [__Notifier__](Notifier.md)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param ip: ip in the format of xx.xx.xx.xx
    :param play: the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on'
    :type ip_action:  valid_set
    :type spec_func:  str
    :type notifications:  {'active': 'when payload is active', 'none': 'value of the Virtual is None', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    :type ip:  str
    :type play:  tuple:virtual_tuples
    '''
    pass

class Rain_gauge:
    ''' Rain_gauge

    Rain gauge meter device

    - **parameters** and **types**

    :param path: path to the specific hardware element
    :param mm_per_rev: mm rain per revolve
    :param notifications: the notifications for Rain_gauge, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type path:  str
    :type mm_per_rev:  float
    :type notifications:  {'rain_flooding': '> 10mm/m2 of rain', 'rain_lot': '> 5mm/m2 of rain', 'rain_nice': '> 2mm/m2 of rain', 'rain_tickle': '> 1mm/m2 rain'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    '''
    pass

class Flow_meter:
    ''' Flow_meter

    Liquid flow meter with hall effect sensor

    - **parameters** and **types**

    :param path: path to the specific hardware element
    :param q_per_rev: quantity per revolve
    :param flow_type: type of flow measured
    :param notifications: the notifications for Flow_meter, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type path:  str
    :type q_per_rev:  float
    :type flow_type:  str
    :type notifications:  {'flow_major': '> 2 m3', 'flow_lot': '> 1 m3', 'flow_nice': '> 0.5 m3', 'flow_tickle': '> 10 l'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    '''
    pass

class Sensor:
    ''' Sensor

    Any temperature sensor

    - **parameters** and **types**

    :param check_event: see the description on events, the temp_check event exists to check sensor values, see [__Event__](Event.md)
    :param high: -
    :param i_read: the type of data that this sensor reads
    :param low: -
    :param notifications: the notifications for Sensors, see [__Notifier__](Notifier.md)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param threshold: the minimum value that an analog input must change before the value is considered changed
    :type check_event:  Event
    :type high:  float
    :type i_read:  str
    :type low:  float
    :type notifications:  {'deicing': 'temperature becomes positive', 'freezing': 'temperature becomes below zero', 'high': 'when payload reaches high', 'low': 'when payload reaches low', 'positive': 'when payload reaches positive or zero coming from a negative payload', 'negative': 'when payload reaches negative, coming from a positive payload', 'normal': 'when payload becomes lower than high or higher than low', 'active': 'when payload is non zero', 'inactive': 'when payload is zero', 'notify+': 'extra notifications'}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type member_of:  list
    :type th_grp:  str
    :type threshold:  float
    '''
    pass

class Sensor_switch:
    ''' Sensor_switch

    An Input switch which is activated by something such as a high temperature like a thermostat

    - **parameters** and **types**

    :param i_read: the type of data that this sensor reads
    :param notifications: the notifications for inputs, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type i_read:  str
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Sonos:
    ''' Sonos

    is a network function to check the presence of a thing through a ping

    - **parameters** and **types**

    :param ip_action: -
    :param spec_func: -
    :param sonos_type: -
    :param soco_controller: boolean if this Sonos speaker is considered a zone controller.  For maximum performance in big networks select a Sonos speaker that is 1)not paired, 2)good network reach, 3)not override_only, 4)not likely to be grouped.  Minimal one speaker should be zone_controller!!
    :param override_only: boolean if zone controller
    :param ping: if need to be ping
    :param notifications: the notifications for pings, see [__Notifier__](Notifier.md)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param ip: ip in the format of xx.xx.xx.xx
    :param play: the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on'
    :type ip_action:  int
    :type spec_func:  str
    :type sonos_type:  str
    :type soco_controller:  bool
    :type override_only:  bool
    :type ping:  bool
    :type notifications:  {'active': 'when payload is active', 'none': 'value of the Virtual is None', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    :type ip:  str
    :type play:  tuple:virtual_tuples
    '''
    pass

class Str_device:
    ''' Str_device

    Str_device, a device containing text

    - **parameters** and **types**

    :param path: path to the specific hardware element
    :param notifications: the notifications for Str_devices, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type path:  str
    :type notifications:  {'empty': 'string is empty', 'letters': 'string is all letters', 'notify+': 'extra notifications', 'numbers': 'string is only numbers'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Str_device']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Str_device']}}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    '''
    pass

class Switch:
    ''' Switch

    Input description, works also for the derived classes

    - **parameters** and **types**

    :param notifications: the notifications for inputs, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    '''
    pass

class Utility_meter:
    ''' Utility_meter

    utility consumption meter

    - **parameters** and **types**

    :param path: path to the specific hardware element
    :param notifications: the notifications for Utility meter devices, see [__Notifier__](Notifier.md)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :type path:  str
    :type notifications:  {'day>{val}': '', 'high>{val}/sec': '', 'hour>{val}': '', 'minute>{val}': '', 'notify+': 'extra notifications'}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    '''
    pass

class Virtual:
    ''' Virtual

    Virtual's are an important vehicle to obtain smart configurations whereby interaction and dependencies between Things and Apps can be arranged, think of Virtuals as abstract rather than real things

    - **parameters** and **types**

    :param notifications: the notifications for virtuals, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param value_app: app logic to determine the payload based programming logic and input parameters
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param play: the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on'
    :type notifications:  {'active': 'when payload is active', 'none': 'value of the Virtual is None', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type value_app:  tuple:value_app_tuples
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    :type play:  tuple:virtual_tuples
    '''
    pass

class Virtual_A:
    ''' Virtual_A

    Analog type Virtual

    - **parameters** and **types**

    :param i_read: the type of data that this sensor reads
    :param notifications: similar for the notifications for Sensors, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param threshold: the minimum value that an analog input must change before the value is considered changed
    :param play: the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on'
    :type i_read:  str
    :type notifications:  {'high': 'when payload reaches high', 'low': 'when payload reaches low', 'normal': 'when payload becomes lower than high or higher than low', 'active': 'when payload is non zero', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    :type threshold:  float
    :type play:  tuple:virtual_tuples
    '''
    pass

class Virtual_R:
    ''' Virtual_R

    Range Virtual's do not just have a binary state such as ordinary virtuals but they can have a value in a range of consecutive integer numbers

    - **parameters** and **types**

    :param descr_range: a list of strings corresponding to the digital_range
    :param digital_range: a sequential list of integers determining the first, last and other possible states
    :param notifications: the notifications for range virtuals. val_ can be followed with the value of the virtual, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param play: the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on'
    :type descr_range:  str
    :type digital_range:  str
    :type notifications:  {'val_': 'when a specific value has been reached', 'going_up': 'when the payload increases', 'going_down': 'when the payload decreases', 'normal': 'when payload becomes lower than high or higher than low', 'high': 'when the payload reaches high', 'low': 'when the payload reaches low'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Virtual_R']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Virtual_R']}, 'carbon_copy@{val}': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light']}, 'twin_copy@{val}': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light']}}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type play:  tuple:virtual_tuples
    '''
    pass

class Win_cover:
    ''' Win_cover

    Window covering

    - **parameters** and **types**

    :param notifications: the notifications for window covers, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param method_things: special methods of this thing, mostly realised through things
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param threshold: the minimum value that an analog input must change before the value is considered changed
    :param my_assistant: a flag if voice (alexa) can activate this thing
    :type notifications:  {'active': 'when payload is active', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type method_things:  {'activate_button': {'doc': {'descr': 'activates the output if inactive', 'short': 'activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'de_activate_button': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}, 'on_off_relay': {'doc': {'descr': 'deactivates the output if active', 'short': 'de_activate_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Output', 'Light']}, 'is_on': {'doc': {'descr': 'is the input to measure if the output is active or not', 'short': 'is_on'}, 'optional': True, 'type': 'Input'}, 'toggle_button': {'doc': {'descr': 'is an input to toggle the output state', 'short': 'toggle_button'}, 'mk_obj_list': True, 'repeat': True, 'optional': True, 'type': ['Button']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    :type threshold:  float
    :type my_assistant:  bool
    '''
    pass

class Wind_gust:
    ''' Wind_gust

    Wind gust device

    - **parameters** and **types**

    :param i_read: the type of data that this sensor reads
    :param notifications: the notifications for Wind_speed, see [__Notifier__](Notifier.md)
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param threshold: the minimum value that an analog input must change before the value is considered changed
    :param play: the effect definition for a virtual, is a named tuple Effect with 'actor', 'when', 'make', 'on'
    :type i_read:  str
    :type notifications:  {'high_wind': 'wind 60 km/h', 'wind_fresh_breeze': 'wind 38 km/h', 'wind_hurricane': 'wind > 120 km/h', 'wind_moderate_breeze': 'wind 28 km/h', 'wind_storm': 'wind 100 km/h', 'wind_strong': 'wind 74 km/h', 'wind_strong_breeze': 'wind 50 km/h', 'wind_very_strong': 'wind 88 km/h', 'wind_violent_storm': 'wind 117 km/h'}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type duration:  int
    :type threshold:  float
    :type play:  tuple:virtual_tuples
    '''
    pass

class Wind_speed:
    ''' Wind_speed

    Wind speed meter device

    - **parameters** and **types**

    :param method_things: special methods of this thing, mostly realised through things
    :param edges_per_rev: number of edges per turn
    :param high_speed_factor: high speed wind factor
    :param low_speed_factor: low speed wind factor
    :param path: path to the specific hardware element
    :param notifications: the notifications for Wind_speed, see [__Notifier__](Notifier.md)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :type method_things:  {'wind_gust': {'doc': {'descr': 'the wind_gust is the highest wind in a 4 second measurement whereby the wind_speed is the average of last 5 measurements', 'short': 'wind_gust'}, 'boot_restore': True, 'optional': True, 'type': 'Wind_gust'}}
    :type edges_per_rev:  int
    :type high_speed_factor:  float
    :type low_speed_factor:  float
    :type path:  str
    :type notifications:  {'high_wind': 'wind 60 km/h', 'wind_fresh_breeze': 'wind 38 km/h', 'wind_hurricane': 'wind > 120 km/h', 'wind_moderate_breeze': 'wind 28 km/h', 'wind_storm': 'wind 100 km/h', 'wind_strong': 'wind 74 km/h', 'wind_strong_breeze': 'wind 50 km/h', 'wind_very_strong': 'wind 88 km/h', 'wind_violent_storm': 'wind 117 km/h'}
    :type fav:  str
    :type icon:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    '''
    pass

class Window:
    ''' Window

    Door and Window methods are the same

    - **parameters** and **types**

    :param method_things: special methods of this thing, mostly realised through things
    :param copy_things: copies of things, either carbon copy (one sided copy) or twin copy (copies in both directions)
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param where2find: where to find in the room or place
    :param path: path to the specific hardware element
    :param effect_virtuals: virtual things that are affected by, or can have an effect on, the value of the parent thing
    :param value_logic: logic to automatically determine the payload  based on time or other things
    :param descr: free description field for this thing
    :param short: free (preferably short) description for this thing
    :param member_of: a list of group names to which thing belongs
    :param th_grp: the technical group to which this thing belongs, used in groupings for lists and reports
    :param active: designate the active state for a binary thing, either 0 or 1
    :param descr_01: description for a binary thing when payload value is 0 or 1
    :param duration: duration of the output being active/ input must be active for duration before considered active
    :param my_assistant: a flag if voice (alexa) can activate this thing
    :type method_things:  {'access': {'doc': {'descr': 'zone list where the door give access to', 'short': 'access'}, 'optional': True, 'type': 'data_list'}, 'beam2close': {'doc': {'descr': 'optical beam, if tripped the door closes after 3 seconds', 'short': 'beam2close'}, 'optional': True, 'type': 'Optical'}, 'beam2open': {'doc': {'descr': 'optical beam, if tripped the door opens if beam_can_open', 'short': 'beam2open'}, 'optional': True, 'type': 'Optical'}, 'beam_can_close': {'doc': {'descr': 'actually is not needed as a switch can be put in series with the optical close beam which is similar to a constantly interrupted beam', 'short': 'beam_can_close'}, 'optional': True, 'type': 'Switch'}, 'beam_can_open': {'doc': {'descr': 'a switch that allows the optical open beam to work, it does not prevent ', 'short': 'beam_can_open'}, 'optional': True, 'type': 'Switch'}, 'is_opened': {'doc': {'descr': 'f.i. a magnetic contact that registers that the door/window is fully opened', 'short': 'is_opened'}, 'optional': True, 'type': 'Input'}, 'keep_closed': {'doc': {'descr': 'all requests to open the dw are ignored', 'short': 'keep_closed'}, 'optional': True, 'type': 'Switch'}, 'keep_opened': {'doc': {'descr': 'all requests to close the dw are ignored', 'short': 'keep_opened'}, 'optional': True, 'type': 'Switch'}, 'light_deco': {'doc': {'descr': 'is on when the door is not closed', 'short': 'light_deco'}, 'optional': True, 'type': 'Light'}, 'light_green': {'doc': {'descr': 'is on when the door is fully open', 'short': 'light_green'}, 'optional': True, 'type': 'Light'}, 'light_night': {'doc': {'descr': 'is on when the f_night is on and till xx seconds after close', 'short': 'light_night'}, 'optional': True, 'type': 'Light'}, 'light_not_closed': {'doc': {'descr': 'is on when the door is not closed', 'short': 'light_not_closed'}, 'optional': True, 'type': 'Light'}, 'light_red': {'doc': {'descr': 'is on when the door is not closed and not fully open (door is moving)', 'short': 'light_red'}, 'optional': True, 'type': 'Light'}, 'light_warn': {'doc': {'descr': 'is on when the door is moving', 'short': 'light_warn'}, 'optional': True, 'type': 'Light'}, 'lights_off_at_close': {'doc': {'descr': "if this virtual is up and the door closes, then all the lights will go off in the room.The virtual is then 'consumed' and goes off", 'short': 'lights_off_at_close'}, 'optional': True, 'type': 'Virtual'}, 'lights_off_at_open': {'doc': {'descr': "if this virtual is up and the door opens, then all the lights will go on in the room.  The virtual is then 'consumed' and goes off", 'short': 'lights_off_at_open'}, 'optional': True, 'type': 'Virtual'}, 'lights_on_at_close': {'doc': {'descr': "if this virtual is up and the door closes, then all the lights will go on in the room. The virtual is then 'consumed' and goes off", 'short': 'lights_on_at_close'}, 'optional': True, 'type': 'Virtual'}, 'lights_on_at_open': {'doc': {'descr': "if this virtual is up and the door opens, then all the lights will go on in the room.  The virtual is then 'consumed' and goes off", 'short': 'lights_on_at_open'}, 'optional': True, 'type': 'Virtual'}, 'notifications': {'doc': {'descr': "door nty's, see [__Notifier__](Notifier.md)", 'short': 'notifications'}, 'optional': True, 'type': {'active': 'when payload is active', 'conflict_oc': 'error as door is registered to be open and closed at the same time', 'inactive': 'when payload is nonactive', 'notify+': 'extra notifications', 'open_max': 'door is open for the specified maximum duration', 'trigger': 'door is triggered', 'trigger_no': 'door is trigger but opening is refused'}}, 'pulse2close': {'doc': {'descr': 'pulse to close the door', 'short': 'pulse2close'}, 'optional': True, 'type': 'Output'}, 'pulse2open': {'doc': {'descr': 'pulse to open the door', 'short': 'pulse2open'}, 'optional': True, 'type': 'Output'}, 'step2open_close': {'doc': {'descr': 'step pulse to close the door when door is open or open the door when the door is closed', 'short': 'step2open_close'}, 'optional': True, 'type': 'Output'}, 'time_auto_close': {'doc': {'descr': 'time in seconds that the door will close automatically after optical close was triggered', 'short': 'time_auto_close'}, 'optional': True, 'type': 'int'}, 'time_check_close': {'doc': {'descr': 'time in seconds to check that the door is closed after a pulse2close to repeat the close command', 'short': 'time_check_close'}, 'optional': True, 'type': 'int'}, 'time_check_open': {'doc': {'descr': 'time in seconds to check that the door is open after a pulse2open to repeat the open command', 'short': 'time_check_open'}, 'optional': True, 'type': 'int'}, 'time_open_max': {'doc': {'descr': 'timer starts when door/window opens, and used for nty_open_max purposes', 'short': 'time_open_max'}, 'optional': True, 'type': 'int'}}
    :type copy_things:  {'carbon_copy': {'doc': {'descr': 'receiving copy - carbon copy', 'short': 'carbon_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}, 'twin_copy': {'doc': {'descr': 'two way copy - twin_copy', 'short': 'twin_copy'}, 'optional': True, 'type': ['Output', 'Motor', 'Light', 'Dim_light', 'Virtual', 'Virtual_A']}}
    :type fav:  str
    :type icon:  str
    :type where2find:  str
    :type path:  str
    :type effect_virtuals:  ['Virtual', 'Virtual_A', 'Virtual_R']
    :type value_logic:  dict
    :type descr:  str
    :type short:  str
    :type member_of:  list
    :type th_grp:  str
    :type active:  int
    :type descr_01:  list-2
    :type duration:  int
    :type my_assistant:  bool
    '''
    pass

class Vera_cmd:
    ''' Aux_obj=Vera_cmd

    vera controller object - Vera_cmd

    - **parameters** and **types**

    :param log_nty: log_nty
    :param vera_pars: vera_pars
    :param vera_type: vera_type
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type log_nty:  str
    :type vera_pars:  list
    :type vera_type:  str
    :type fav:  str
    :type icon:  str
    '''
    pass

class Arduino:
    ''' tc=Arduino

    controller of things - Arduino

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Daikin:
    ''' tc=Daikin

    controller of things - Daikin

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Hue:
    ''' tc=Hue

    controller of things - Hue

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class IP_Building:
    ''' tc=IP_Building

    controller of things - IP_Building

    - **parameters** and **types**

    :param size: number of io's
    :param tpe: type of io's
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type size:  int
    :type tpe:  str
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Ikea:
    ''' tc=Ikea

    controller of things - Ikea

    - **parameters** and **types**

    :param secret: ikea secret printed on device
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type secret:  str
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class KNX:
    ''' tc=KNX

    controller of things - KNX

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Loxone:
    ''' tc=Loxone

    controller of things - Loxone

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Lutron:
    ''' tc=Lutron

    controller of things - Lutron

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class MAC_OS:
    ''' tc=MAC_OS

    controller of things - MAC_OS

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Modbus:
    ''' tc=Modbus

    controller of things - Modbus

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Niko:
    ''' tc=Niko

    controller of things - Niko

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Ow_eds:
    ''' tc=ow_eds

    controller of things - OW_EDS

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Raspi:
    ''' tc=Raspi

    controller of things - Raspi

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Renson:
    ''' tc=Renson

    Renson Healthbox controller

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Somfy:
    ''' tc=Somfy

    controller of things - Somfy

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Ubuntu:
    ''' tc=Ubuntu

    controller of things - Ubuntu

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Unipi_evok:
    ''' tc=Unipi_evok

    controller of things - Unipi_evok

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Vera:
    ''' tc=Vera

    controller of things - Vera

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Slack_driver:
    ''' Slack_driver in Driver

    is the driver for the Slack interface

    - **parameters** and **types**

    :param role_me: role_me of 'Slack_driver', adds <loxone> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Niko_driver:
    ''' Niko_driver in Driver

    is the driver for Niko

    - **parameters** and **types**

    :param role_me: role_me of 'Niko_driver', adds <niko> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class HAP_driver:
    ''' HAP_driver in Driver

    is the driver for HAP Home Apple Protocol

    - **parameters** and **types**

    :param role_me: role_me of 'HAP_driver', adds <hap> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class KNX_driver:
    ''' KNX_driver in Driver

    is the driver for KNX

    - **parameters** and **types**

    :param role_me: role_me of 'KNX_driver', adds <knx> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Lutron_driver:
    ''' Lutron_driver in Driver

    is the driver for Lutron

    - **parameters** and **types**

    :param role_me: role_me of 'Lutron_driver', adds <lutron> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Modbus_driver:
    ''' Modbus_driver in Driver

    is the driver for Modbus

    - **parameters** and **types**

    :param role_me: role_me of 'Modbus_driver', adds <modbus> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Somfy_driver:
    ''' Somfy_driver in Driver

    is the driver for Somfy

    - **parameters** and **types**

    :param role_me: role_me of 'Somfy_driver', adds <somfy> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class Twitter_driver:
    ''' Twitter_driver in Driver

    is the driver for Twitter

    - **parameters** and **types**

    :param role_me: role_me of 'Twitter_driver', adds <twitter> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass

class HAP:
    ''' tc=HAP

    controller of things - HAP

    - **parameters** and **types**

    :param fav: is this a favorite element
    :param icon: icon file for this element
    :param color: color on the display for this item
    :param ip: ip in the format of xx.xx.xx.xx
    :param roles: list of roles for this things_controller, mostly they are assigned automatically when a tc is assigned in a driver or an app
    :param ths_hw: hardware controlling the thing by the things_controller
    :type fav:  str
    :type icon:  str
    :type color:  str
    :type ip:  str
    :type roles:  list
    :type ths_hw:  list
    '''
    pass

class Knx_driver:
    ''' KNX_driver in Driver

    is the driver for KNX

    - **parameters** and **types**

    :param role_me: role_me of 'KNX_driver', adds <knx> to the roles of the specified tc
    :param fav: is this a favorite element
    :param icon: icon file for this element
    :type role_me:  {tc}
    :type fav:  str
    :type icon:  str
    '''
    pass
