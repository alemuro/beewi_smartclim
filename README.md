![Main](https://github.com/alemuro/beewi_smartclim/workflows/Main/badge.svg?branch=master)

# beewi_smartclim - Library for BeeWi SmartClim Bluetooth LE sensor


Use this library to read temeperature and humidity from your own BeeWi SmartClim sensor.



## Functionality 
It supports reading the different measurements from the sensor
- temperature
- humidity
- battery level

To use this library you will need a Bluetooth Low Energy dongle or a Raspberry Pi with Bluetooth support.


## Build

```
$ make build
```


## Example

```
from beewi_smartclim import BeewiSmartClimPoller

b = BeewiSmartClimPoller("d0:5f:b8:51:9b:36")
b.update_sensor()

temperature = b.get_temperature()
humidity = b.get_humidity()
battery = b.get_battery()

print(temperature, humidity, battery)
```



## Projects Depending on `beewi_smartclim`

https://github.com/home-assistant/home-assistant