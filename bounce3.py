# Talk to the SenseHat
from sense_hat import SenseHat
sense = SenseHat()

# Color Constants

r = (255, 0, 0) # Red
g = (0, 255, 0) # Green
b = (0, 0, 255) # Blue

# Configure Sense Hat LED Matrix
sense.low_light=True

# Red ==================
sense.set_rotation(0) 
sense.show_message(".", text_colour=r)

sense.set_rotation(90) 
sense.show_message(".", text_colour=r)

sense.set_rotation(180) 
sense.show_message(".", text_colour=r)

sense.set_rotation(270) 
sense.show_message(".", text_colour=r)

# Green =================
sense.set_rotation(0) 
sense.show_message(".", text_colour=g)

sense.set_rotation(90) 
sense.show_message(".", text_colour=g)

sense.set_rotation(180) 
sense.show_message(".", text_colour=g)

sense.set_rotation(270) 
sense.show_message(".", text_colour=g)

# Blue ====================
sense.set_rotation(0) 
sense.show_message(".", text_colour=b)

sense.set_rotation(90) 
sense.show_message(".", text_colour=b)

sense.set_rotation(180) 
sense.show_message(".", text_colour=b)

sense.set_rotation(270) 
sense.show_message(".", text_colour=b)

