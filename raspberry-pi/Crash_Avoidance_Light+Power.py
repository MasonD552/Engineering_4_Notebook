#type: ignore 
import board
import busio
import adafruit_mpu6050
import digitalio
import time

# Initialize I2C communication with the MPU6050 sensor
sda_pin = board.GP14  # Replace with your SDA pin
scl_pin = board.GP15  # Replace with your SCL pin
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

# Initialize the LED
led_pin = board.GP16  # Replace with the actual GPIO pin you are using
led = digitalio.DigitalInOut(led_pin)
led.direction = digitalio.Direction.OUTPUT

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
    
    # Print accelerometer data and LED status
    print(f"Acceleration (m/s²) - X: {x_acceleration:.3f}, Y: {y_acceleration:.3f}, Z: {z_acceleration:.3f}")
    print(f"LED Status: {'ON' if led.value else 'OFF'}")
    
    # Add a delay to avoid rapid LED flickering
    time.sleep(0.1)
