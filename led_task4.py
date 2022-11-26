# -------------------------------------
#Author - Bassam Ali - Student: 21047697
# -------------------------------------

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#LED and BUTTON Port
led1_port = 17
led2_port = 10
led3_port = 11
button1_port = 27
button2_port = 22

#set up buttons
GPIO.setup(button1_port, GPIO.IN)
#button1_state = GPIO.input(button1_port)
GPIO.setup(button2_port, GPIO.IN,)


#set up LEDs
GPIO.setup(led1_port, GPIO.OUT)
GPIO.setup(led2_port, GPIO.OUT)
GPIO.setup(led3_port, GPIO.OUT)



#print("LED will be turned off until pressed.\n")
#print("When button is pressed, LED will be on for 5 secs.\n\n")


print("\n\nPress button 1 for light sequence 1")
print("Press button 2 for light sequence 2")
print("\n*You can reverse either light sequences mid sequence*")
print("*Just hold button 2 for few seocnds for it to reverse*")


while True:


    #BUTTON 1
    if GPIO.input(button1_port) == 0:

        print("Light Sequence 1 Begun")



        #LED 1
        GPIO.output(led1_port, GPIO.HIGH)
        time.sleep(1)


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


    
        #if resumes as normal
        else:
            #resuming normal sequence
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

                #if resumes as normal
                else:
                    #resuming normal sequence
                    GPIO.output(led3_port, GPIO.LOW)






        print("Light Sequence 1 Ended\n")


#@Basyou20

    #BUTTON 2

    if GPIO.input(button2_port) == 0:

        print("Light Sequence 2 Begun")




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


                #if resumes as normal
                else:
                    #resuming normal sequence
                    GPIO.output(led1_port, GPIO.LOW)


        print("Light Sequence 2 Ended\n")


    
    elif GPIO.input(button1_port) == 1:
        GPIO.output(led1_port, GPIO.LOW)
        GPIO.output(led2_port,GPIO.LOW)
        GPIO.output(led3_port,GPIO.LOW)
        #print("LED turned off until button pressed.")
        time.sleep(0.01)
