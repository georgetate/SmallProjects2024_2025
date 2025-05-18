from time import time

prompt = "Set your minds on things that are above, not on things that are on earth. Colossians 3:2"

# timer
start = time()
print(prompt)
response = input()
stop = time()

timespan = (stop - start) / 60
wordcount = len(prompt.split(" "))
WordsPerMinute = round(wordcount/timespan)

if response == prompt:
    print(f"WPM: {WordsPerMinute}\nMistakes: 0")
else:
    mistakes = 0
    for i in range(len(prompt)):
        if response[i] != prompt[i]:
            mistakes += 1
    print(f"WPM: {WordsPerMinute}\nMistakes: {mistakes}")




