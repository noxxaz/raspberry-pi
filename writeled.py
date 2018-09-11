import sys

from sense_hat import SenseHat

sense = SenseHat()

# Configure Sense Hat LED Matrix
sense.low_light=True
sense.set_rotation(180)
sense.clear()


sense.show_message(str(sys.argv[1]))
