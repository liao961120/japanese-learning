#%%
import json
import logging
from utils import lookup, download_audio

logging.basicConfig(filename="extract_terms.log",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
logging.info("Start searching terms")

with open("wordlist.txt", encoding="utf-8") as f:
    words = f.read().strip()
    words = words.split()
with open("words.json", encoding="utf-8") as f:
    output = json.load(f)
    saved_words = { w[0] for w in output }
    
for word in words:
    downloaded = sum(1 for w in saved_words if word in w)
    if downloaded > 0: continue
    # Search word in online dict
    query = lookup(word)
    if query is None: 
        logging.warning(f"{word} not available")
        continue
    # Download audio
    audio_path = download_audio(query[1])
    output.append([query[0], audio_path])


with open("words.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=True)
