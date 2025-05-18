import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

for i in range(1, 28):
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

GPIO.cleanup()
