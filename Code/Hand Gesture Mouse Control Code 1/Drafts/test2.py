from os import write
import serial
import time
import hand_LCD


arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

while hand_LCD :
       if hand_LCD is EnvironmentError :
              x=2
              arduino.write(bytes(x))
              #y= arduino.readline()
              #print(y)
       else:
              x=1
              arduino.write(bytes (x))
              #y = arduino.readline()
              #print(y)

#if any problem arises call me immediately -conor