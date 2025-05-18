# Importing modules and classes
import tm1637
import time

# Creating 4-digit 7-segment display object
tm = tm1637.TM1637(clk=4, dio=17)  # Using GPIO pins 18 and 17
clear = [0, 0, 0, 0]  # Defining values used to clear the display

# Displaying a rolling string
tm.write(clear)
time.sleep(1)
s = "Hello" + " " + input("What is your name: ")
tm.scroll(s, delay=250)
time.sleep(2)
