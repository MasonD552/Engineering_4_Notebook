# type: ignore
import board
import busio
import adafruit_mpu6050
import time 
# Initialize I2C communication
sda_pin = board.GP14  # Replace with your SDA pin
scl_pin = board.GP15  # Replace with your SCL pin
i2c = busio.I2C(scl_pin, sda_pin)

# Initialize the MPU6050 sensor
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    # Read acceleration values
    acceleration = mpu.acceleration
    x_acceleration, y_acceleration, z_acceleration = acceleration
    
    # Print acceleration values to the serial monitor
    print(f"Acceleration (m/s²) - X: {x_acceleration}, Y: {y_acceleration}, Z: {z_acceleration}")
    time.sleep(0.25)