import time
from sense_hat import SenseHat
 
sense = SenseHat()

# Declare color constants 
r = (255, 0, 0)
o = (255, 127, 0)
y = (255, 200, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
e = (0, 0, 0)
w = (255, 255, 255)

# Emoji patterns

# Static smilies
emoji0 = [
e,e,y,y,y,y,e,e,
e,y,y,y,y,y,y,e,
y,y,e,y,y,e,y,y,
y,y,y,y,y,y,y,y,
y,e,y,y,y,y,e,y,
y,y,e,e,e,e,y,y,
e,y,y,e,e,y,y,e,
e,e,y,y,y,y,e,e
]

emoji1 = [
e,e,y,y,y,y,e,e,
e,y,e,e,e,e,y,e,
y,e,y,e,e,y,e,y, 
y,e,e,e,e,e,e,y,
y,r,e,e,e,e,r,y,
y,e,r,r,r,r,e,y,
e,y,e,r,r,e,y,e,
e,e,y,y,y,y,e,e
]

emoji2 = [
e,e,y,y,y,y,e,e,
e,y,y,y,y,y,y,e,
y,y,b,y,y,b,y,y,
y,y,y,y,y,y,y,y,
y,r,y,y,y,y,r,y,
y,y,r,r,r,r,y,y,
e,y,y,r,r,y,y,e,
e,e,y,y,y,y,e,e
]

# Scrolling out to left
emoji3 = [
e,y,y,y,y,e,e,e,
y,y,y,y,y,y,e,e,
y,b,y,y,b,y,y,e,
y,y,y,y,y,y,y,e,
r,y,y,y,y,r,y,e,
y,r,r,r,r,y,y,e,
y,y,r,r,y,y,e,e,
e,y,y,y,y,e,e,e
]

emoji4 = [
y,y,y,y,e,e,e,e,
y,y,y,y,y,e,e,e,
b,y,y,b,y,y,e,e,
y,y,y,y,y,y,e,e,
y,y,y,y,r,y,e,e,
r,r,r,r,y,y,e,e,
y,r,r,y,y,e,e,e,
y,y,y,y,e,e,e,e
]

emoji5 = [
y,y,y,e,e,e,e,e,
y,y,y,y,e,e,e,e,
y,y,b,y,y,e,e,e,
y,y,y,y,y,e,e,e,
y,y,y,r,y,e,e,e,
r,r,r,y,y,e,e,e,
r,r,y,y,e,e,e,e,
y,y,y,e,e,e,e,e
]

emoji6 = [
y,y,e,e,e,e,e,e,
y,y,y,e,e,e,e,e,
y,b,y,y,e,e,e,e,
y,y,y,y,e,e,e,e,
y,y,r,y,e,e,e,e,
r,r,y,y,e,e,e,e,
r,y,y,e,e,e,e,e,
y,y,e,e,e,e,e,e
]

emoji7 = [
y,e,e,e,e,e,e,e,
y,y,e,e,e,e,e,e,
b,y,y,e,e,e,e,e,
y,y,y,e,e,e,e,e,
y,r,y,e,e,e,e,e,
r,y,y,e,e,e,e,e,
y,y,e,e,e,e,e,e,
y,e,e,e,e,e,e,e
]

emoji8 = [
e,e,e,e,e,e,e,e,
y,e,e,e,e,e,e,e,
y,y,e,e,e,e,e,e,
y,y,e,e,e,e,e,e,
r,y,e,e,e,e,e,e,
y,y,e,e,e,e,e,e,
y,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

emoji9 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
y,e,e,e,e,e,e,e,
y,e,e,e,e,e,e,e,
y,e,e,e,e,e,e,e,
y,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

# Scrolling in from Right

emoji10 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,y,
e,e,e,e,e,e,e,y,
e,e,e,e,e,e,e,y,
e,e,e,e,e,e,e,y,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

emoji11 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,y,
e,e,e,e,e,e,y,y,
e,e,e,e,e,e,y,y,
e,e,e,e,e,e,y,r,
e,e,e,e,e,e,y,y,
e,e,e,e,e,e,e,y,
e,e,e,e,e,e,e,e
]

emoji12 = [
e,e,e,e,e,e,e,y,
e,e,e,e,e,e,y,y,
e,e,e,e,e,y,y,b,
e,e,e,e,e,y,y,y,
e,e,e,e,e,y,r,y,
e,e,e,e,e,y,y,r,
e,e,e,e,e,e,y,y,
e,e,e,e,e,e,e,y
]

emoji13 = [
e,e,e,e,e,e,y,y,
e,e,e,e,e,y,y,y,
e,e,e,e,y,y,b,y,
e,e,e,e,y,y,y,y,
e,e,e,e,y,r,y,y,
e,e,e,e,y,y,r,r,
e,e,e,e,e,y,y,r,
e,e,e,e,e,e,y,y
]

emoji14 = [
e,e,e,e,e,y,y,y,
e,e,e,e,y,y,y,y,
e,e,e,y,y,b,y,y,
e,e,e,y,y,y,y,y,
e,e,e,y,r,y,y,y,
e,e,e,y,y,r,r,r,
e,e,e,e,y,y,r,r,
e,e,e,e,e,y,y,y
]

emoji15 = [
e,e,e,e,y,y,y,y,
e,e,e,y,y,y,y,y,
e,e,y,y,b,y,y,b,
e,e,y,y,y,y,y,y,
e,e,y,r,y,y,y,y,
e,e,y,y,r,r,r,r,
e,e,e,y,y,r,r,y,
e,e,e,e,y,y,y,y
]

emoji16 = [
e,e,e,y,y,y,y,e,
e,e,y,y,y,y,y,y,
e,y,y,b,y,y,b,y,
e,y,y,y,y,y,y,y,
e,y,r,y,y,y,y,r,
e,y,y,r,r,r,r,y,
e,e,y,y,r,r,y,y,
e,e,e,y,y,y,y,e
]

# Configure Sense Hat LED Matrix
sense.low_light=True
sense.set_rotation(180) 
sense.clear()

# Flash Emoji
sense.set_pixels(emoji2)
time.sleep(.5)
sense.set_pixels(emoji1)
time.sleep(.5)
sense.set_pixels(emoji2)
time.sleep(.5)
sense.set_pixels(emoji1)
time.sleep(.5)
sense.set_pixels(emoji2)
time.sleep(.5)
sense.set_pixels(emoji1)
time.sleep(.5)
sense.set_pixels(emoji2)
time.sleep(1)

#Animated scroll out to left 
sense.set_pixels(emoji3)
time.sleep(.1)
sense.set_pixels(emoji4)
time.sleep(.1)
sense.set_pixels(emoji5)
time.sleep(.1)
sense.set_pixels(emoji6)
time.sleep(.1)
sense.set_pixels(emoji7)
time.sleep(.1)
sense.set_pixels(emoji8)
time.sleep(.1)
sense.set_pixels(emoji9)
time.sleep(.1)
sense.clear()
time.sleep(.1)

# Write message
sense.show_message("Smile! It's contagious!", text_colour=b)

#Animated scroll in from right 
sense.set_pixels(emoji10)
time.sleep(.1)
sense.set_pixels(emoji11)
time.sleep(.1)
sense.set_pixels(emoji12)
time.sleep(.1)
sense.set_pixels(emoji13)
time.sleep(.1)
sense.set_pixels(emoji14)
time.sleep(.1)
sense.set_pixels(emoji15)
time.sleep(.1)
sense.set_pixels(emoji16)
time.sleep(.1)
sense.set_pixels(emoji2)
time.sleep(.5)

# Flash Emoji
sense.set_pixels(emoji1)
time.sleep(.5)
sense.set_pixels(emoji2)
time.sleep(.5)
sense.set_pixels(emoji1)
time.sleep(.5)
sense.set_pixels(emoji2)
time.sleep(.5)
sense.set_pixels(emoji1)
time.sleep(.5)
sense.set_pixels(emoji2)
time.sleep(.5)
sense.set_pixels(emoji1)
time.sleep(.5)
sense.set_pixels(emoji2)
time.sleep(1)

# Clear
sense.clear()
