from machine import Pin, PWM
import time

# Setup servos
servo1 = PWM(Pin(0))
servo2 = PWM(Pin(1))
servo3 = PWM(Pin(2))

for s in (servo1, servo2, servo3):
    s.freq(50)

def move_servo(servo, angle):
    min_duty = 1000
    max_duty = 9000
    duty = int(min_duty + (angle / 180.0) * (max_duty - min_duty))
    servo.duty_u16(duty)

while True:
    try:
        line = input()
        print("Received:", line)

        parts = line.strip().split(',')
        if len(parts) != 3:
            print("Invalid input:", line)
            continue

        angle1 = int(float(parts[0]))
        angle2 = int(float(parts[1]))
        angle3 = int(float(parts[2]))

        move_servo(servo1, angle1)
        move_servo(servo2, angle2)
        move_servo(servo3, angle3)

    except Exception as e:
        print("Error:", e)

    time.sleep(0.01)
