from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('home.html', name=name, static_folder='static')

@app.route("/webdl")
def dl(name=None):
    return render_template('webdl.html', name=name, static_folder='static')
