import json
import os
from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

app = Flask(__name__)

@app.route('/webhook', methods = ['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Requested")
    print(json.dumps(req,indent=4))

    #res = processRequest(req)
    return jsonify(req)

