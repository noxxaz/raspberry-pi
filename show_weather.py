from sense_hat import SenseHat
 
sense = SenseHat()
sense.set_rotation(180)

# while 1 :
 
# Humidity
humidity = sense.get_humidity()
humidity = round(humidity, 1) # round to 1 decimal
sense.show_message("Humidity: " + str(humidity) + "%", text_colour = [255, 0, 0], scroll_speed = .07)

# Temperature
temp = sense.get_temperature_from_pressure()
temp = (temp * 1.8) + 32 # convert C to F
temp = round(temp, 1)    # round to 1 decimal
sense.show_message("Temp: " + str(temp) + "F", text_colour = [0, 0, 255], scroll_speed = .07)

# Air Pressure
pressure = sense.get_pressure()
pressure = round(pressure, 1) # round to 1 decimal
sense.show_message("Air Pressure: " + str(pressure) + "mBar", text_colour = [0, 255, 0], scroll_speed = .07)
