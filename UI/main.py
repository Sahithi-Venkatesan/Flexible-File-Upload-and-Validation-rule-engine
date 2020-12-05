'''
from flask import Flask, render_template, request, flash
import json
app = Flask(__name__)
@app.route('/')  
def home():
    return render_template("index.html")
@app.route('/login_1', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('login_1.html')
    
if __name__ == "__main__":   
    app.run(debug=True)
'''
from flask import Flask, render_template, request, flash, redirect, url_for
import json
import pandas as pd
from io import StringIO
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, CanConvertValidation, MatchesPatternValidation, InRangeValidation, InListValidation, DateFormatValidation
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')  
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('upload.html')



Ext_check = set(['csv', 'txt'])

def file_check(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in Ext_check
	
'''
@app.route('/design', methods=['POST'])
def upload_file():
	if request.method == 'POST':
       
		file = request.files['file']
		if file.filename == '':
			flash('Please select a file')
			return render_template('design.html')
		if file and file_check(file.filename):
			filename = secure_filename(file.filename)
			#file.save(file.filename)  # stores file in main folder
            file.save(os.path.join('templates', filename))
			flash('File successfully uploaded')
			return render_template('design.html')
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return render_template('design.html')
@app.route('/design', methods=['post', 'get'])
def retrieve():
    if request.method == 'POST':
        s = request.form.get('s')
        print(s)
        return redirect(url_for('login'))
    return render_template('design.html')
'''
@app.route('/design', methods=['post', 'get'])
def design():
    if request.method == 'POST':
        if request.form.get('datatype') == 'String':
            a=request.form.get('datatype')
            print(a)
            return render_template("design.html")
        if request.form.get('colnum') == '1':
            a=request.form.get('colnum')
            print(a)
            return render_template("design.html")
        if request.form.get('template') == 'Age':
            a=request.form.get('template')
            print(a)
            return render_template("design.html")
        if request.form.get('columns') == '1':
            a=request.form.get('columns')
            values=2
            print(a)
            return render_template("design.html",value=a,values=values)
        if request.form.get('columns') == '2':
            a=request.form.get('columns')
            values=2
            print(a)
            return render_template("design.html",value=a,values=values)
        if request.form.get('columns') == '3':
            a=request.form.get('columns')
            values=3
            print(a)
            return render_template("design.html",value=a,values=values)
        if request.form.get('columns') == '4':
            a=request.form.get('columns')
            values=4
            print(a)
            return render_template("design.html",value=a,values=values)
        if request.form.get('columns') == '5':
            a=request.form.get('columns')
            values=5
            print(a)
            return render_template("design.html",value=a,values=values)
        return redirect(url_for('design'))
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("design.html") 

if __name__ == "__main__":   
    app.run(debug=True)
