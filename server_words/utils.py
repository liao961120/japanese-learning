import re
import os
import subprocess

DICT = './bin/hj_linux_amd64'
pat_word = re.compile(r'^\S+ (\[[^][ ]+\]){1,2}')
pat_url = re.compile(r'http\S+$')

def lookup(term):
    result = subprocess.Popen(f"./bin/hj_linux_amd64 -jp {term}", shell=True, stdout=subprocess.PIPE)
    output = result.stdout.read().decode('utf-8')
    if output =='': return None

    heads = []
    append_next = False
    entry = {'head': '', 'def': ''}
    for i, line in enumerate(output.split('\n')):
        if i == 0:
            entry["head"] = line.strip()
            continue
        if line.strip() == '':
            if entry["head"] != '':
                heads.append(entry.copy())
            append_next = True
            entry = {'head': '', 'def': ''}
            continue
        if append_next:
            entry["head"] = line.strip()
            append_next = False
            continue
        entry["def"] += line + '\n'

    matched = []
    for head in heads:
        word = pat_word.search(head["head"])
        url = pat_url.search(head["head"])

        if word is None or url is None:
            print(f"Failed to match {head['head']}")
        else:
            matched.append([word[0], url[0], head["def"]])

    if len(matched) == 0:
        print(f"Failed to match {output}")
        print(output)
        return None

    return matched


def download_audio(url):
    fname = os.path.basename(url)
    if not fname.endswith('.mp3'): fname += '.mp3'
    fp = f"audio/{fname}"
    os.system(f"wget -O {fp} {url}")
    return f"server_words/{fp}"