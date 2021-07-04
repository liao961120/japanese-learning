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
    for i, line in enumerate(output.split('\n')):
        if i == 0:
            heads.append(line)
            continue
        if line.strip() == '':
            append_next = True
            continue
        if append_next:
            heads.append(line.strip())
            append_next = False

    matched = []
    for head in heads:
        word = pat_word.search(head)
        url = pat_url.search(head)

        if word is None or url is None:
            print(f"Failed to match {head}")
            print(head)
        else:
            matched.append([word[0], url[0]])

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