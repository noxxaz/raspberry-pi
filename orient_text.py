from sense_hat import SenseHat

sense = SenseHat()


while 1 :
  orientation = sense.get_orientation_degrees()
  print(sense.orientation)
  #If 
  #sense.show_message("AAA")
