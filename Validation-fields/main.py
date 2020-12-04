from flask import Flask, render_template, request, flash
import json
import pandas as pd
from io import StringIO
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, CanConvertValidation, MatchesPatternValidation, InRangeValidation, InListValidation, DateFormatValidation
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

#code to retrieve uploaded file
'''
app.secret_key = "secret key"

Ext_check = set(['csv', 'txt'])

def file_check(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in Ext_check
	

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
       
		file = request.files['file']
		if file.filename == '':
			flash('Please select a file')
			return render_template('inputfield.html')
		if file and file_check(file.filename):
			filename = secure_filename(file.filename)
			file.save(file.filename)  # stores file in main folder
            #file.save(os.path.join('Validation-fields', filename))  -->to store file in Validation-fields
			flash('File successfully uploaded')
			return render_template('inputfield.html')
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return render_template('inputfield.html')
'''            

@app.route('/', methods=['post', 'get'])

def login():
    message = ''
    if request.method == 'POST':
        n0 = request.form.get('n0')  # access the data inside 
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        d0 = request.form.get('d0')  # access the data inside 
        d1 = request.form.get('d1')
        d2 = request.form.get('d2')
        l0 = request.form.get('l0')  # access the data inside 
        l1 = request.form.get('l1')
        l2 = request.form.get('l2')

        lwsv=LeadingWhitespaceValidation()
        twsv=TrailingWhitespaceValidation()
        irv=InRangeValidation(0, 120)
        ilv=InListValidation(['Male', 'Female', 'Other'])
        mpv=MatchesPatternValidation(r'\d[A-Z]')
        dfv=DateFormatValidation( r'\d(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})')
        #IsDtypeValidation()
        c0=""
        c1=""
        c2=""
        if n0=='Name' or n0=='First name' or n0=='Last name' or n0=='name':          
            c0=[lwsv, twsv]
        if n0=='Age':
            c0=irv
        if n0=='Sex':
            c0=ilv
        if n0=='ID':
            c0=mpv
        if n1=='Name' or n1=='First name' or n1=='Last name' or n1=='name':          
            c1=[lwsv, twsv]
        if n1=='Age':
            c1=irv
        if n1=='Sex':
            c1=ilv
        if n1=='ID':
            c1=mpv
        if n2=='Name'or n2=='First name' or n2=='Last name' or n2=='name':          
            c2=[lwsv, twsv]
        if n2=='Age':
            c2=irv
        if n2=='Sex':
            c2=ilv
        if n2=='ID':
            c2=mpv
        if n2=='DOB':
            c2=dfv
                
        schema = Schema([
        Column(n0, c0),
        Column(n1, [c1]),
        Column(n2, [c2])
        ])

        #test_data = pd.read_csv('data.csv',header=None,error_bad_lines=False)
        #test_data = pd.read_csv(StringIO(Name))
        test_data = pd.read_csv('data.csv')
        #test_data = pd.read_csv(file.filename)--> rename to consider the file that is being uploaded

        errors = schema.validate(test_data)

        for error in errors:
            print(error)

    return render_template('design.html', message=message)

    
if __name__ == "__main__":   
    app.run(debug=True)