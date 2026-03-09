from pysimverse import Drone
import time

#Create an instance of drone
drone = Drone()
drone.connect()

drone.take_off()
#distance is in cm


drone.move_forward(280)
time.sleep(2)
drone.move_forward(200)
drone.move_backward(200)
time.sleep(2)
drone.move_left(50)
time.sleep(2)
drone.move_right(70)
time.sleep(2)