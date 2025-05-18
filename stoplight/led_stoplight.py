import RPi.GPIO as GPIO
from time import sleep

green = 12
yellow = 16
red = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(yellow,GPIO.OUT)
GPIO.setup(red,GPIO.OUT)

while True:
    GPIO.output(green,GPIO.HIGH)
    sleep(5)
    GPIO.output(green,GPIO.LOW)

    GPIO.output(yellow,GPIO.HIGH)
    sleep(1)
    GPIO.output(yellow,GPIO.LOW)

    GPIO.output(red,GPIO.HIGH)
    sleep(4)
    GPIO.output(red,GPIO.LOW)

GPIO.cleanup()
