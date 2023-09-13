# Engineering_4_Notebook

![jose-ramirez-tim-anderson (1)](https://github.com/MasonD552/Engineering_4_Notebook/blob/main/images/jose-ramirez-tim-anderson.gif)
&nbsp;

## Table of Contents
* [Circuit Python](Circuit_Python)
* [LED_Blink](#LED_Blink)
* [LaunchPad_Part 1](#LaunchPad_Part_1)
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
## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;


