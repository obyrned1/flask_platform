# dummyapp/app/views.py
from flask import render_template
from app import app

from systeminfo import systeminfo


@app.route('/')
def index():
	returnDict = {}
	returnDict['sysinfo'] = systeminfo.main()
	returnDict['title'] = 'Home'
	return render_template("index.html", **returnDict)
