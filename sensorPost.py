import requests
import time
from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board

board = Board(1, 0x10)  # Select i2c bus 1, set address to 0x10

# threshold value (TBD)
thresh = 1000

if __name__ == "__main__":
  while board.begin() != board.STA_OK:  # Board begin and check the board's status
    print("Board begin failed.")
    time.sleep(1)
print("Board begin success.")
board.set_adc_enable()

# loop--post to ifttt endpoint if voltage > threshold value
while True:

    # if voltage > threshold, post to ifttt, wait to prevent multi activation, else wait 0.5s
    if board.get_adc_value(board.A0) < thresh:
        print("Event triggered")
        requests.post("https://maker.ifttt.com/trigger/rpi_test/with/key/dl19EHfc-UHyIuQ-5AjJEQ")
        time.sleep(3)
    else:
        time.sleep(1)