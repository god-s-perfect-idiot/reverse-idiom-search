from flask import Flask, render_template, request, render_template_string, send_from_directory, abort, safe_join, send_file
from nocache import nocache
import model
import service
import os
import json

prev=''
app = Flask(__name__)

@app.route("/")
@nocache
def home():
    return render_template('index.html')

@app.route("/fetch", methods=["POST"])
def fetch():
    if(request.method == 'POST'):
        term = request.form.get('searchterm')

        return json.jsonify("worked")

if(__name__=="__main__"):
    app.run(debug=True)
