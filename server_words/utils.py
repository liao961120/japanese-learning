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

    output = output.split('\n')[0]
    word = pat_word.search(output)
    url = pat_url.search(output)

    if word is None or url is None:
        print(f"Failed to match {term}")
        print(output)
        return None

    return word[0], url[0]


def download_audio(url):
    fname = os.path.basename(url)
    if not fname.endswith('.mp3'): fname += '.mp3'
    fp = f"audio/{fname}"
    os.system(f"wget -O {fp} {url}")
    return f"server_words/{fp}"