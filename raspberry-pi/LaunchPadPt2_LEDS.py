# It initializes two LEDs, one red (ledr) and one blue (ledb), and uses them to perform a countdown.
# The countdown starts from 10 and decrements by 1 every half second until it reaches 1,
# at which point it prints "Liftoff" and turns on the blue LED for 2 seconds.

# type: ignore
import board
import time
import digitalio

ledb = digitalio.DigitalInOut(board.GP16)  # Define LED on Board
ledr = digitalio.DigitalInOut(board.GP15)  # Define LED on Board
ledr.direction = digitalio.Direction.OUTPUT
ledb.direction = digitalio.Direction.OUTPUT
print("Countdown")  # Print "Countdown"
time.sleep(1)  # Pause for 1 second.

for x in range(10, 0, -1):  # Start a for loop with 'x' ranging from 10 down to 1 (inclusive), decreasing by 1 in each iteration.
    print(x)
    ledr.value = True
    time.sleep(0.5)
    ledr.value = False
    time.sleep(0.5)
    if x <= 1:
        print("Liftoff")  # Print "Liftoff" when 'x' is equal to 1
        ledb.value = True
        time.sleep(2)