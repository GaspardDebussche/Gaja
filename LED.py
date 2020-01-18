import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)



def led_management(state):
    print("Eye state: {}".format(state))
    if state==0:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
    if state==-1:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
    if state==2:
        GPIO.output(23, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)

