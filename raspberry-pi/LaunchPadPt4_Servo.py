# This code demonstrates a countdown sequence using LEDs on a board, a physical button, and a servo motor.
# The countdown starts from 10 and decrements by 1 every second until it reaches 0 (liftoff).
# It prints the countdown to the serial monitor, blinks a red LED each second, and turns on a green LED to signify liftoff.
# A servo motor slowly retracts the launch tower starting at 3 seconds until it reaches 180 degrees at liftoff.
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

# Servo Setup
pwm_servo = pwmio.PWMOut(board.GP13, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

print("Press the button to start the countdown.")  # Print a message

countdown_active = False
button_pressed_during_countdown = False

while True:
    while not countdown_active and not button.value:
        time.sleep(0.1)  # Add a small delay to reduce CPU load and improve responsiveness

    if not countdown_active:
        print("Countdown")  # Print "Countdown" after the button is pressed
        countdown_active = True
        button_pressed_during_countdown = False  # Reset the button press flag

    for x in range(10, 0, -1):
        if button.value:
            button_pressed_during_countdown = True  # Set the flag if the button is pressed during the countdown
            break

        print(x)
        ledr.value = True
        time.sleep(0.5)
        ledr.value = False
        time.sleep(0.5)

        # Adjust servo angle gradually starting at 3 seconds
        if countdown_active and x <= 7:  # 3 seconds
            desired_angle = (10 - x) * 20  # Adjust the angle as needed
            servo1.angle = desired_angle

    if countdown_active and not button_pressed_during_countdown and x <= 1:
        print("Liftoff")  # Print "Liftoff" when the countdown reaches 0
        ledb.value = True
        time.sleep(2)
        ledb.value = False
        countdown_active = False
