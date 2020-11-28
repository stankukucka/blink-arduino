from pyfirmata2 import Arduino
import time

board = Arduino(Arduino.AUTODETECT)

print("...Arduino detected")
print("...Blink test started")

while True:
    board.digital[13].write(1)
    time.sleep(2)
    board.digital[13].write(0)
    time.sleep(1)
    board.digital[13].write(1)
    time.sleep(2)
    board.digital[13].write(0)
    time.sleep(1)
    board.digital[13].write(1)
    time.sleep(2)
    board.digital[13].write(0)
    time.sleep(1)
    print("...Blink test successfull!")
    exit()
