
# This program allows you to input three sets of (x, y) coordinates for the vertices
# of a triangle, calculates its area, and displays it on a 128x64 OLED screen.
# After displaying the triangle and its area, the program waits for 10 seconds
# and then prompts for new coordinates.


#type: ignore
# Import libraries
import time
import busio
import board
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
from adafruit_displayio_ssd1306 import SSD1306
from adafruit_display_text.label import Label
import terminalio
import displayio

displayio.release_displays()

# Initialize I2C communication
sda_pin = board.GP14  # Replace with your SDA pin
scl_pin = board.GP15  # Replace with your SCL pin
i2c = busio.I2C(scl_pin, sda_pin)

# Initialize the display
display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)
display = SSD1306(display_bus, width=128, height=64)

origin_x = 64  # Set the origin (center of the screen)
origin_y = 32

# Function to draw a line on the OLED screen
def draw_line(x1, y1, x2, y2, color=0xFFFF00):
    line = Line(int(x1), int(y1), int(x2), int(y2), color=color)
    return line

# Create a label to display the area
area_label = Label(terminalio.FONT, x=5, y=5, text="", color=0xFFFF00)

# Define a function to calculate the area of a triangle
def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(0.5 * ((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))))

# Function to draw a triangle on the OLED screen relative to the origin
def draw_triangle(x1, y1, x2, y2, x3, y3, origin_x, origin_y):
    triangle = Triangle(
        int(origin_x + x1), int(origin_y - y1),
        int(origin_x + x2), int(origin_y - y2),
        int(origin_x + x3), int(origin_y - y3),
        outline=0xFFFF00
    )
    return triangle

# Function to draw a circle (origin) on the OLED screen
def draw_circle(x, y, radius):
    circle = Circle(int(x), int(y), radius, outline=0xFFFF00)
    return circle

# Main function to handle user input, calculate area, and draw on the OLED screen
while True:
    area_label = Label(terminalio.FONT, x=5, y=5, text="", color=0xFFFF00)
    try:
        # Initialize display groups for each iteration
        splash = displayio.Group()
        
        x1, y1 = map(float, input("Enter the first coordinates (x,y): ").split(","))
        x2, y2 = map(float, input("Enter the second coordinates (x,y): ").split(","))
        x3, y3 = map(float, input("Enter the third coordinates (x,y): ").split(","))

        # Check if the points form a valid triangle (not collinear)
        if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) != 0:
            area = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
            area_label.text = f"Area: {area:.2f} km²"
            print(f"Area: {area:.2f} km²")
            
            # Draw the triangle and the origin
            splash.append(draw_triangle(x1, y1, x2, y2, x3, y3, origin_x, origin_y))
            splash.append(draw_circle(origin_x, origin_y, 2))
            splash.append(area_label)
            # Draw the Axes
            splash.append(draw_line(0, 32, 128, 32))
            splash.append(draw_line(64, 0, 64, 64))

            # Create labels for axes
            x_label = Label(terminalio.FONT, text="X", color=0xFFFF00)
            x_label.x = 2
            x_label.y = 38
            splash.append(x_label)
            y_label = Label(terminalio.FONT, text="Y", color=0xFFFF00)
            y_label.x = 66
            y_label.y = 60
            splash.append(y_label)

            # Show the display group
            display.show(splash)
            
            # Wait for 5 seconds
            time.sleep(5)

            #Clear Screen
            splash.pop
        else:
            print("These points are not a valid triangle. Please try again, and make sure you are using the x, y syntax.")
    except ValueError:
        print("Invalid input. Please enter coordinates in (x,y) format separated by commas.")
