import RPi.GPIO as GPIO
import time

led1_port = 17
led2_port = 10
led3_port = 11

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)


#LED 1
GPIO.setup(led1_port, GPIO.OUT)
GPIO.output(led1_port, GPIO.HIGH)

time.sleep(2)

GPIO.output(led1_port, GPIO.LOW)


#LED 2
GPIO.setup(led2_port, GPIO.OUT)
GPIO.output(led2_port, GPIO.HIGH)

time.sleep(2)

GPIO.output(led2_port, GPIO.LOW)


#LED 3
GPIO.setup(led3_port, GPIO.OUT)
GPIO.output(led3_port, GPIO.HIGH)

time.sleep(2)

GPIO.output(led3_port, GPIO.LOW)