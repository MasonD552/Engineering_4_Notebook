# type: ignore
import board
import time

print("Countdown")  # Print "Countdown" 
time.sleep(1) # Pause for 1 second.

for x in range(10, 0, -1): # Start a for loop with 'x' ranging from 10 down to 1 (inclusive), decreasing by 1 in each iteration.
    time.sleep(1) # Pause for 1 second.
    print(x)
    
    if x == 1:
        time.sleep(1)
        print("Liftoff")# Print "Liftoff" to the console when 'x' is equal to 1 