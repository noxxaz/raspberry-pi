# Connect to Sense Hat
from sense_hat import SenseHat
sense = SenseHat()

# Configure Sense Hat LED Matrix
sense.low_light=True
sense.set_rotation(180)
sense.clear()

# Color constants
g = [0, 255, 0]  # Green
p = [20, 1, 150] # Purple

# Draw the background color first
sense.show_message(" ", back_colour=p)
sense.show_message("Raspberry Pi is Good for you! ", text_colour=g, back_colour=p)

