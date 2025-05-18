# Importing modules and classes
import tm1637
import time
import RPi.GPIO as GPIO

# Setting to BCM mode
GPIO.setmode(GPIO.BCM)

# Setting up the button and lightbulb
button = 18
GPIO.setup(button, GPIO.IN)
lightbulb = 19
GPIO.setup(lightbulb, GPIO.OUT)
light_on = False

# Setting up the display
clock, digital_io = 4, 17
tm = tm1637.TM1637(clk=clock, dio=digital_io)
clear = [0, 0, 0, 0]  # Defining values used to clear the diplay

while True:
    try:
        if not GPIO.input(button) and not light_on:
            time.sleep(.25)
            GPIO.output(lightbulb, GPIO.HIGH)
            light_on = True
            mins = 0
            secs = 0
            tm.numbers(mins,secs)

        elif not GPIO.input(button) and light_on:
            time.sleep(.25)
            GPIO.output(lightbulb, GPIO.LOW)
            tm.write(clear)
            light_on = False

        elif GPIO.input(button) and light_on:
            time.sleep(1)
            if mins == 59 and secs == 59:
                mins = 0
                secs = 0
            elif secs == 59:
                mins += 1
                secs = 0
            else:
                secs += 1
            tm.numbers(mins,secs)

    except KeyboardInterrupt:
        break

tm.write(clear)
GPIO.output(lightbulb,GPIO.LOW)
GPIO.cleanup() 
