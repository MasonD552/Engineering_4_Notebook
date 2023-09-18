# This code demonstrates a countdown sequence using LEDs on a board, a physical button, and a servo.
# The countdown starts from 10 and decrements by 1 every second until it reaches 0 (liftoff).
# It prints the countdown to the serial monitor, blinks a red LED each second, and turns on a green LED to signify liftoff.
# The servo starts sweeping at 3 seconds and continuously sweeps to reach 180 degrees at liftoff.
# If the button is pressed during the countdown process, it aborts, and another button press starts the countdown again.

# type: ignore
import board
import time
import digitalio
import pwmio
from adafruit_motor import servo

# Define LEDs
ledb = digitalio.DigitalInOut(board.GP16)  # Blue LED
ledr = digitalio.DigitalInOut(board.GP15)  # Red LED
ledr.direction = digitalio.Direction.OUTPUT
ledb.direction = digitalio.Direction.OUTPUT

# Define the button
button = digitalio.DigitalInOut(board.GP14)  # Define the button on a specific pin
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN  # Use a pull-down resistor

# Initialize the servo
pwm_servo = pwmio.PWMOut(board.GP13, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

print("Press the button to start the countdown.")  # Print a message

countdown_active = False
button_pressed_during_countdown = False
button_press_count = 0  # Track the number of button presses

while True:
    while not countdown_active and button_press_count == 0 and not button.value:
        time.sleep(0.01)
        pass

    if button.value:
        button_press_count += 1

    if button_press_count % 2 == 1 and not countdown_active:
        print("Countdown")  # Print "Countdown" after the second button press
        countdown_active = True
        button_pressed_during_countdown = False  # Reset the button press flag
        time.sleep(1)
        
    for x in range(10, 0, -1):
        if button.value:
            print("Abort")  # Print "Abort" after the button is pressed during countdown
            countdown_active = False  # Reset countdown when "Abort" is detected
            button_pressed_during_countdown = True  # Set the flag if the button is pressed during the countdown
            time.sleep(1)
            break

        print(x)
        ledr.value = True
        time.sleep(0.5)
        ledr.value = False
        time.sleep(0.5)

        if countdown_active and not button_pressed_during_countdown and x <= 1:
            print("Liftoff")  # Print "Liftoff" when the countdown reaches 0
            ledb.value = True
            servo1.angle = 180  # Set servo angle to 180 at liftoff
            time.sleep(2)
            ledb.value = False
            countdown_active = False
            break

    if button_pressed_during_countdown:
        countdown_active = False  # Reset countdown if "Abort" was printed and the button was pressed
        button_press_count = 0  # Reset button press count

    # After liftoff or abort, reset to initial state
    if not countdown_active and (button_press_count % 2 == 1 or button_pressed_during_countdown):
        print("Press the button to start the countdown.")
        button_press_count = 0
        servo1.angle = 0  # Reset servo angle to 0
