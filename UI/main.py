'''
from flask import Flask, render_template, request, flash
import json
app = Flask(_name_)
@app.route('/')  
def home():
    return render_template("index.html")
@app.route('/login_1', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('login_1.html')
    
if _name_ == "_main_":   
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
import os
import boto3
import config as keys
 
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
        return redirect(url_for('upload'))
    return render_template('upload.html')

s3 = boto3.client('s3',
                    aws_access_key_id = "AKIAJEUEB2MKHIBV7PDA",
                    aws_secret_access_key = "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"
                    )

BUCKET_NAME='dell-hackathon'

@app.route('/upload_aws',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
    return render_template("upload.html")

@app.route('/design', methods=['post', 'get'])
def design():
    if request.method == 'POST':
        values=0
        if request.form.get('columns') == '1':
            a=request.form.get('columns')
            values=1
            print(a)
            return render_template("design.html",value=a,values=values)
        count=1
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
        #value = None
        cnum0 = request.form.get('cnum0')
        cnum1 = request.form.get('cnum1')
        cnum2 = request.form.get('cnum2')
        cnum3 = request.form.get('cnum3')
        cnum4 = request.form.get('cnum4')
        d0 = request.form.get('d0')
        d1 = request.form.get('d1')
        d2 = request.form.get('d2')
        d3 = request.form.get('d3')
        d4 = request.form.get('d4')
      
        c0=""
        c1=""
        c2=""
        c3=""
        c4=""
        if int(cnum1 or 123) is None:
            cnum1=""
        if int(cnum2 or 23) is None:
            cnum2=""
        if int(cnum3 or 23) is None:
            cnum3=""
        if int(cnum4 or 23) is None:
            cnum4=""

        if cnum4=='4':
            test_data = pd.read_csv(StringIO('''Age,Name,Phn,Date,Time
            32,    Sahithi,123,1/13/2000,25:00
            300,Shreya,6124352617,22/2/2000,3
            24,Bhavana,88,3,f'''))
            if d0=='Age':
                c0=InRangeValidation(0, 90)
            if d0=='Name':
                c0=LeadingWhitespaceValidation()
            if d0=='Gender':
                c0=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d0=='Phn':
                c0=MatchesPatternValidation(r'\d{10}')
            if d0=='E-mail':
                c0=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d0=='Date':
                c0=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d0=='Time':
                c0=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            if d1=='Age':
                c1=InRangeValidation(0, 90)
            if d1=='Name':
                c1=LeadingWhitespaceValidation()
            if d1=='Gender':
                c1=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d1=='Phn':
                c1=MatchesPatternValidation(r'\d{10}')
            if d1=='E-mail':
                c1=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d1=='Date':
                c1=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d1=='Time':
                c1=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            if d2=='Age':
                c2=InRangeValidation(0, 90)
            if d2=='Name':
                c2=LeadingWhitespaceValidation()
            if d2=='Gender':
                c2=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d2=='Phn':
                c2=MatchesPatternValidation(r'\d{10}')
            if d2=='E-mail':
                c2=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d2=='Date':
                c2=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d2=='Time':
                c2=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            if d3=='Age':
                c3=InRangeValidation(0, 90)
            if d3=='Name':
                c3=LeadingWhitespaceValidation()
            if d3=='Gender':
                c3=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d3=='Phn':
                c3=MatchesPatternValidation(r'\d{10}')
            if d3=='E-mail':
                c3=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d3=='Date':
                c3=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d3=='Time':
                c3=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            if d4=='Age':
                c4=InRangeValidation(0, 90)
            if d4=='Name':
                c4=LeadingWhitespaceValidation()
            if d4=='Gender':
                c4=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d4=='Phn':
                c4=MatchesPatternValidation(r'\d{10}')
            if d4=='E-mail':
                c4=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d4=='Date':
                c4=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d4=='Time':
                c4=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            list=[]
            for col in test_data.columns:
                list.append(col)
            schema = Schema([Column(list[int(cnum0)], [c0]),Column(list[int(cnum1)], [c1]),Column(list[int(cnum2)], [c2]), Column(list[int(cnum3)], [c3]), Column(list[int(cnum4)], [c4]) ])
            errors = schema.validate(test_data)
            for error in errors:
                print(error)
            pd.DataFrame({'col':errors}).to_csv('static/errors.csv')
            return redirect(url_for('design'))


        if cnum3=='3':
            test_data = pd.read_csv(StringIO('''Age,Name,Phn
            32,    Sahithi,123
            300,Shreya,6124352617
            24,Bhavana,88'''))
            if d0=='Age':
                c0=InRangeValidation(0, 90)
            if d0=='Name':
                c0=LeadingWhitespaceValidation()
            if d0=='Gender':
                c0=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d0=='Phn':
                c0=MatchesPatternValidation(r'\d{10}')
            if d0=='E-mail':
                c0=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d0=='Date':
                c0=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d0=='Time':
                c0=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            if d1=='Age':
                c1=InRangeValidation(0, 90)
            if d1=='Name':
                c1=LeadingWhitespaceValidation()
            if d1=='Gender':
                c1=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d1=='Phn':
                c1=MatchesPatternValidation(r'\d{10}')
            if d1=='E-mail':
                c1=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d1=='Date':
                c1=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d1=='Time':
                c1=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            if d2=='Age':
                c2=InRangeValidation(0, 90)
            if d2=='Name':
                c2=LeadingWhitespaceValidation()
            if d2=='Gender':
                c2=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d2=='Phn':
                c2=MatchesPatternValidation(r'\d{10}')
            if d2=='E-mail':
                c2=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d2=='Date':
                c2=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d2=='Time':
                c2=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            if d3=='Age':
                c3=InRangeValidation(0, 90)
            if d3=='Name':
                c3=LeadingWhitespaceValidation()
            if d3=='Gender':
                c3=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d3=='Phn':
                c3=MatchesPatternValidation(r'\d{10}')
            if d3=='E-mail':
                c3=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d3=='Date':
                c3=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d3=='Time':
                c3=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            list=[]
            for col in test_data.columns:
                list.append(col)
            schema = Schema([Column(list[int(cnum0)], [c0]),Column(list[int(cnum1)], [c1]),Column(list[int(cnum2)], [c2]), Column(list[int(cnum3)], [c3]) ])
            errors = schema.validate(test_data)
            for error in errors:
                print(error)
            pd.DataFrame({'col':errors}).to_csv('static/errors.csv')
            return redirect(url_for('design'))

       
        if cnum2=='2':
            test_data = pd.read_csv(StringIO('''Age,Name,Phn
            32,    Sahithi,123
            300,Shreya,6124352617
            24,Bhavana,88'''))
            if d0=='Age':
                c0=InRangeValidation(0, 90)
            if d0=='Name':
                c0=LeadingWhitespaceValidation()
            if d0=='Gender':
                c0=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d0=='Phn':
                c0=MatchesPatternValidation(r'\d{10}')
            if d0=='E-mail':
                c0=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d0=='Date':
                c0=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d0=='Time':
                c0=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            if d1=='Age':
                c1=InRangeValidation(0, 90)
            if d1=='Name':
                c1=LeadingWhitespaceValidation()
            if d1=='Gender':
                c1=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d1=='Phn':
                c1=MatchesPatternValidation(r'\d{10}')
            if d1=='E-mail':
                c1=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d1=='Date':
                c1=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d1=='Time':
                c1=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            if d2=='Age':
                c2=InRangeValidation(0, 90)
            if d2=='Name':
                c2=LeadingWhitespaceValidation()
            if d2=='Gender':
                c2=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d2=='Phn':
                c2=MatchesPatternValidation(r'\d{10}')
            if d2=='E-mail':
                c4=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d2=='Date':
                c2=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d2=='Time':
                c2=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            list=[]
            for col in test_data.columns:
                list.append(col)
            schema = Schema([Column(list[int(cnum0)], [c0]),Column(list[int(cnum1)], [c1]),Column(list[int(cnum2)], [c2]) ])
            errors = schema.validate(test_data)
            for error in errors:
                print(error)
            pd.DataFrame({'col':errors}).to_csv('static/errors.csv')
            return redirect(url_for('design'))
        elif cnum1=='1':
            test_data = pd.read_csv(StringIO('''Age,Name
            32,    Sahithi
            300,Shreya
            24,Bhavana'''))
            if d0=='Age':
                c0=InRangeValidation(0, 30)
            if d0=='Name':
                c0=LeadingWhitespaceValidation()
            if d0=='Gender':
                c0=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d0=='Phn':
                c0=MatchesPatternValidation(r'\d{10}')
            if d0=='E-mail':
                c0=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d0=='Date':
                c0=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d0=='Time':
                c0=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            if d1=='Age':
                c1=InRangeValidation(0, 30)
            if d1=='Name':
                c1=LeadingWhitespaceValidation()
            if d1=='Gender':
                c1=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d1=='Phn':
                c1=MatchesPatternValidation(r'\d{10}')
            if d1=='E-mail':
                c1=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d1=='Date':
                c1=MatchesPatternValidation(r'(^([1-31]|[0-1][1-9])+(/|-)([0][1-9]|[1-12])+(/|-)[\d]{4})')
            if d1=='Time':
                c1=MatchesPatternValidation(r'(^([2][0-4]|[0-1][0-9])+:[0-5][0-9])')
            list=[]
            for col in test_data.columns:
                list.append(col)
            schema = Schema([Column(list[int(cnum0)], [c0]),Column(list[int(cnum1)], [c1]) ])
            errors = schema.validate(test_data)
            for error in errors:
                print(error)
            pd.DataFrame({'col':errors}).to_csv('static/errors.csv')
            return redirect(url_for('design'))
        else:
            test_data = pd.read_csv(StringIO('''Time
            24/12/1200
            03:00
            24:60'''))
            if d0=='Age':
                c0=InRangeValidation(0, 30)
            if d0=='Name':
                c0=LeadingWhitespaceValidation()
            if d0=='Gender':
                c0=InListValidation(['Male', 'Female', 'Other', 'm','M','f','F','male','female','other'])
            if d0=='Phn':
                c0=MatchesPatternValidation(r'\d{10}')
            if d0=='E-mail':
                c0=MatchesPatternValidation(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            if d0=='Date':
                c0=MatchesPatternValidation(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}")
            if d0=='Time':
                c0=MatchesPatternValidation(r"[\d]{1,2}:[\d]{2}")
            list=[]
            for col in test_data.columns:
                list.append(col)
            schema = Schema([Column(list[int(cnum0)], [c0])])
            errors = schema.validate(test_data)
            for error in errors:
                print(error)
            pd.DataFrame({'col':errors}).to_csv('static/errors.csv')
            return redirect(url_for('design'))
        return redirect(url_for('design'))
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("design.html")

if __name__ == "__main__":   
    app.run(debug=True)