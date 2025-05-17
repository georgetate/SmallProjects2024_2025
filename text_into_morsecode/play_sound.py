from pydub import AudioSegment as audiosegment
from pydub.playback import play
from time import sleep
import RPi.GPIO as GPIO

# setup the button
button = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)
# setup the audio sounds
short = audiosegment.from_file("/home/george/Python_Projects/morsecode/morseshort.mp3", format="mp3")
long = audiosegment.from_file("/home/george/Python_Projects/morsecode/morselong.mp3", format="mp3")

# play when pushed
while True:
    try:
        if not GPIO.input(button):
            play(short)
            sleep(.5)
            play(long)
    except KeyboardInterrupt:
        print()
        break

GPIO.cleanup()


