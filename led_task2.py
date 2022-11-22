import RPi.GPIO as GPIO
import time

led1_port = 17



GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)


#LED 1
GPIO.setup(led1_port, GPIO.OUT)
GPIO.output(led1_port, GPIO.HIGH)

time.sleep(1)

GPIO.output(led1_port, GPIO.LOW)

