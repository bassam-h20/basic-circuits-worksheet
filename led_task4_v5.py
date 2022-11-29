# -------------------------------------
#Author - Bassam Ali - Student: 21047697
# -------------------------------------

import RPi.GPIO as GPIO
import time

#Warnings and mode setting
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#LED and BUTTON Port
led1_port = 17
led2_port = 10
led3_port = 11
button1_port = 27
button2_port = 22

#while loop condition
i = 0


#set up buttons
GPIO.setup(button1_port, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button2_port, GPIO.IN, pull_up_down = GPIO.PUD_UP)


#set up LEDs
GPIO.setup(led1_port, GPIO.OUT)
GPIO.setup(led2_port, GPIO.OUT)
GPIO.setup(led3_port, GPIO.OUT)



#print("LED will be turned off until pressed.\n")
#print("When button is pressed, LED will be on for 5 secs.\n\n")


print("\n\nPress button 1 for any of the following:\n1 - light sequence 1\n2 - hold to turn off the LED")
print("\nPress button 2 for any of the following:\n1 - light sequence 2\n2 - hold to reverese the lighting sequence")
print("\n*You can reverse either light sequences mid sequence*")
print("*Just hold button 2 for it to reverse*")
print("\nIf you want to change the lighting sequence, please turn off the LED first")
print("\n")



