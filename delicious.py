from sense_hat import SenseHat

sense = SenseHat()

# Configure Sense Hat LED Matrix
sense.low_light=True
sense.set_rotation(180) 
sense.clear()


# Color constants
r = (255, 0, 100)   # raspberry
w = (255, 255, 255) # white

sense.show_message(" Raspberry Pi is Delicious! ", text_colour=r, back_colour=w )

