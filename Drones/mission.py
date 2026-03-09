from pysimverse import Drone
import keyboard
import time

# create drone
drone = Drone()

# connect to simulator
drone.connect()

print("Drone Controls")
print("T = Takeoff")
print("L = Land")
print("W A S D = Move")
print("UP/DOWN = Height")
print("ESC = Exit")

while True:

    if keyboard.is_pressed('t'):
        drone.take_off()
        time.sleep(0.5)

    if keyboard.is_pressed('l'):
        drone.land()
        time.sleep(0.5)

    if keyboard.is_pressed('w'):
        drone.move_forward(100)

    if keyboard.is_pressed('s'):
        drone.move_backward(100)

    if keyboard.is_pressed('a'):
        drone.move_left(50)

    if keyboard.is_pressed('d'):
        drone.move_right(50)

    if keyboard.is_pressed('up'):
        drone.move_up(50)

    if keyboard.is_pressed('down'):
        drone.move_down(50)

    if keyboard.is_pressed('esc'):
        print("Exiting simulator")
        break

    time.sleep(0.1)