while True:

    
    #BUTTON 1
    if GPIO.input(button1_port) == 0:
        i = 0

        print("Light Sequence 1 Begun")
        time.sleep(0.5)
        while True and GPIO.input(button1_port) != 0 and i != 1 :

            
            #LED 1
            #time.sleep(1)
            GPIO.output(led1_port, GPIO.HIGH)

            

            #if stopped at LED 1 - Red
            if GPIO.input(button2_port) == 0:
                print("Now flowing in opposite direction")
                time.sleep(1)
                GPIO.output(led1_port, GPIO.LOW)
                #LED 3 on
                GPIO.output(led3_port, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(led3_port, GPIO.LOW)
                #LED 2 on
                GPIO.output(led2_port, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(led2_port, GPIO.LOW)
                print("Opposite direction light sequence ended")

            time.sleep(1)
            #stopping circuit
            if (GPIO.input(button1_port) == 0):
                GPIO.output(led1_port, GPIO.LOW)
                GPIO.output(led2_port, GPIO.LOW)
                GPIO.output(led3_port, GPIO.LOW)
                print("Led Turned Off")
                i += i

            

            #if resumes as normal
            else:
                #resuming normal sequence
                #time.sleep(1)
                GPIO.output(led1_port, GPIO.LOW)

                


                #LED 2
                GPIO.output(led2_port, GPIO.HIGH)
                time.sleep(1)


                #if stopped at LED 2 - Yellow
                if GPIO.input(button2_port) == 0:
                    print("Now flowing in opposite direction")
                    time.sleep(1)
                    GPIO.output(led2_port, GPIO.LOW)
                    #LED 3 on
                    GPIO.output(led1_port, GPIO.HIGH)
                    time.sleep(1)
                    GPIO.output(led1_port, GPIO.LOW)
                    #LED 2 on
                    GPIO.output(led3_port, GPIO.HIGH)
                    time.sleep(1)
                    GPIO.output(led3_port, GPIO.LOW)
                    print("Opposite direction light sequence ended")

                #stopping circuit
                if (GPIO.input(button1_port) == 0):
                    GPIO.output(led1_port, GPIO.LOW)
                    GPIO.output(led2_port, GPIO.LOW)
                    GPIO.output(led3_port, GPIO.LOW)
                    print("Led Turned Off")
                    i += i

                #if resumes as normal
                else:
                    #resuming normal sequence
                    GPIO.output(led2_port, GPIO.LOW)

                     

                #if stopped at LED 3 - Green
                    GPIO.output(led3_port, GPIO.HIGH)
                    time.sleep(1)
                
                    if GPIO.input(button2_port) == 0:
                        print("Now flowing in opposite direction")
                        time.sleep(1)
                        GPIO.output(led3_port, GPIO.LOW)
                        #LED 3 on
                        GPIO.output(led2_port, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(led2_port, GPIO.LOW)
                        #LED 2 on
                        GPIO.output(led1_port, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(led1_port, GPIO.LOW)
                        print("Opposite direction light sequence ended")

                       #stopping circuit
                    if (GPIO.input(button1_port) == 0):
                        GPIO.output(led1_port, GPIO.LOW)
                        GPIO.output(led2_port, GPIO.LOW)
                        GPIO.output(led3_port, GPIO.LOW)
                        print("Led Turned Off")
                        i += i

                    #if resumes as normal
                    else:
                        #resuming normal sequence
                        GPIO.output(led3_port, GPIO.LOW)

        




        
        print("Light Sequence 1 Ended\n")
        time.sleep(2)



    #B.A#



    #BUTTON 2
    if GPIO.input(button2_port) == 0:

        print("Light Sequence 2 Begun")
        time.sleep(0.5)

        while True and GPIO.input(button1_port) != 0 and i != 1 :

            




            #LED 3 - Green
            GPIO.output(led3_port, GPIO.HIGH)
            time.sleep(1)


            #if stopped at LED 3 - Green
            if GPIO.input(button2_port) == 0:
                print("Now flowing in opposite direction")
                time.sleep(1)
                GPIO.output(led3_port, GPIO.LOW)
                #LED 3 on
                GPIO.output(led1_port, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(led1_port, GPIO.LOW)
                #LED 2 on
                GPIO.output(led2_port, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(led2_port, GPIO.LOW)
                print("Opposite direction light sequence ended")

            #stopping circuit
            if (GPIO.input(button1_port) == 0):
                GPIO.output(led1_port, GPIO.LOW)
                GPIO.output(led2_port, GPIO.LOW)
                GPIO.output(led3_port, GPIO.LOW)
                print("Led Turned Off")
                i += i

            #if resumes as normal
            else:
                #resuming normal sequence
                GPIO.output(led3_port, GPIO.LOW)


                #LED 2 - Yellow
                GPIO.output(led2_port, GPIO.HIGH)
                time.sleep(1)

                #if stopped at LED 2 - Yellow
                if GPIO.input(button2_port) == 0:
                        print("Now flowing in opposite direction")
                        time.sleep(1)
                        GPIO.output(led2_port, GPIO.LOW)
                        #LED 3 on
                        GPIO.output(led3_port, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(led3_port, GPIO.LOW)
                        #LED 2 on
                        GPIO.output(led1_port, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(led1_port, GPIO.LOW)
                        print("Opposite direction light sequence ended")

                #stopping circuit
                if (GPIO.input(button1_port) == 0):
                    GPIO.output(led1_port, GPIO.LOW)
                    GPIO.output(led2_port, GPIO.LOW)
                    GPIO.output(led3_port, GPIO.LOW)
                    print("Led Turned Off")
                    i += i

                #if resumes as normal
                else:
                    #resuming normal sequence
                    GPIO.output(led2_port, GPIO.LOW)


                    #LED 1 - Red
                    GPIO.output(led1_port, GPIO.HIGH)
                    time.sleep(1)

                    #if stopped at LED 1 - Red
                    if GPIO.input(button2_port) == 0:
                        print("Now flowing in opposite direction")
                        time.sleep(1)
                        GPIO.output(led1_port, GPIO.LOW)
                        #LED 3 on
                        GPIO.output(led2_port, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(led2_port, GPIO.LOW)
                        #LED 2 on
                        GPIO.output(led3_port, GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(led3_port, GPIO.LOW)
                        print("Opposite direction light sequence ended")

                    #stopping circuit
                    if (GPIO.input(button1_port) == 0):
                        GPIO.output(led1_port, GPIO.LOW)
                        GPIO.output(led2_port, GPIO.LOW)
                        GPIO.output(led3_port, GPIO.LOW)
                        print("Led Turned Off")
                        i += i


                    #if resumes as normal
                    else:
                        #resuming normal sequence
                        GPIO.output(led1_port, GPIO.LOW)


        print("Light Sequence 2 Ended\n")
        time.sleep(2)

    
    elif GPIO.input(button2_port) == 1:
        GPIO.output(led1_port, GPIO.LOW)
        GPIO.output(led2_port,GPIO.LOW)
        GPIO.output(led3_port,GPIO.LOW)
        #print("LED turned off until button pressed.")
        time.sleep(0.01)
