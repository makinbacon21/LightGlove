import requests
import time
from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board

board = Board(1, 0x10)  # Select i2c bus 1, set address to 0x10

# threshold value (TBD)
thresh = 1300

if __name__ == "__main__":
  while board.begin() != board.STA_OK:  # Board begin and check the board's status
    print("Board begin failed.") # debug logging
    time.sleep(1)
print("Board begin success.") # debug logging
board.set_adc_enable()

# infinite loop
while True:

    # if voltage < threshold, post to ifttt, wait to prevent multi activation, else wait 0.5s
    if board.get_adc_value(board.A0) < thresh:
        print("pointer triggered") # debug logging
        requests.post("https://maker.ifttt.com/trigger/pointer_finger/with/key/esey_sUu1A1kbufOqfcjz4fYppk18XBgfJMeJkhNMoX")
        time.sleep(3)
    elif board.get_adc_value(board.A1) < thresh:
        print("middle triggered") # debug logging
        requests.post("https://maker.ifttt.com/trigger/middle_finger/with/key/esey_sUu1A1kbufOqfcjz4fYppk18XBgfJMeJkhNMoX")
        time.sleep(3)
    else:
        time.sleep(1)