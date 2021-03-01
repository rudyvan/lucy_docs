<!--s_name-->
# Things_controllers

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
This structure defines a Things Controller such as 'Raspberry','Ubuntu','MAC_OS','Arduino','Vera','Hue','Ikea','Ow_eds','Unipi_Evok'

<!--e_descr-->

## Summary

A things_controller is a computer that manages a set of things, and these are inputs, outputs, binary or analog or any sensor such as temperature, humidity, co2, etc..

the definition of a things_controller is a dictionary (you can name them), or a list (names are generated).

Some things_controllers are alien, such as a [Hue()](Hue_driver.md) - a philips hue bridge, or [Ikea()](Ikea_driver.md) - an ikea tradfri gateway, or [Vera()](Vera_driver.md) - a vera limited gateway.

Others will be added in the future such as niko or lutron.

<!--s_tbl-->
## List of [properties](Properties.md) for __Things_controllers__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | items | ['Raspi', 'Ubuntu', 'MAC_OS', 'Arduino', 'Vera', 'Hue', 'Ikea', 'Ow_eds', 'Unipi_Evok', 'Daikin', 'IP_Building', 'Loxone', 'Renson'] | False | - | This structure defines a Things Controller such as 'Raspberry','Ubuntu','MAC_OS','Arduino','Vera','Hue','Ikea','Ow_eds','Unipi_Evok' | 
<!--e_tbl-->

