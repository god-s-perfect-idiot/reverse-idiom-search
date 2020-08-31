from flask import Flask, render_template, request, render_template_string, send_from_directory, abort, safe_join, send_file 
from nocache import nocache
import model
import service
import os

prev=''
app = Flask(__name__)

@app.route("/")
@nocache
def home():
    return render_template('index.html')



if(__name__=="__main__"):
    app.run(debug=True)
