#type: ignore
import board
import busio
import adafruit_mpu6050
import digitalio
import time
from adafruit_displayio_ssd1306 import SSD1306
from adafruit_display_text import label
import displayio
import terminalio
displayio.release_displays()

# Initialize I2C communication with the MPU6050 sensor
sda_pin = board.GP14  # Replace with your SDA pin
scl_pin = board.GP15  # Replace with your SCL pin
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)  # Replace with your MPU6050 address

# Initialize the LED
led_pin = board.GP16  # Replace with the actual GPIO pin you are using
led = digitalio.DigitalInOut(led_pin)
led.direction = digitalio.Direction.OUTPUT

# Initialize the SSD1306 OLED screen
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP17)
display = SSD1306(display_bus, width=128, height=64)

# Create the display group
splash = displayio.Group()

# Add title block to display group
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)
display.show(splash)

# Main loop
while True:
    # Read acceleration values
    acceleration = mpu.acceleration
    x_acceleration, y_acceleration, z_acceleration = acceleration

    # Check if the helicopter is tilted at approximately 90 degrees (adjust threshold as needed)
    tilt_threshold = 0.45  # Adjust this value based on your setup
    if z_acceleration < -tilt_threshold:
        # Helicopter is tilted, turn on the LED warning light
        led.value = True
    else:
        # Helicopter is not tilted, turn off the LED
        led.value = False

    # Read angular velocity values
    angular_velocity = mpu.gyro
    x_angular_velocity, y_angular_velocity, z_angular_velocity = angular_velocity

    # Update OLED screen with angular velocity values and LED status
    angular_velocity_text = f"X: {x_angular_velocity:.3f},\n Y: {y_angular_velocity:.3f},\n Z: {z_angular_velocity:.3f}"
    led_status = "LED Status: ON" if led.value else "LED Status: OFF"
    text_area.text = angular_velocity_text + "\n" + led_status

    # Add a delay to avoid rapid LED flickering
    time.sleep(0.1)
