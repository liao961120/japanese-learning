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
    words = [ w.strip() for w in words.split() if not w.strip().startswith('#') ]
# with open("words.json", encoding="utf-8") as f:
#     output = json.load(f)
#     saved_words = { w[0] for w in output }

output = []
for word in words:
    # Search word in online dict
    query = lookup(word)
    if query is None: 
        logging.warning(f"{word} not available")
        continue
    # Download audio
    for word in query:
        audio_path = download_audio(word[1])
        output.append([word[0], audio_path])


with open("words.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=True)
