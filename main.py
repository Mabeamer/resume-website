from flask import Flask, render_template, request
from ytdl import *
import sys

app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return render_template('home.html', name=name, static_folder='static')

@app.route("/webdl", methods=['GET','POST'])
def dl(name=None):
    woowoo = 'America ya! :D'
    print(woowoo)
    if request.method == "POST":
        print('POST')
        userText = request.form['urlLink']
        print(userText)
        converter(userText)
        #send to /download url to give user download option
        
        

    #if link gets sent over
    #change website to have download button clickable and returns file
    return render_template('webdl.html', name=name, static_folder='static')
