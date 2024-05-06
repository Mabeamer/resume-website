from flask import Flask, render_template, request, redirect, send_file
#from flask_sqlalchemy import SQAlchemy
from ytdl import *
import sys

app = Flask(__name__)

class ytvideo:
    def __init__(self,videoLink,videoFile,videoName):
        self.videoLink = videoLink
        self.videoFile = videoFile
        self.videoName = videoName

# Tells flask-sqlalchemy what database to connect to
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
# Enter a secret key
#app.config["SECRET_KEY"] = "ENTER YOUR SECRET KEY"
# Initialize flask-sqlalchemy extension
#db = SQLAlchemy()
 
# LoginManager is needed for our application 
# to be able to log in and out users
#login_manager = LoginManager()
#login_manager.init_app(app)
@app.route("/")
def hello(name=None):
    return render_template('home.html', name=name, static_folder='static')

@app.route("/photography")
def photography(name=None):
    return render_template('photography.html', name=name, static_folder='static')

@app.route("/webdl", methods=['GET','POST'])
def dl(name=None):
    woowoo = 'America ya! :D'
    print(woowoo)
    if request.method == "POST":
        print('POST')
        userText = request.form['urlLink']
        print(userText)
        #converter(userText)
        userFile = ytvideo(userText,"test","test234")
        converter(userFile)
        #send to /download url to give user download option
        return redirect("/dl", code=301)  
        

    #if link gets sent over
    #change website to have download button clickable and returns file
    return render_template('webdl.html', name=name, static_folder='static')

@app.route('/dl', methods=['GET','POST'])
def fileDl(name=None):
    print("WE ARE GOING TO DOWNLOAD THIS FILE")
    #incomplete
    #TODO - set up a method/class/function(?) that sends the user the file that was saved to the server to the html page
    if request.method == "POST":
        #get name 
        fileName = "test.mp4" 
        return send_file(fileName) 
    return render_template('dl.html', name=name, static_folder='static')

@app.route('/test.mp4', methods=['GET','POST'])
def testDl(name=None):
    return send_file('test.mp4')
