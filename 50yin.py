import os
import time
import random
import pathlib
import json

REPEAT = 3
SUBSET = ['k']

with open("gojuon.json", encoding="utf-8") as f:
	data = json.load(f)

data_sub = []
for char in data:
	for s in SUBSET:
		if char['roman'].startswith(s):
			data_sub.append(char)
			break

data_sub = data_sub * REPEAT
random.shuffle(data_sub)

# Listen and write down hiragana 
audio = pathlib.Path('data/audio/')
for i, char in enumerate(data_sub):
	mp3 = char["audio"]
	for j in range(3):
		#time.sleep(1)
		os.system(f"cvlc --play-and-exit {mp3} >/dev/null 2>&1")

	print(f"{i+1:02}. Write down your answer...")
	time.sleep(.5)
	print(f'    ANSWER: {char["hiragana"]: <5}{char["katakana"]: <5}{char["roman"]}')
	print()
