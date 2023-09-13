# This code demonstrates a countdown sequence using LEDs on a board and a physical button.
# The countdown starts from 10 and decrements by 1 every second until it reaches 0 (liftoff).
# It prints the countdown to the serial monitor, blinks a red LED each second, and turns on a green LED to signify liftoff.
# If the button is pressed during the countdown process, it aborts, and another button press starts the countdown again.

# type: ignore
import board
import time
import digitalio

# Define LEDs
ledb = digitalio.DigitalInOut(board.GP16)  # Blue LED
ledr = digitalio.DigitalInOut(board.GP15)  # Red LED
ledr.direction = digitalio.Direction.OUTPUT
ledb.direction = digitalio.Direction.OUTPUT

# Define the button
button = digitalio.DigitalInOut(board.GP14)  # Define the button on a specific pin
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN  # Use a pull-down resistor

print("Press the button to start the countdown.")  # Print a message

countdown_active = False

while True:
    while not countdown_active and not button.value:
        pass
    
    if not countdown_active:
        print("Countdown")  # Print "Countdown" after the button is pressed
        countdown_active = True

    for x in range(10, -1, -1):
        if button.value:
            print("ABORT")  # Print "ABORT" if the button is pressed during the countdown
            countdown_active = False
            ledr.value = False  # Turn off the red LED
            break

        print(x)
        ledr.value = True
        time.sleep(1)
        ledr.value = False

    if countdown_active:
        print("Liftoff")  # Print "Liftoff" when the countdown reaches 0
        ledb.value = True
        time.sleep(2)
        ledb.value = False
        countdown_active = False
