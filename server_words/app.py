#%%
import re
import json
import subprocess
from flask import Flask, request
from flask_cors import CORS
from utils import lookup


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
