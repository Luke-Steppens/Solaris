import board, busio, digitalio, time
from adafruit_st7735r import ST7735R
import displayio
from adafruit_display_shapes.circle import Circle

# SPI Display Setup
mosi_pin = board.GP11
clk_pin = board.GP10
reset_pin = board.GP17
cs_pin = board.GP18
dc_pin = board.GP16

displayio.release_displays()
spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)

display = ST7735R(display_bus, width=128, height=160, bgr=1)

# Button Setup (with internal pull-ups)
button_left = digitalio.DigitalInOut(board.GP4)  # Now Left
button_left.direction = digitalio.Direction.INPUT
button_left.pull = digitalio.Pull.UP

button_right = digitalio.DigitalInOut(board.GP5)  # Now Right
button_right.direction = digitalio.Direction.INPUT
button_right.pull = digitalio.Pull.UP

button_up = digitalio.DigitalInOut(board.GP2)  # Now Up
button_up.direction = digitalio.Direction.INPUT
button_up.pull = digitalio.Pull.UP

button_down = digitalio.DigitalInOut(board.GP3)  # Now Down
button_down.direction = digitalio.Direction.INPUT
button_down.pull = digitalio.Pull.UP

# Initial Dot Position
dot_x = 64
dot_y = 80
dot_radius = 5

dot = Circle(dot_x, dot_y, dot_radius, fill=0x00FF00)

# Group for display elements
group = displayio.Group()
group.append(dot)
display.root_group = group

# Movement speed
step = 3

while True:
    if not button_up.value:  # Move Up
        dot.y = max(0, dot.y - step)
    if not button_down.value:  # Move Down
        dot.y = min(160, dot.y + step)
    if not button_left.value:  # Move Left
        dot.x = max(0, dot.x - step)
    if not button_right.value:  # Move Right
        dot.x = min(128, dot.x + step)

    display.root_group = group  # Refresh display
    time.sleep(0.1)  # Delay to prevent too fast movement
