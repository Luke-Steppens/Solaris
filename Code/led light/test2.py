import serial
import time
#import Final_handtracking as ft
import itertools


ard = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

c = 1

if c == 1:
       x = 'a'
       ard.write(x.encode())
       time.sleep(0.05)
else:
       y = 1
       ard.write(bytes(y, 'utf-8'))
       time.sleep(0.05)



