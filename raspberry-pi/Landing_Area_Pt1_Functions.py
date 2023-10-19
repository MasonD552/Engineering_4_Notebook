# Define a function to calculate the area of a triangle using its coordinates
def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    # Calculate the area of the triangle using the coordinates
    return abs(0.5 * ((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))))


# Define a function to get user input for three sets of coordinates (x1, y1), (x2, y2), (x3, y3)
def get_user_input():
    while True:
        try:
            x1, y1 = map(
                float,
                input("Enter the first coordinates (x,y): ").split(","))
            x2, y2 = map(
                float,
                input("Enter the second coordinates (x,y): ").split(","))
            x3, y3 = map(
                float,
                input("Enter the third coordinates (x,y): ").split(","))
            return x1, y1, x2, y2, x3, y3
        except ValueError:
            print(
                "Invalid input. Please enter coordinates in (x,y) format separated by commas."
            )


# Start an  loop to keep asking for input and calculating triangle areas
while True:
    x1, y1, x2, y2, x3, y3 = get_user_input()

    # Check if the points form a valid triangle (not collinear)
    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) != 0:
        area = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
        print(
            f"The area of the triangle with vertices ({x1},{y1}), ({x2},{y2}), ({x3},{y3}) is {area} square km."
        )
    else:
        print(
            "These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!"
        )
