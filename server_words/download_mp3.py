#%%
import json

with open("words.json", encoding="utf-8") as f:
    words = json.load(f)


# %%
import os

for i, word in enumerate(words):
    url = word[1]
    fname = os.path.basename(url)
    if not fname.endswith('.mp3'):
        fname += '.mp3'
    fp = f"audio/{fname}"
    words[i][1] = f"server_words/{fp}"
    os.system(f"wget -O {fp} {url}")
# %%
with open("words_local.json", "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=True)
# %%
