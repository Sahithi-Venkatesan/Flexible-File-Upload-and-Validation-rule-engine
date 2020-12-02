from flask import Flask, render_template, request
import csv
import json
import pandas as pd
from io import StringIO
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, CanConvertValidation, MatchesPatternValidation, InRangeValidation, InListValidation

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])

def login():
    message = ''
    if request.method == 'POST':
        l1 = request.form.get('l1')  # access the data inside 
        l2 = request.form.get('l2')
        l3 = request.form.get('l3')
        
        '''
        x = {
            "col_name": l1,
            "dtype": l2,
            "length": l3
            }

        print(x)
        '''
        
        schema = Schema([
        Column('l1', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()])
        col_name=["l1"]
        test_data = pd.read_csv("data.csv",header=None,error_bad_lines=False)

        errors = schema.validate(test_data)

        for error in errors:
            print(error)
    return render_template('inputfield.html', message=message)
'''
def fields():
    if request.method=='POST'
        d1=request.form1.get('d1')
        print(d1)
    return render_template('inputfield.html')
'''

'''
        if (l1 == 'sahithi' and l2 == 'int' and l3 == '7'):
            message = l2
        else:
            message = l2
'''
    

if __name__ == "__main__":   
    app.run(debug=True)