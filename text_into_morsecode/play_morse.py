from pydub import AudioSegment as audiosegment
from pydub.playback import play
from time import sleep


# setup the audio sounds
short = audiosegment.from_file("/home/george/Python_Projects/morsecode/morseshort.mp3", format="mp3")
long = audiosegment.from_file("/home/george/Python_Projects/morsecode/morselong.mp3", format="mp3")



play(short); play(short); play(short); play(short)   # H: ....
play(short)                                   # E: .
play(short); play(long); play(short); play(short)   # L: .-..
play(short); play(long); play(short); play(short)   # L: .-..
play(long); play(long); play(long)               # O: ---
  
play(short); play(long); play(long)              # W: .--
play(long); play(long); play(short)              # O: ---
play(short); play(long); play(short); play(long)   # R: .-.
play(short); play(long); play(short); play(short)   # L: .-..
play(long); play(short); play(short)            # D: -..
