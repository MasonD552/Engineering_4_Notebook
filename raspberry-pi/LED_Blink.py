# type: ignore
import board
import time
import digitalio
led=digitalio.DigitalInOut(board.LED) #Define LED on Board
led.direction=digitalio.Direction.OUTPUT



# Main loop for blinking the LED indefinitely
while True:
    toggle_led(True)  # Turn the LED on
    time.sleep(1)  # Delay for 1 second
    toggle_led(False)  # Turn the LED off
    time.sleep(1)  # Delay for 1 second
