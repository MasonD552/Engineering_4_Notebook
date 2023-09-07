# type: ignore
import board
import time
import digitalio
led=digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT

# Function to toggle the LED state


# Main loop for blinking the LED indefinitely
while True:
    toggle_led(True)  # Turn the LED on
    time.sleep(1)  # Delay for 1 second
    toggle_led(False)  # Turn the LED off
    time.sleep(1)  # Delay for 1 second
