# Digital Design Worksheet


### Task 1:
###### Built a LED circuit using the following components:
1. 330 Ohm Resistor
2. An LED
3. Bread Board
4. Coin Cell Battery
5. Coil wire

* Circuit fully functional
![led circuit 1](./LED_circuit.jpeg)


### Task 2 :
######  Used the Raspberry Pi as the power source for the LED Circuit and implemented code (code file: led_task2.py) to allow the red LED  light to turn on for 1 second and turn off. Connected wire to port 17.
* Circuit is fully functional
![led circuit 2](./LED_circuit2.jpeg)


### Task 3:
######  Implemented code to blink each LED light for 2 seconds in the order (Red, Yellow, Green), (code file: led_task3.py).
1. Added two more LED lights, two 330 ohm resistors, 4 wires. 
2. Yellow LED light connected to port 10, and Green LED light connected to port 11

* Circuit is fully functional
![led circuit 3](./LED_circuit3.jpeg)

### Task 4:
###### Built on my previous circuit and added the following to it:

1. 2 buttons each with a 10 KOhm resistor
2. More Coil wires

- Button 1 allows the user to turn the LED lights on or off

- Button 2 allows the user to turn to LED lights in a reverse sequence, or change the direction of the light sequence


![led circuit 4](./LED_circuit4.jpeg)

![program output](./led_demo.png)
- The screenshot above shows the output from the program and the input of the buttons


### Task 5:
###### A program that calculates Voltage, Current, Resistance and Serial Resistance (in a series circuit)

- An example of successful output shown below

![program output](./task5_demo.png)

- An example of an assertion error shown below (2 images)
- The correct current calculation is 0.6 Amps according to the values entered by the user, but is changed below to 0.7, so it outputs an assertion error and prints a "test failed" message

![terminal output 1](./task5_demo2.png) ![terminal output 2](./task5_demo3.png)


