from sense_hat import SenseHat

# Grab the orientation of R-Pi
# https://astro-pi.org/wp-content/uploads/2015/10/orientation.png
sense = SenseHat()
orientation = sense.get_orientation()
yaw = orientation['yaw']
roll = orientation['roll']
pitch = orientation['pitch']

print("yaw: " + str(yaw))
print("roll: " + str(roll))
print("pitch: " + str(pitch))

# Is R-Pi perpendicular to the ground?
# If so, use yaw to determine which way is up
# If not, then it's impossible to orient so drop through
if roll < 300 and roll > 80 : 
  if yaw >= 315 or yaw <= 45 :
    sense.set_rotation(90)
  elif yaw >= 225 and yaw < 315 :
    sense.set_rotation(0)
  elif yaw >= 135 and yaw < 225 :
    sense.set_rotation(270)
  elif yaw > 45 and yaw < 135 :
    sense.set_rotation(180)

# Color constants
r = (255, 0, 100)   # raspberry
w = (255, 255, 255) # white

# Draw 'Pi'
image = [
w,w,w,w,w,w,w,w,
r,r,r,r,w,w,r,w,
w,r,w,w,r,w,w,w,
w,r,w,w,r,w,r,w,
w,r,r,r,w,w,r,w,
w,r,w,w,w,w,r,w,
w,r,w,w,w,w,r,w,
r,r,r,w,w,r,r,r
]
 
sense.set_pixels(image)
