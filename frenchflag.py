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
w = (255, 255, 255)
 
image = [
b,b,b,w,w,r,r,r,
b,b,b,w,w,r,r,r,
b,b,b,w,w,r,r,r,
b,b,b,w,w,r,r,r,
b,b,b,w,w,r,r,r,
b,b,b,w,w,r,r,r,
b,b,b,w,w,r,r,r,
b,b,b,w,w,r,r,r
]
 
sense.set_pixels(image)
