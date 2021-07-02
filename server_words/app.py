#%%
import re
import json
import subprocess
from flask import Flask, request
from flask_cors import CORS

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


# Server application
app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def queryTerms():
    terms = request.args.get('terms')
    terms = json.loads(terms)

    output = []
    for term in terms:
        query = lookup(term)
        if query is None: continue
        output.append(query)
    
    return json.dumps(output, ensure_ascii=False)
