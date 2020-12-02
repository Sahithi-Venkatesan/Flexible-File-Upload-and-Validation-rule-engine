from flask import Flask, render_template, request
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