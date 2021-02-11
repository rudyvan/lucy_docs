# Shelly Devices

Shelly devices are very low cost yet powerful wifi enabled things that can be included using pin type shelly.

A shelly_driver is not created as these devices can be addressed directly through there ip address.

for more information, see ![shelly](shelly_rgbw2.pdf) of how to wire RGB ledstrip or 3 white strips.

All of the effects are supported in Color_light and have to be coded as : "meteor_shower", "gradual_change", "breath", "flash", "gradual_on_off", "red_green_change".

Only outputs are supported and the shelly_rgbw2 is tested in color and white mode (use of the channel in pin is mandatory).

Examples:
```
light={
    "room_lights":{
        "closet_RGB": 
            Color_light(pin="shelly:192.168.15.79",usage={"watts":24},
                value_logic={"assign":{"is_room_secure":"0","is_holiday":"0",
                             "00:00":"0","17:00":"50,gradual_change","18:00":"60,meteor_shower",
                             "19:00":"100,gradual_change","20:00":"100,green","21:00":"100,blue","22:00":"50,red"}}),
        "bed_led":           
            Dimmer(pin="shelly:192.168.15.79,1",usage={"watts":6},
                value_logic={"assign":{"is_room_secure":"0","is_holiday":"0",
                             "00:00":"0","17:00":"50","18:00":"60","19:00":"100,"22:00":"50"}}),
```

## Deployment of Shelly devices

Firstly use the shelly app to define and link the device to the wifi network.
Ensure the ip address of the device is reachable and stays fixed.

Define all the parameters for the device including the type of wiring (color) or white strips and voltage 12V or 24V.

Test everything properly.

 