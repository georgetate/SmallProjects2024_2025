import RPi.GPIO as GPIO
import time

led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)

print("LED on")
GPIO.output(led,GPIO.HIGH)

time.sleep(3)

print("LED off")
GPIO.output(led,GPIO.LOW)

GPIO.cleanup()
