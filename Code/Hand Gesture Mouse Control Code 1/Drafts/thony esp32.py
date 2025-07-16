from machine import UART, Pin
import time

uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))  # UART0, pins GP0 (TX), GP1 (RX)

image_data = b''
image_start = False

while True:
    if uart.any():
        chunk = uart.read()
        if chunk:
            image_data += chunk

    # You can set up a limit or special header/footer to know when a frame ends
    if len(image_data) > 5000:  # naive frame size limit
        print("Image received, length:", len(image_data))

        # Save image to file or forward to PC
        with open("photo.jpg", "wb") as f:
            f.write(image_data)

        print("Image saved as photo.jpg")
        image_data = b''
        time.sleep(1)
