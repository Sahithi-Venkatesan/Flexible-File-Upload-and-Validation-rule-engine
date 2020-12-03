from flask import Flask, render_template, request, flash
import json
import pandas as pd
from io import StringIO
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, CanConvertValidation, MatchesPatternValidation, InRangeValidation, InListValidation
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

        schema = Schema([
        Column('n1', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()])
        ])

        test_data = pd.read_csv('data.csv',header=None,error_bad_lines=False)
        #test_data = pd.read_csv(file.filename)--> rename to consider the file that is being uploaded

        errors = schema.validate(test_data)

        for error in errors:
            print(error)

    return render_template('inputfield.html', message=message)

    

if __name__ == "__main__":   
    app.run(debug=True)
