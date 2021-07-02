#%%
import json
from app import lookup

with open("wordlist.txt", encoding="utf-8") as f:
    words = f.read().strip()
    words = words.split()
# %%
output = []
for word in words:
    query = lookup(word)
    if query is None: 
        print(word, "not available")
        continue
    output.append(query)

# %%
with open("words.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=True)
# %%
