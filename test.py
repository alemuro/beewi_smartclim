from beewi_smartclim import BeewiSmartClimPoller

b = BeewiSmartClimPoller("d0:5f:b8:51:9b:36")
b.update_sensor()

temperature = b.get_temperature()
humidity = b.get_humidity()
battery = b.get_battery()

print(temperature, humidity, battery)