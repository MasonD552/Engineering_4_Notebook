#The code continuously reads acceleration data from the MPU6050, checks for approximately 90-degree tilts,
# activates the LED warning light when a tilt is detected. 
#It displays accelerometer data and the LED status on the serial monitor.
#type:ignore
import board
import busio
import adafruit_mpu6050

# Initialize I2C communication
sda_pin = board.GP14  #SDA pin
scl_pin = board.GP15  #SCL pin
i2c = busio.I2C(scl_pin, sda_pin)

# Initialize the MPU6050 sensor
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    # Read acceleration values
    acceleration = mpu.acceleration
    x_acceleration, y_acceleration, z_acceleration = acceleration
    
    # Round acceleration values to 3 decimal places
    x_acceleration = round(x_acceleration, 3)
    y_acceleration = round(y_acceleration, 3)
    z_acceleration = round(z_acceleration, 3)
    
    # Print rounded acceleration values to the serial monitor
    print(f"Acceleration (m/s²) - X: {x_acceleration}, Y: {y_acceleration}, Z: {z_acceleration}")
