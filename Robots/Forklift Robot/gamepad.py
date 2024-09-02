# Imports go at the top
from microbit import *
import radio

# Startup Code
radio.config(group=1)

# Initiailise device(s)
radio.on()

# Initialise pins
pin13.NO_PULL
pin14.NO_PULL
pin15.NO_PULL
pin16.NO_PULL

# Code in a 'while True:' loop repeats forever
while True:

    # Read in values from joystick and scale them to ~8 bit values
    joy_x = int((pin1.read_analog() + 1)/ 4)
    joy_y = int((pin2.read_analog() + 1)/ 4)
  
    # Send the joystick values to the receiver
    radio.send_bytes(bytearray([joy_x, joy_y]))

    print(joy_x, joy_y)
    sleep(150)


    
