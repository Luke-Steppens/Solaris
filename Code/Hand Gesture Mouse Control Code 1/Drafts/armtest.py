import serial
import time

# Serial port settings
COM_PORT = 'COM8'  # Replace with your actual COM port
BAUD_RATE = 115200

def initialize_serial():
    try:
        # Attempt to open the serial port
        ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for the Arduino to reset and initialize
        print(f"Connected to {COM_PORT} at {BAUD_RATE} baud rate.")
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None

def send_data(ser, data):
    try:
        # Send the data to the Arduino
        ser.write(data.encode('utf-8'))
        print(f"Sent: {data}")
    except PermissionError as e:
        print(f"Error sending data: {e}")

def close_serial(ser):
    try:
        ser.close()
        print("Serial port closed.")
    except Exception as e:
        print(f"Error closing serial port: {e}")

def main():
    # Attempt to initialize the serial connection
    ser = initialize_serial()
    
    if ser is not None:
        # Send data to Arduino
        send_data(ser, '0,90,45')  # Example data to send to Arduino
        
        # Close the serial connection properly
        close_serial(ser)
    else:
        print("Failed to connect to the Arduino.")

if __name__ == "__main__":
    main()
