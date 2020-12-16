import requests

import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# define spi bus to MCP3008 and MCP3008 object
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)

# threshold value (TBD)
thresh = 6000

# define analog channel
channel = AnalogIn(mcp, MCP.P0)

# loop--post to ifttt endpoint if voltage > threshold value
while True:
    #<DEBUG>
    print('Raw ADC Value: ', channel.value)
    print('ADC Voltage: ' + str(channel.voltage) + 'V')
    #</DEBUG>

    # if voltage > threshold, post to ifttt, wait to prevent multi activation, else wait 0.5s
    if channel.voltage > thresh:
        requests.post("https://maker.ifttt.com/trigger/rpi_test/with/key/dl19EHfc-UHyIuQ-5AjJEQ")
        time.sleep(3)
    else:
        time.sleep(0.5)