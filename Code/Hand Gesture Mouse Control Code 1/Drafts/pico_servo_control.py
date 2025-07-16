from machine import Pin, PWM
import time

# Setup PWM pins for servos
servo1 = PWM(Pin(0))  # X-axis servo
servo2 = PWM(Pin(1))  # Y-axis servo
servo3 = PWM(Pin(2))  # Z-axis servo

# Configure PWM frequency for servos
servo1.freq(50)
servo2.freq(50)
servo3.freq(50)

def angle_to_duty(angle):
    """Convert angle (0-180) to duty value (0-65535)"""
    min_duty = 1638  # 2.5% of 65535
    max_duty = 8191  # 12.5% of 65535
    return int(min_duty + (max_duty - min_duty) * angle / 180)

# Initialize servos to center position
for servo in [servo1, servo2, servo3]:
    servo.duty_u16(angle_to_duty(90))

# Setup UART for receiving data from laptop
from machine import UART
uart = UART(0, baudrate=115200)

def process_command(command):
    try:
        # Parse the angles from the command string
        angles = command.strip().split(',')
        if len(angles) == 3:
            angle1 = int(angles[0])
            angle2 = int(angles[1])
            angle3 = int(angles[2])
            
            # Update servo positions
            servo1.duty_u16(angle_to_duty(angle1))
            servo2.duty_u16(angle_to_duty(angle2))
            servo3.duty_u16(angle_to_duty(angle3))
    except Exception as e:
        print("Error processing command:", e)

# Main loop
print("Pico ready to receive commands")
buffer = ""

while True:
    if uart.any():
        char = uart.read(1).decode()
        if char == '\n':
            process_command(buffer)
            buffer = ""
        else:
            buffer += char
