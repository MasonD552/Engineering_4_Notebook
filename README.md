# Engineering_4_Notebook

![jose-ramirez-tim-anderson (1)](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/jose-ramirez-tim-anderson.gif)
&nbsp;

## Table of Contents
* [Circuit Python](Circuit_Python)
* [LED_Blink](#LED_Blink)
* [LaunchPad_Part 1](#LaunchPad_Part_1)
* [LaunchPad_Part 2](#LaunchPad_Part_2)
* [LaunchPad_Part 3](#LaunchPad_Part_3)
* [LaunchPad_Part 4](#LaunchPad_Part_4)
* [Crash_Avoidance_Pt_1](#Crash_Avoidance_Pt_1)
* [Crash Avoidance Pt 2](#Crash_Avoidance_Pt_2)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;
# Circuit Python
![PinMap](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/Screenshot%202023-09-12%20201819.png)

## LED_Blink

### Assignment Description

Getting the board led to blinking on and off every second.

### Evidence 

![ezgif-1-4ff8ace096](https://github.com/MasonD552/Engineering_4_Notebook/assets/91158978/dd274ec4-a577-4c9a-b4ca-1d311f63547d)


### Wiring

No Wiring

### Code

[Code for LED Blink](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/LED_Blink.py)
### Reflection

The LED code wasn't particularly challenging; it mostly involved reviewing concepts from the previous year. The only tricky part was the process of uploading it to the board, which differed slightly as I had to manually drag the code into the "code.py" file instead of simply pressing the F5 key.

&nbsp;


## LaunchPad_Part_1

### Assignment Description

Make a count down go from 10 -> 1 and then after one(0) say LIFTOFF. Example: 10 9 8 7 6 5 4 3 2 1 Liftoff

### Evidence 
![Countdown](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/ezgif.com-video-to-gif.gif)

### Wiring

No Wiring

### Code

[Code for LaunchPad Countdown](https://github.com/MasonD552/Engineering_4_Notebook/blob/0d7bec4f410bc323a3a9192ba7742061eb506b4a/raspberry-pi/LaunchPadPt1_Countdown.py)
### Reflection

A for loop in Python is like a friendly robot that helps you do repetitive tasks without going crazy. When you see for x in range(10, 0, -1):, it's like telling the robot, "Hey, I want to count from 10 down to 1, and I want you to do something in between each number."

The robot starts at 10 because you said so and then counts down one by one, all the way to 1. While it does this, you can make it do things, like pausing for a second with time.sleep(1) and printing the current number. And when it reaches 1, you can make it do something special, like shouting "Liftoff!"

&nbsp;
## LaunchPad_Part_2

### Assignment Description
It indicates two LEDs, one red (ledr) and one blue (ledb), and uses them to perform a countdown. The countdown starts from 10 and decrements by 1 every half second until it reaches 1, at which point it prints "Liftoff" and turns on the blue LED for 2 seconds.

### Evidence 

![LEDCOUNTDOWN](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/ezgif.com-video-to-gif%20(1).gif)
### Wiring
<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/image_67140865.JPG"  width="50%" height="20%">

### Code

[LED Countdown Code](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/LaunchPadPt2_LEDS.py)

### Reflection

The LED launch pad countdown is pretty straightforward. I knew that all I had to do was tell the board I had two leds and where they were plugged in. Then I had to wire the leds correctly. I had a little trouble with one of my leds. I accidentally plugged the longer leg in the - and the shorter leg in the positive but I then realized and switched them. I also noticed that Jinho's code was being finicky so I tried helping him. We soon realized he didn't save his code to the board.

&nbsp;

## LaunchPad_Part_3

### Assignment Description

The countdown starts from 10 and decreases by 1 every second until it reaches 0 (liftoff). It prints the countdown to the serial monitor, blinks a red LED each second, and turns on a green/blue LED to signify liftoff. If the button is pressed during the countdown process, it aborts, and another button press starts the countdown again.

### Evidence 

![ButtonCOUNTDOWN](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/ButtonCountdown.gif)

### Wiring

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/Countdownbuttonwiring.JPG"  width="50%" height="20%">

### Code

[Button Countdown Code](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/LaunchPadPt3_Button.py)

### Reflection
For this assignment, I was able to do the 🔥 SPICY VERSION 🔥 by when the button is pressed it ✋ aborts and then 🔄 resets the code back up to the top and waits for the button to be pressed again. I had trouble figuring out how to get the code not to abort and start the countdown at the same time. I solved this by using different states. I also had 🤔 the issue of not knowing how to get the code to reset to the top, so I put an if statement at the bottom so that if liftoff or abort happened, it would reset the code. 🚀🔁💡


&nbsp;
## LaunchPad_Part_4

### Assignment Description

The countdown starts from 10 and decreases by 1 every second until it reaches 0 (liftoff). It prints the countdown to the serial monitor, blinks a red LED each second, and turns on a green LED to signify liftoff. A servo motor slowly retracts the launch tower starting at 3 seconds until it reaches 180 degrees at takeoff. If the button is pressed during the countdown process, it aborts, and another button press starts the countdown again.

### Evidence 

![ServoCOUNTDOWN](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/countdownservo.gif)

### Wiring

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/IMG_2525.jpg"  width="50%" height="20%">

### Code

[Servo Countdown Code](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/LaunchPadPt4_Servo.py)

### Reflection

One of the main challenges I encountered was synchronizing the countdown, servo rotation, and button press handling. To address this, I introduced different states in the code. Initially, I had to ensure that the countdown didn't start immediately upon pressing the button. I resolved this by utilizing a state flag that allowed the countdown to commence only after the second button press, creating a smooth user experience. ✋🔄

Another significant challenge was coordinating the servo's rotation to start at 3 seconds and continuously sweep until liftoff. To tackle this, I employed a flag that signaled the initiation of servo rotation precisely when the countdown reached 3 seconds. This flag-controlled servo movement ensured that the servo gradually reached 180 degrees by liftoff, aligning with the mission commander's requirements. 🤖🕒 But I was unable to get it to start at 3 seconds. So I did not do the 3 seconds.

Furthermore, I handled button presses during the countdown, allowing for an "abort" action. Upon detecting an abort, the code reset its state, preparing for another countdown. This functionality was achieved by incorporating state management in the code. 🔁💡

In the end, the code successfully orchestrated a synchronized countdown, servo rotation, and button interaction, meeting the requirements for a controlled liftoff sequence. 🌟


&nbsp;
## Crash_Avoidance_Pt_1

### Assignment Description
This reads acceleration values from an MPU6050 accelerometer connected to a Raspberry Pi Pico.
The acceleration values are rounded to three decimal places and continuously printed to the serial monitor

### Evidence 

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/CrashAvoidancePt1.gif"  width="80%" height="50%">

### Wiring

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/WIN_20230919_13_42_01_Pro.jpg"  width="50%" height="20%">

### Code

[CrashAvoidancept1Code](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_Accelerometer.py)

### Reflection



&nbsp;
## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on the knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;


