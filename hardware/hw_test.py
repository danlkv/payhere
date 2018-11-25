import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin = 26
GPIO.setup(pin,GPIO.OUT)
while True:
    print("true")
    GPIO.output(pin,True)
    time.sleep(1)
    print("false")
    GPIO.output(pin,False)
    time.sleep(2)