The things_controllers driven by Lucy (those also drive the alien ones) can be a [Raspberry](https://www.raspberrypi.org/) or a special purpose ethernet [Arduino](https://www.arduino.cc/) or even a full unix computer with [Ubuntu](https://www.ubuntu.com/) or [Debian](https://www.debian.org/).

In case of a raspberry, it can be equipped with [unipi](Unipi_driver.md) or [piface](Piface_driver.md).

Some specific consideration exists in case of a raspberry or an arduino as things_controller is presented next.

In both a color setting can be used to distinguish visually the different things_controllers by the deployer when it displays logging messages.	

Additional information is available in [things](Things.md).

Very detailed reporting is available from the [prj_parser](Prj_parser.md), see the report at the end.

## Raspberry Specifics

* Definition of Raspberrys:
    * please beware that the raspi "name" must equal the socket.gethostname() of the specific raspberry-pi (is the pi name set with raspi-config)
    * as io_dev (input/output devices) currently piface or UniPi are accepted.   The UniPi string must be followed with 2 arguments : the number of relays and inputs installed

* Raspberry Roles: The role that a given raspberry can perform is defined in the role list of that raspberry. All raspberry's can run scenes, email, read inputs or drive outputs, but some specific roles can be assigned. 
    Below is a list of specific roles to add in the Raspi(roles=[]) definition:

    | Raspberry Role | Description |
    | --- | --- |
    | __option_x__                  | see the chapter on options to allow for multiple systems for security or climate to name a few
    | __s_clim__                    | is a raspberry who runs the same program as the m_clim, but are prevented from outputting to boiler, pump and climate controllers.  It is fitted with a touch display they can be placed anywhere a view on the heating/cooling situation is needed. m_clim and s_clim email at midnight full statistics and reset everything for the new day
    | __arduino-light__             | role to give to every Arduino that is given a light function 
    | __show__ and __displ_small__  | is the nerve centre capturing status messages from everyone and logging/displaying them. At midnight a summary is emailed
    | __papirus__                   | assumes the raspberry has a papirus display and with a specific UDP message, the text get displayed 
	
## Arduino Specifics

Arduino's with an ethernet port can be used as RGB led drivers or as access controllers reading ibuttons or other access devices.

In the Arduino() definition a roles=["arduino-access"] must be added for an access device, and roles=["arduino-light"] for a led driver.

Also always ensure that the programmable mac address is unique or dhcp ip issues will arise.

The ip address must be a fixed one.

## Example

In the example below several things_controllers are defined with a naming convention with 'PI-' prefix for raspberry's en 'AR-' for arduino's.
There is one Vera() gateway, 2 hue bridges and one ikea tradfri gateway.


<!--s_insert_{"tree":["(dk:garden).*(o:Things_controllers)","(dk:garage).*(o:Things_controllers)","(dk:master_bed).*(o:Things_controllers)","(dk:office).*(o:Things_controllers)","(dk:attic).*(o:Things_controllers)"]}-->

from project.py tree:['(dk:garden).*(o:Things_controllers)', '(dk:garage).*(o:Things_controllers)', '(dk:master_bed).*(o:Things_controllers)', '(dk:office).*(o:Things_controllers)', '(dk:attic).*(o:Things_controllers)']
```python3
# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:garden,o:Place,kw:contents,lp:1,o:Things_controllers>

from lucy_app import *

Things_controllers(items = {
            "PI-Garden":Raspi(color = "brown",ip = "192.168.15.55",ths_hw = ["unipi,8,14"]),
            "PI-Gate":Raspi(color = "green",ip = "192.168.15.121",ths_hw = ["unipi,16,14"]),
            "PI-Soccer":Raspi(color = "white",ip = "192.168.15.78",ths_hw = ["unipi,6,6"])})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:garage,o:Room,kw:contents,lp:0,o:Things_controllers>

from lucy_app import *

Things_controllers(items = {
            "PI-RearDoor":Raspi(color = "white",ip = "192.168.15.94",ths_hw = ["unipi,12,14"]),
            "PI-Security":Raspi(color = "cyan",ip = "192.168.15.29",ths_hw = ["unipi,16,14"]),
            "PI-Water":Raspi(color = "green",ip = "192.168.15.33",ths_hw = ["unipi,6,6"])})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:master_bed,o:Room,kw:contents,lp:1,o:Things_controllers>

from lucy_app import *

Things_controllers(items = {
            "DK_Bedroom":Daikin(color = "white",ip = "192.168.15.92"),
            "Hue_Bridge2":Hue(color = "white",ip = "192.168.15.159")})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:office,o:Room,kw:contents,lp:0,o:Things_controllers>

from lucy_app import *

Things_controllers(
    items = {
            "DK_Office":Daikin(color = "blue",ip = "192.168.15.60"),
            "Hue_Bridge":Hue(color = "white",ip = "192.168.15.136"),
            "Ikea_Tradfri":Ikea(color = "white",ip = "192.168.15.164",secret = "Ua42jpHcvKu3xsKy"),
            "PI-CSlave":Raspi(color = "white",ip = "192.168.15.91"),
            "PI-Dev":Raspi(color = "white",ip = "192.168.15.56"),
            "PI-Notify":Raspi(color = "white",ip = "192.168.15.106",ths_hw = ["piface"]),
            "PI-Notify2":Raspi(color = "white",ip = "192.168.15.63"),
            "PI-Notify3":Raspi(color = "white",ip = "192.168.15.133",ths_hw = ["piface"]),
            "PI-Notify4":Raspi(color = "white",ip = "192.168.15.120",ths_hw = ["piface"]),
            "PI-Stats":Raspi(
                    color = "blue",
                    ip = "192.168.15.35",
                    roles = ["trace","dropbox","sms","network","things_forensics","notifier","phone"],
                    ths_hw = ["unipi,6,6"]),
            "Vera_plus":Vera(color = "white",ip = "192.168.15.75"),
            "imac-lucy":Ubuntu(color = "white",ip = "192.168.15.113"),
            "ow_office":Ow_eds(color = "white",ip = "192.168.15.151")})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:attic,o:Room,kw:contents,lp:0,o:Things_controllers>

from lucy_app import *

Things_controllers(items = {
            "Healthbox_North":Renson(color = "magenta",ip = "192.168.15.146"),
            "Healthbox_South":Renson(color = "magenta",ip = "192.168.15.145"),
            "PI-Light":Raspi(color = "magenta",ip = "192.168.15.31",ths_hw = ["unipi,16,14"])})

```

<!--e_insert-->

