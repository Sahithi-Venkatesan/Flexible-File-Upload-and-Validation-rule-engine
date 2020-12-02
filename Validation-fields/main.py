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
        l1 = request.form.get('l1')  # access the data inside 
        l2 = request.form.get('l2')
        l3 = request.form.get('l3')

        x = {
            "col_name": l1,
            "dtype": l2,
            "length": l3
            }

        print(x)

        schema = Schema([
        Column('l1', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()])
        ])

        test_data = pd.read_csv('data.csv')
        #test_data = pd.read_csv(file.filename)--> rename to consider the file that is being uploaded

        errors = schema.validate(test_data)

        for error in errors:
            print(error)
    return render_template('inputfield.html', message=message)

'''
        if (l1 == 'sahithi' and l2 == 'int' and l3 == '7'):
            message = l2
        else:
            message = l2
'''
    

if __name__ == "__main__":   
    app.run(debug=True)
