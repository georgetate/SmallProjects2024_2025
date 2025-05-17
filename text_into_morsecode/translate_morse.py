from pydub import AudioSegment as audiosegment
from pydub.playback import play
from time import sleep


# setup the audio sounds
short = audiosegment.from_file("/home/george/Python_Projects/morsecode/morseshort.mp3", format="mp3")
long = audiosegment.from_file("/home/george/Python_Projects/morsecode/morselong.mp3", format="mp3")

def translate(message: str):
    morse_code_dict = {
    "a": "short long",
    "b": "long short short short",
    "c": "long short long short",
    "d": "long short short",
    "e": "short",
    "f": "short short long short",
    "g": "long long short",
    "h": "short short short short",
    "i": "short short",
    "j": "short long long long",
    "k": "long short long",
    "l": "short long short short",
    "m": "long long",
    "n": "long short",
    "o": "long long long",
    "p": "short long long short",
    "q": "long long short long",
    "r": "short long short",
    "s": "short short short",
    "t": "long",
    "u": "short short long",
    "v": "short short short long",
    "w": "short long long",
    "x": "long short short long",
    "y": "long short long long",
    "z": "long long short short",
    "0": "long long long long long",
    "1": "short long long long long",
    "2": "short short long long long",
    "3": "short short short long long",
    "4": "short short short short long",
    "5": "short short short short short",
    "6": "long short short short short",
    "7": "long long short short short",
    "8": "long long long short short",
    "9": "long long long long short"
    }
    
    morse = ""
    message = message.lower()
    for char in message:
        if char in morse_code_dict.keys():
            morse += morse_code_dict[char]
            morse += " pause "
            
    
    return morse

def play_morse(beeps: str):
    beeps = beeps.split(" ")
    for beep in beeps:
        if beep == "short":
            play(short)
        elif beep == "long":
            play(long)
        elif beep == "pause":
            sleep(.25)

def main():
    message = input("What would you like to say: ")
    beeps = translate(message)
    play_morse(beeps)

if __name__ == "__main__":
    main()
