# Imports go at the top
from microbit import *
import radio

# Startup Code
radio.config(group=1)

# Initiailise device(s)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:

    # Receive bytearray (8 bit maximum) from GamePad
    incoming = radio.receive_bytes()

 
    if (incoming) is not None:
        print(incoming[0], incoming[1])

    sleep(150)


    
