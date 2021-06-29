<!--s_name-->
# Things_controllers

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
This structure defines a Things Controller such as 'Raspberry','Ubuntu','MAC_OS','Arduino','Vera','Hue','Ikea','Eds','Unipi_Evok'

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
  | items | ['Raspi', 'Ubuntu', 'MAC_OS', 'Arduino', 'Vera', 'Hue', 'Ikea', 'Eds', 'Unipi_Evok', 'Daikin', 'IP_Building', 'Loxone', 'Renson', 'Modbus', 'Sma'] | False | - | This structure defines a Things Controller such as 'Raspberry','Ubuntu','MAC_OS','Arduino','Vera','Hue','Ikea','Eds','Unipi_Evok' | 
<!--e_tbl-->

The things_controllers driven by Lucy (those also drive the alien ones) can be a [Raspberry](https://www.raspberrypi.org/) or a special purpose ethernet [Arduino](https://www.arduino.cc/) or even a full unix computer with [Ubuntu](https://www.ubuntu.com/) or [Debian](https://www.debian.org/).

In case of a raspberry, it can be equipped with [unipi](Unipi_driver.md) or [piface](Piface_driver.md), by using the hw_gws list definition.

Some specific consideration exists in case of a raspberry or an arduino as things_controller.

A Things_controller need to be located through a path.

Currently, the following path definitions are possible:

<!--s_insert_{"prj_parser":"app_obj.conf","sections":["PATH"],"vars":["tc_path_defs"]}-->

from app_obj.conf:
```python3
[PATH]

tc_path_defs={
	"ip": {"gw_sleep":0, "format":"ip"},
	"usb":{"gw_sleep":0.8, "format":"tc,usb_path,nr"}}

```

<!--e_insert-->

The format parameter defines the structure of the path definition, see below for examples. 

Very detailed reporting regarding the thingscontrollers is available after the parsing completes from the [prj_parser](Prj_parser.md), see the report at the end.

## Raspberry Specifics

* Definition of Raspberrys:
    * please beware that the raspi "name" must equal the socket.gethostname() of the specific raspberry-pi (is the pi name set with raspi-config)
    * as io_dev (input/output devices) currently piface or UniPi are accepted.   The UniPi string must be followed with 2 arguments : the number of relays and inputs installed

* Raspberry Roles: The role that a given raspberry can perform is defined in the role list of that raspberry. All raspberry's can run scenes, email, read inputs or drive outputs, but some specific roles can be assigned. 
    
    These roles are automatically assigned by associating a things_controller with a driver or an app.

## Examples

In the example below several things_controllers are defined with a naming convention with 'PI-' prefix for raspberry's.
Amongst others there is one Vera() gateway, 2 hue bridges, 1 ikea tradfri gateway, Modbus energy reading device and several Renson and Daikin controllers.


<!--s_insert_{"tree":["(dk:garden).*(o:Things_controllers)","(dk:garage).*(o:Things_controllers)","(dk:master_bed).*(o:Things_controllers)","(dk:office).*(o:Things_controllers)","(dk:attic).*(o:Things_controllers)"]}-->

from project.py tree:['(dk:garden).*(o:Things_controllers)', '(dk:garage).*(o:Things_controllers)', '(dk:master_bed).*(o:Things_controllers)', '(dk:office).*(o:Things_controllers)', '(dk:attic).*(o:Things_controllers)']
```python3
# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:garden,o:Place,kw:contents,lp:1,o:Things_controllers>

from lucy_app import *

Things_controllers(items = {
            "PI-Garden":Raspi(hw_gws = ["unipi:8,14"],path = "ip:192.168.15.55"),
            "PI-Gate":Raspi(hw_gws = ["unipi:16,14"],path = "ip:192.168.15.121"),
            "PI-Soccer":Raspi(hw_gws = ["unipi:6,6"],path = "ip:192.168.15.78")})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:garage,o:Room,kw:contents,lp:0,o:Things_controllers>

from lucy_app import *

Things_controllers(items = {
            "PI-RearDoor":Raspi(hw_gws = ["unipi:12,14"],path = "ip:192.168.15.94"),
            "PI-Security":Raspi(hw_gws = ["unipi:16,14"],path = "ip:192.168.15.29")})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:master_bed,o:Room,kw:contents,lp:1,o:Things_controllers>

from lucy_app import *

Things_controllers(items = {
            "DK_Bedroom":Daikin(path = "ip:192.168.15.92"),
            "Hue_Bridge2":Hue(path = "ip:192.168.15.159")})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:office,o:Room,kw:contents,lp:0,o:Things_controllers>

from lucy_app import *

Things_controllers(
    items = {
            "DK_Office":Daikin(path = "ip:192.168.15.60"),
            "Hue_Bridge":Hue(path = "ip:192.168.15.136"),
            "Ikea_Tradfri":Ikea(path = "ip:192.168.15.164",secret = "Ua42jpHcvKu3xsKy"),
            "PI-CSlave":Raspi(path = "ip:192.168.15.91"),
            "PI-Dev":Raspi(path = "ip:192.168.15.56"),
            "PI-Notify":Raspi(hw_gws = ["piface:8,8"],path = "ip:192.168.15.106"),
            "PI-Notify2":Raspi(path = "ip:192.168.15.63"),
            "PI-Notify3":Raspi(hw_gws = ["piface:8,8"],path = "ip:192.168.15.133"),
            "PI-Notify4":Raspi(hw_gws = ["piface:8,8"],path = "ip:192.168.15.120"),
            "PI-Stats":Raspi(hw_gws = ["unipi:6,6"],path = "ip:192.168.15.35"),
            "Vera_plus":Vera(path = "ip:192.168.15.75"),
            "imac-lucy":Ubuntu(path = "ip:192.168.15.113"),
            "ow_office":Eds(path = "ip:192.168.15.151")})

# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:attic,o:Room,kw:contents,lp:0,o:Things_controllers>

from lucy_app import *

Things_controllers(items = {
            "Healthbox_North":Renson(path = "ip:192.168.15.146"),
            "Healthbox_South":Renson(path = "ip:192.168.15.145"),
            "PI-Light":Raspi(hw_gws = ["unipi:16,14"],path = "ip:192.168.15.31")})

```

<!--e_insert-->

