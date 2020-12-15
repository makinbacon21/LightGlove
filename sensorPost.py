import requests
import RPI.GPIO as GPIO

import time

# set gpio pins
pins = [8, 10, 12, 16, 18]

# use board pin numbers and not SoC pin numbers
GPIO.setmode(GPIO.BOARD)

# set pins as inputs
for pin in pins:
    GPIO.setup(pin, GPIO.IN)

# infinite loop checking high vs low and printing
while True:
    for pin in pins:
        if pin == 1:
            print(str(pin) + " is HIGH")
        else:
            print(str(pin) + " is LOW")

    time.sleep(0.5)
    # requests.post("https://maker.ifttt.com/trigger/rpi_test/with/key/dl19EHfc-UHyIuQ-5AjJEQ"