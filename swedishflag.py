from sense_hat import SenseHat
 
sense = SenseHat()
 
r = (255, 0, 0)
o = (255, 127, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
e = (0, 0, 0)
 
image = [
b,b,y,y,b,b,b,b,
b,b,y,y,b,b,b,b,
b,b,y,y,b,b,b,b,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
b,b,y,y,b,b,b,b,
b,b,y,y,b,b,b,b,
b,b,y,y,b,b,b,b
]
 
sense.set_pixels(image)
