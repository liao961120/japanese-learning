#%%
import os
import time
import random
import pathlib

FROM = 6
TO = 10
REPEAT = 3

jap = 'あ ア	い イ	う ウ	え エ	お オ	か カ	き キ	く ク	け ケ	こ コ	さ サ	し シ	す ス	せ セ	そ ソ	た タ	ち チ	つ ツ	て テ	と ト	な ナ	に ニ	ぬ ヌ	ね ネ	の ノ	は ハ	ひ ヒ	ふ フ	へ ヘ	ほ ホ	ま マ	み ミ	む ム	め メ	も モ	や ヤ	ゆ ユ	よ ヨ	ら ラ	り リ	る ル	れ レ	ろ ロ	わ ワ	を ヲ	ん ン'.split('\t')[FROM-1:TO]

roman = 'a	i	u	e	o	ka	ki	ku	ke	ko	sa	shi	su	se	so	ta	chi	tsu	te	to	na	ni	nu	ne	no	ha	hi	fu	he	ho	ma	mi	mu	me	mo	ya	yu	yo	ra	ri	ru	re	ro	wa	wo	n'.split('\t')[FROM-1:TO]

hiragana = [ x.split(' ')[0] for x in jap ]
katagana = [ x.split(' ')[1] for x in jap ]


# Listen and write down hiragana 
audio = pathlib.Path('audio/50yin/')
idx = []
for i in range(REPEAT):
	idx += list(range(len(roman)))
random.shuffle(idx)

for i in idx:
	mp3 = audio / f"{roman[i]}.mp3"
	for j in range(3):
		time.sleep(1)
		os.system(f"cvlc --play-and-exit {mp3} >/dev/null 2>&1")

	print("Write down your answer...")
	time.sleep(3.5)
	print(f'ANSWER:  {hiragana[i]}')
	print()


# %%
