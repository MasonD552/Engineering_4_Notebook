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
* [Landing_Area_Part_1(Functions)](#Landing_Area_Part_1_Functions)
* [Landing_Area_Part_2(Plotting)](#Landing_Area_Part_2_Plotting)
* [Morse_Code_Pt1(Translation)](#Morse_Code_Pt1_Translation)
* [Morse_Code_Pt2(Transmission)](#Morse_Code_Pt2_Transmission)
* [Data Pt 1(Storage)](#Data_Pt1_Storage)
* [Data Pt 2(Analysis)](#Data_Pt2_Analysis)
* [Crash Avoidance Pt 4](#Crash_Avoidance_Pt_4)
  
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

18.7901% decrease in von mises stress

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
1.97857%increase in displacement

0.428477% increase in von mises stress

### Part Link 

[Beam Onshape Link](https://cvilleschools.onshape.com/documents/dd59f389e3f75e6c83491e1b/w/01511871c7c3bde9b77a0bbb/e/06a6eb71a015865d3f97e651?renderMode=0&uiState=651c4c872c3aec7eb76807df). 

### Part Image & Videos
![Slowmo gif](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/ezgif.com-video-to-gif%20(2).gif)

<figure>
    <img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/finalbeamvonmises.png"
         alt="BeamStressAnalysis">
    <figcaption>von Mises stress(MPa)</figcaption>
</figure>
<figure>
    <img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/finalnbeamdeformation.png"
         alt="BeamDisplacementAnalysis">
    <figcaption>Displacement(mm)</figcaption>
</figure>
<figure>

### Reflection
For this assignment we were able to make our beam able to hold more weight, meaning our stress had a higher tolerance, but the displacement worsened from the last assignment. If we were to change our beam I think we would make the thickness of the beam thicker. We could also have done multiple tests to ensure the beam worked more in FEA. In total, I was pretty pleased with how our beam turned out.


&nbsp;

## Landing_Area_Part_1_Functions

### Assignment Description

The code must ask for the user to input a set of three coordinates in (x,y) format
The triangle area must be determined using a function
If the user inputs coordinates incorrectly (letters or improper format) the code should return to the input stage, it should not throw an error or exit the script
The triangle area must be printed to the screen in this format: “The area of the triangle with vertices (x,y), (x,y), (x,y) is {area} square km.
The code must return to the input stage after printing the area, and wait for user input.

### Evidence 

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/Landing%20area%20pt1.gif"  width="80%" height="50%">


### Code

[Landing_Area_Part_1_Functions_Code](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/Landing_Area_Pt1_Functions.py)

### Reflection
In this assignment, I was able to make the function tell the script to find the area of three vertices of the triangle(x1,y1), etc. When I started I completely glanced over the part where it asks you to do the .split part. If I hadn't asked Mr. Miller I would have of submitted the wrong thing. I also made it so that it would check to see if the form is improper or if the triangle is linear(not a triangle) it would say it was invalid. I finally got it so that I could input the coordinates like 1,2 then 2,9 then 30, 20 and I didn't have to input them in one line.



&nbsp;
## Landing_Area_Part_2_Plotting

### Assignment Description

The code must ask for the user to input a set of three coordinates in (x,y) format
of a triangle, calculates its area, and displays it on a 128x64 OLED screen.
After displaying the triangle and its area, the program waits for 5 seconds and then prompts for new coordinates.


### Evidence 

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/Landing%20area%20plotting%20gif.gif"  width="40%" height="50%">

### Wiring

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/LA2wiring.jpg"  width="50%" height="5%">


### Code

[Landing_Area_Part_2_Plotting_Code](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/Landing_Area_Pt2_Plotting.py)

### Reflection
In this assignment, I made the function tell the script to find the area of three vertices of the triangle(x1,y1), etc. I was able to take those vertices and plug them into new functions Circle(), Triangle(), Line(). I also learned more about how the OLED works with different display groups. I was also able to learn how the origin is graphed on the OLED. Your y values go down and x values go to the right. I was also able to use where the origin is set to graph the x axis and y axis. I kept having issues with graphing the x and y axis so I only made one display group. Then my triangle wouldn't clear so I commented my try and went to see why my code kept coming up with an error.



&nbsp;

## Morse_Code_Pt1_Translation

### Assignment Description
Create a Python script that acts as a Morse code translator. It utilizes a provided dictionary to map English letters and numbers to their Morse code equivalents. The code takes user input for text and translates it into Morse code, with spaces between letters and slashes between words. The program allows the user to exit by typing "-q". This assignment demonstrates text processing, dictionary usage, and interactive user input handling in Python.

### Evidence 

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/Morse%20code%20translation.gif"  width="80%" height="50%">



### Code

[Morse Code Translation Code](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/Morse_Code_Pt1_Translation.py)

### Reflection

This was a pretty simple assignment as I have used dictionaries in code before at home so this was a good review of dictionaries. Using the break tool was interesting as I was able to get it so that it would break and go back to the top after a text was translated. The only confusing part was when I went to check the translation online it came up with some weird translations like "Hell# Wo#ld". It would do that on one of the websites but others wouldn't do that. I wasn't too worried as I knew my code worked.


&nbsp;
## Morse_Code_Pt2_Transmission

### Assignment Description
Create a Python script that acts as a Morse code translator. It utilizes a provided dictionary to map English letters and numbers to their Morse code equivalents. The code takes user input for text and translates it into Morse code, with spaces between letters and slashes between words. The program allows the user to exit by typing "-q". Then it takes each dot or dash and transmits it to a led. The space between each word is converted to time.sleep() to add a space between each word.
### Evidence 

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/Morse%20Code%20Part%202%20Transmission.gif"  width="80%" height="50%">

### Wiring
![MorseCode wiring transmission](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/Wiring%20morse%20code%20transmission.jpg)

### Code

[Morse Code Translation Code](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/Morse_Code_Pt1_Translation.py)

### Reflection

This was a pretty simple assignment as I have used dictionaries in code before at home so this was a good review of dictionaries. Using the break tool was interesting as I was able to get it so that it would break and go back to the top after a text was translated. The only confusing part was when I went to check the translation online it came up with some weird translations like "Hell# Wo#ld". It would do that on one of the websites but others wouldn't do that. I wasn't too worried as I knew my code worked.


&nbsp;
## Data_Pt1_Storage

### Assignment Description
Create code using the crash avoidance code to log data to the data.csv file. Switch between Code and Data Modes using GP0. 
Records time, XYZ acceleration, and tilt status. LED blinks on data save. Retrieve data on the computer.

### Evidence 

<img src="https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/Datastorage%20gif.gif"  width="80%" height="50%">

### Wiring
![DataStorageWiring](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/Wiringdatastorage.png)

### Code

[Data Storage Code](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/raspberry-pi/Data_Pt1_Storage.py)

### Reflection
This assignment was hard, I kept running into a lot of difficulty with my board completely resetting itself, and I also couldn't get my switch to work. I eventually got everything to work. For the board factory resetting itself, I found out that when I had the battery switched on and I went to plug the board into the computer I would notice the code.py file said "Hello World" Then I checked and saw that my lib file was empty. I made a lib file so when I insert new lib folders/files onto my board I would have them saved so I would have to go fetch them. The switch situation was easy I had to find a new switch and I also realized that to switch from data to code mode you have to switch AND unplug and replug in the board. **To avoid in the future: DON'T HAVE BATTERY ON OR PLUGGED IN WHEN PLUGGED INTO COMPUTER**


&nbsp;

## Data_Pt2_Analysis

### Assignment Description

Generate a line chart depicting time on the horizontal axis and acceleration on the vertical axis, incorporating X, Y, and Z accelerations on a single plot. Provide clear titles and axis labels, including units.
Construct a chart illustrating time on the X-axis and the tilt status of the Pico on the Y-axis. Ensure to include informative titles and axis labels, specifying the units.

### Evidence 

[Link to Data Analysis Google Sheet](https://docs.google.com/spreadsheets/d/1ylrBX09e-f8WUV6Asc_nx6c_sdjhclWAiN0MOl-M2ZY/edit?usp=sharing)

<img width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTE2E6SyzK33knWjsTKGYlb96mEzAAzaLCqcVL6pIy5E3zxwTn1wECxurqkPyP5jJRfy3l8Ete5RECR/pubchart?oid=691265260&amp;format=image">


<img width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTE2E6SyzK33knWjsTKGYlb96mEzAAzaLCqcVL6pIy5E3zxwTn1wECxurqkPyP5jJRfy3l8Ete5RECR/pubchart?oid=801704479&amp;format=image">

### Reflection
This assignment was straightforward I had to copy the data from the data.csv file into a Google Sheets document then I had to format it into something way easier to read. I also had to make two charts. One chart shows the X Y and Z acceleration and the other shows when the PICO was tilted. I wanted to figure out how to get the tilt graph to have a step from 0 -> 1 instead of steps by 0.25. So I figured out how to make the step size by 1.


&nbsp;
