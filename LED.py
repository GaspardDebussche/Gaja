import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#for i in range(1,20):
GPIO.setup(18, GPIO.OUT)
print("LEDon")
#for i in range(1,20):
GPIO.output(18,GPIO.HIGH)
time.sleep(5)
print("LED off")
GPIO.output(18, GPIO.LOW)

