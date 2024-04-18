from flask import Flask, render_template, request, redirect, send_from_directory
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
        return redirect("/dl", code=301)  
        

    #if link gets sent over
    #change website to have download button clickable and returns file
    return render_template('webdl.html', name=name, static_folder='static')

@app.route('/dl', methods=['GET','POST'])
def fileDl(name=None):
    print("WE ARE GOING TO DOWNLOAD THIS FILE")
    #incomplete 
    if request.method == "POST":
        fileName = ''
        return send_from_directory(,fileName) 
    return render_template('dl.html' name=name, static_folder='static')
