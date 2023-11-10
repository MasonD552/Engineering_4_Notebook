#type: ignore 
import board
import busio
import adafruit_mpu6050
import digitalio
import time
import storage

# Initialize I2C communication with the MPU6050 sensor
sda_pin = board.GP14  # SDA pin
scl_pin = board.GP15  # SCL pin
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

# Initialize the Onboard Led and Led connected to GP16
led_pin = board.LED  # LED PIN = ONBOARD
led = digitalio.DigitalInOut(led_pin)
led.direction = digitalio.Direction.OUTPUT

led_2_pin = board.GP16  # LED PIN = GP16
led_2 = digitalio.DigitalInOut(led_2_pin)
led_2.direction = digitalio.Direction.OUTPUT
# Function to check if the Pico is tilted
def is_tilted(acceleration, tilt_threshold):
    x_acceleration, y_acceleration, z_acceleration = acceleration
    return z_acceleration < -tilt_threshold

# Create or open the data.csv file in append mode
with open("/data.csv", "a") as datalog:
    while True:
        # Get the current time
        time_elapsed = time.monotonic()

        # Read acceleration values
        acceleration = mpu.acceleration
        x_acceleration, y_acceleration, z_acceleration = acceleration

        # Check if the Pico is tilted
        tilt_threshold = 0.45  # Adjust this value based on your setup
        tilt = 1 if is_tilted(acceleration, tilt_threshold) else 0

        if z_acceleration < -tilt_threshold:
            # tilted, turn on the LED warning light
            led_2.value = True
        else:
            # not tilted, turn off the LED
            led_2.value = False
        # Prepare the data as a CSV string
        data_string = f"{time_elapsed:.2f},{x_acceleration:.3f},{y_acceleration:.3f},{z_acceleration:.3f},{tilt}\n"

        # Write the data to the data.csv file
        datalog.write(data_string)
        
        # Blink the onboard LED briefly
        led.value = True
        time.sleep(0.1)
        led.value = False

        # Flush the file to ensure data is saved
        datalog.flush()

        # Add a delay to control the sampling rate (4 samples per second)
        time.sleep(0.25)
