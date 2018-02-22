
from flask import render_template
from app import app

from systeminfo import main
@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] =  main.main()   # Feel free to put your name here
    returnDict['title'] = 'Home'
    return render_template("index.html", **returnDict)

