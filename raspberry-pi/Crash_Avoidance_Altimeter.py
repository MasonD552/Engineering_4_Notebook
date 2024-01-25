# type: ignore
import board
import busio
import adafruit_mpu6050
import digitalio
import time
import adafruit_mpl3115a2  # Import the MPL3115A2 library
from adafruit_displayio_ssd1306 import SSD1306
from adafruit_display_text import label
import displayio
import terminalio

displayio.release_displays()

# Initialize I2C communication with the MPU6050 sensor
sda_pin = board.GP14  # Replace with your SDA pin
scl_pin = board.GP15  # Replace with your SCL pin
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)  # Replace with your MPU6050 address

# Initialize the MPL3115A2 altimeter
mpl3115a2 = adafruit_mpl3115a2.MPL3115A2(i2c)

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

time.sleep(10)

# Add title block to display group
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)
display.show(splash)

# Store the initial altitude
initial_altitude = mpl3115a2.altitude
print(initial_altitude)

# Main loop
while True:
    # Read acceleration values
    acceleration = mpu.acceleration
    x_acceleration, y_acceleration, z_acceleration = acceleration

    # Read angular velocity values
    angular_velocity = mpu.gyro
    x_angular_velocity, y_angular_velocity, z_angular_velocity = angular_velocity

    # Read altitude from MPL3115A2 altimeter
    current_altitude = mpl3115a2.altitude

    # Check if the device is more than 1 meter above its starting point
    altitude_threshold = 1.0
    if current_altitude - initial_altitude > altitude_threshold:
        # Device is more than 1 meter above the starting point, turn off the warning light
        led.value = False
    else:
        tilt_threshold = 0.45  # Adjust this value based on your setup
        if z_acceleration < -tilt_threshold:
            # Sensor is tilted, turn on the LED warning light
            led.value = True
        else:
            led.value = False

    # Update OLED screen with angular velocity values, LED status, and altitude
    led_status = "LED Status: ON" if led.value else "LED Status: OFF"
    altitude_text = f"Current Altitude: {current_altitude:.3f} meters\nInitial Altitude: {initial_altitude:.3f} meters"
    angular_velocity_text = f"X: {x_angular_velocity:.3f},\n Y: {y_angular_velocity:.3f},\n Z: {z_angular_velocity:.3f}"
    text_area.text = altitude_text + "\n" + led_status + "\n" + angular_velocity_text

    # Add a delay to avoid rapid LED flickering
    time.sleep(0.1)
