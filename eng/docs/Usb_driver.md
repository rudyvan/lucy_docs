<!--s_name-->
# Usb_driver

<!--e_name-->

<!--s_role-->
<!--e_role-->

<!--s_descr-->
Driver for interfacing with usb serial devices.

<!--e_descr-->

## Example

In the example below a usb_driver is defined with one item serial_arduino:

<!--s_insert_{"tree":"(o:Usb_driver)"}-->

from project.py tree:(o:Usb_driver)
```python3
# --> project.py :<dk:project,o:Project,kw:drivers,lp:16,o:Usb_driver>

from lucy_app import *

Usb_driver(
    usb_paths = {
            "RS485":{
                    "baudrate":9600,
                    "bytesize":8,
                    "parity":"E",
                    "port":["/dev/serial/by-id/usb-Silicon_Labs_CP2102*","/dev/ttyUSB0*"],
                    "stopbits":2},
            "serial_arduino":{"baudrate":38400,"bytesize":8,"parity":"N","port":["/dev/serial/by-id/usb-Arduino*","/dev/ttyUSB0*"],"stopbits":1}})

```

<!--e_insert-->

Subsequently the serial input can be used to specify a pin for a thing as in:

<!--s_insert_{"tree":"(dk:garden).*(o:Access_point)"}-->

from project.py tree:(dk:garden).*(o:Access_point)
```python3
# --> project.py :<dk:project,o:Project,kw:property,lp:0,o:House,kw:places,dk:garden,o:Place,kw:contents,lp:2,o:Access_ways,kw:items,dk:iButton_out_garden,o:Access_point>

from lucy_app import *

Access_point(direction = "exit",method_things = {
            "access_green":Light(duration = 4,path = "unipi:PI-Garden,relay,7"),
            "access_red":Light(duration = 4,path = "unipi:PI-Garden,relay,6")},path = "usb:PI-Garden,serial_arduino,1w_button,0")

```

<!--e_insert-->

## Current Limitations

The serial driver looks for 1w=.... cr and then this is assigned to the field for which the pin is defined.

Future versions will certainly add more interaction possibilities between a serial device (in this example an arduino) and a thingscontroller.

Second issue is that the parameters (baudrate,...) are not checked and just copied into serial.open().  Please study therefore the serial module before adding/changing.
The timeout is automatically patched to zero as the driver needs to be non blocking.
 
<!--s_tbl-->
## List of [properties](Properties.md) for __Usb_driver__:

  | Property | Validation | Optional? | Repeat? | Description |
  | --- | --- | --- | --- | --- |
  | fav | str | True | - | is this a favorite element | 
  | icon | str | True | - | icon file for this element | 
  | usb_paths | dict | False | - | Per usb_path the port, baudrate and other parameters of the serial port should be defined. Use a dictionary with keywords as in use of the python serial module for open such as {port}, {baudrate}, {bytesize}, {parity}, {stopbits},.. If the port name ends with *, then the first matching portname will be used instead of an exact name. | 

## List of [Errors/Warnings](Error_Warn.md) for  __Usb_driver__:

  | Error/Warning ID | Error/Warning MSG | Occurring When? |
  | --- | --- | --- | 
  | err_usb_port_fail | !!usb error port {:}/{:} port? {:} |  
  | err_usb_port_ok | !!usb port ok again {:}/{:} -> {:} |  
  | err_usb_scan_decode | !!usb error scan decode {:}/{:} fail {:} |  
  | err_usb_scan_th | !!usb error scan, ?thing {:}/{:} fail {:} |  
<!--e_tbl-->

