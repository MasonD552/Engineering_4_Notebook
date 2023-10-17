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
* [Crash Avoidance Pt 3](#Crash_Avoidance_Pt_3)
* [FEA_Part_1_BeamDesign](#FEA_Part_1_BeamDesign)
* [FEA_Part_3_Analysis](#FEA_Part_3_Analysis)
* [FEA_Part_4_Iterative_Design](#FEA_Part_4_Iterative_Design)
* [FEA_Part_5_Final_Beam](#FEA_Part_5_Final_Beam)
  
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

[Crash Avoidance Pt. 1 Code](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_Accelerometer.py)

### Reflection

😎 The coolest part of this assignment was definitely diving into the world of f-strings! 🚀 F-strings are really like the superheroes of Python formatting, making everything appear incredibly organized and simplifying the task of printing multiple values in a single statement. 🦸‍♂️💥

Imagine you're juggling a bunch of variables and data, and you want to display them in a clear and neat way. That's where f-strings come to the rescue! You can effortlessly insert variables and expressions directly into your strings, using curly braces {} to enclose them. This not only keeps your code clean but also makes it super readable. 📚✨

For instance, if you have variables `name` and `age`, you can print them together in a sentence like this:

```python
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

The values of `name` and `age` seamlessly integrate into your string, making it a breeze to understand and maintain. 🙌

But wait, there's more! 🎉 You also mentioned learning about the `round()` function. 📏 This nifty function is like your personal math wizard, allowing you to round numerical values to a specific decimal place. 🧙‍♂️✨

Let's say you have a float like `pi = 3.14159265359`, and you only want to display it with two decimal places:

```python
pi = 3.14159265359
rounded_pi = round(pi, 2)
print(f"The rounded value of pi is approximately {rounded_pi}.")
```

The `round()` function does the magic here, rounding `pi` to two decimal places and giving you a clean and precise result. 🎩🔮

So, f-strings and `round()` are two powerful tools in your Python arsenal that make your code more organized, readable, and precise. 🐍💻🚀

&nbsp;
## Crash_Avoidance_Pt_2

### Assignment Description
This reads acceleration values from an MPU6050 accelerometer connected to a Raspberry Pi Pico.
The acceleration values are rounded to three decimal places and continuously printed to the serial monitor if the accelerometer is rotated 90 degrees then a red LED will turn on. 
Connect a battery to make it so that the board runs wirelessly. 

### Evidence 

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/crashavoidancelightpower.gif"  width="80%" height="50%">

### Wiring

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/WIN_20230922_13_37_43_Pro.jpg"  width="50%" height="20%">

### Code

[Crash Avoidance Pt. 2 Code](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_Light%2BPower.py)

### Reflection
In this assignment, we were tasked to build on the last assignment with the MPU6050. We had to add on by making it battery-powered and adding an LED.

📊 Threshold Creation 📏

The first thing I did was create a threshold. This threshold was a variable that would be set to an angle of 90 degrees. When the accelerometer went past 90 degrees, it would turn on the LED.

💡 LED Logic Challenge 💭

The hardest part was figuring out whether to have the threshold be greater than the x and y variables or just z. So I decided to do just z, then it worked.

👏 Credits to Mr. Miller 👨‍🏫

I give credit to Mr. Miller as the only person to be able to get the battery out of the battery connector.


&nbsp;
## Crash_Avoidance_Pt_3

### Assignment Description
This reads acceleration values from an MPU6050 accelerometer connected to a Raspberry Pi Pico.
The acceleration values are rounded to three decimal places and continuously printed to the serial monitor if the accelerometer is rotated 90 degrees then a red LED will turn on. 
Connect a battery to make it so that the board runs wirelessly. 
Print angular velocity values to OLED.

### Evidence 

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/OLEDCrashAvoidance.gif"  width="80%" height="50%">

### Wiring

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/OLED_CrashAccel.jpg"  width="50%" height="20%">

### Code

[Crash Avoidance Pt. 3 Code](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_OLED.py)

### Reflection

🚁 **Raspberry Pi Pico Crash Avoidance Module with MPU6050 and OLED** 🛠️

In this assignment, I was able to get the board to be rotated 90 degrees then turn on an LED and print the angular velocity values to an OLED.

🧩 **Address Conundrum** 🤔

The hardest part of this assignment was figuring out the address of the OLED vs. the MPU6050. I found that the OLED's address was 0x3D, and the MPU's address was 0x68. When I realized that I was supposed to put the SDA and SCL into the same pin, it worked. 

📊 **Displaying Data** 📝

I was also able to figure out how to print my values on the board and have it say "LED Status:". In general, this assignment taught me how to print onto the OLED.


&nbsp;
## FEA_Part_1_BeamDesign

### Assignment Description

This assignment explores engineering tradeoffs by designing a 3D-printed beam to maximize load-bearing capacity while adhering to specific constraints. The goal is to create a beam that avoids breaking or excessive bending(beyond 35mm) and satisfies the following requirements:


* Use the provided attachment block without modifications. 
* Ensure full engagement with the holder. 
* Follow the example eye bolt mounting geometry. 
* Place the eyebolt hole's center 180 mm from the attachment block's front face. 
* Prevent any part of the beam from extending below the attachment block. 
* Maintain vertical angles >= 45 degrees relative to the horizontal plane. 
* Use PLA material. 
* Keep the entire beam, including the attachment block, under 13 grams in weight.


### Part Link 

[Beam Onshape Link](https://cvilleschools.onshape.com/documents/dd59f389e3f75e6c83491e1b/w/01511871c7c3bde9b77a0bbb/e/06a6eb71a015865d3f97e651?renderMode=0&uiState=651c4c872c3aec7eb76807df). 

### Part Image

![BeamOnshapePic](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/Beam%20Starter%20%2B%20Holder%20Copy%201.png)

### Reflection

This assignment was enjoyable and challenging for us. We took inspiration on this design from the I beam which is the most substantial beam so we wanted to incorporate it into our design. The problem with the I beam was that it had too much of an overhang so we redesigned it as a Y beam for support. Another issue we ran into was having too much weight, in the beginning, the beam was very solid but it had way too much weight. For the cut down we had to add several circles and rectangular holes which affected the stability of the beam. My advice is for next time to create a little simpler design to avoid all the holes that we had to put, although I think our Y beam design was sturdy.

&nbsp;
## FEA_Part_3_Analysis

### Points Most Likely to Fail

Our beam did well against the FEA but there is definitely room for improvement. In the base of our beam the bottom as well as the top are under pressure and it would snap there. The problem is the sharp corners and lack of materials, we are going to fix it by adding fillets and slimming it down to bulk up certain parts. Another problem we faced was the stress of the line of circles because they are too close together. 


### Part Link 

[Beam Onshape Link](https://cvilleschools.onshape.com/documents/dd59f389e3f75e6c83491e1b/w/01511871c7c3bde9b77a0bbb/e/06a6eb71a015865d3f97e651?renderMode=0&uiState=651c4c872c3aec7eb76807df). 

### Part Image

<figure>
    <img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/FEAPART3AnalysisvonMises%20stress.png"
         alt="BeamStressAnalysis">
    <figcaption>von Mises stress(MPa)</figcaption>
</figure>
<figure>
    <img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/FEAPART3AnalysisDisplacement.png"
         alt="BeamDisplacementAnalysis">
    <figcaption>Displacement(mm)</figcaption>
</figure>
<figure>


&nbsp;
## FEA_Part_4_Iterative_Design

### What we did to improve
9.25187% decrease in displacement

18.7901%decrease in von mises stress

### Part Link 

[Beam Onshape Link](https://cvilleschools.onshape.com/documents/dd59f389e3f75e6c83491e1b/w/01511871c7c3bde9b77a0bbb/e/06a6eb71a015865d3f97e651?renderMode=0&uiState=651c4c872c3aec7eb76807df). 

### Part Image

<figure>
    <img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/part%204%20vonmises.png"
         alt="BeamStressAnalysis">
    <figcaption>von Mises stress(MPa)</figcaption>
</figure>
<figure>
    <img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/part4%20displacement.png"
         alt="BeamDisplacementAnalysis">
    <figcaption>Displacement(mm)</figcaption>
</figure>
<figure>

### Reflection
Going from version one we knew we had to get rid of the overhangs we didn't realize we had. We saw that in the FEA simulation, the most stress was on the top part. We also noticed that there was not a lot of pressure where the clip was. So we moved some of the weight from the tip higher up. We also got rid of the overhangs, we used more fillets and chamfers to make the edges stronger. We also wanted to decrease stress and we did that by decreasing the stress by 18.7901% and 9.25% for the displacement. We were able to make out beam pretty strong. Some of the weak spots were the connection to the connector piece and the circle/holes were also a weak spot. In all, we were pretty successful in creating a beam that was able to hold weight.


&nbsp;
## FEA_Part_5_Final_Beam

### What we did to improve
9.25187% decrease in displacement

18.7901%decrease in von mises stress

### Part Link 

[Beam Onshape Link](https://cvilleschools.onshape.com/documents/dd59f389e3f75e6c83491e1b/w/01511871c7c3bde9b77a0bbb/e/06a6eb71a015865d3f97e651?renderMode=0&uiState=651c4c872c3aec7eb76807df). 

### Part Image & Videos
![Slowmo gif](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/ezgif.com-video-to-gif%20(2).gif)

<figure>
    <img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/part%204%20vonmises.png"
         alt="BeamStressAnalysis">
    <figcaption>von Mises stress(MPa)</figcaption>
</figure>
<figure>
    <img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/part4%20displacement.png"
         alt="BeamDisplacementAnalysis">
    <figcaption>Displacement(mm)</figcaption>
</figure>
<figure>

### Reflection

&nbsp;



