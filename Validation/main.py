'''
import os
import boto3
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
from werkzeug.utils import secure_filename
import config as keys
  

s3 = boto3.client('s3',
                    aws_access_key_id = "AKIAJEUEB2MKHIBV7PDA",
                    aws_secret_access_key = "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"
                    )

BUCKET_NAME='dell-hackathon'

@app.route('/')  
def home():
    return render_template("index.html")

@app.route('/upload',methods=['post'])
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
                msg = "Upload Done ! "

    return render_template("index.html",msg =msg)


if __name__ == "__main__":   
    app.run(debug=True)
'''

import csv
import pandas as pd
from csv import *

with open('country-codes.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    # get column names from a csv file
    column_names = csv_dict_reader.fieldnames
    print(column_names)

    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row)

data = pd.read_csv("country-codes.csv")

for col in data.columns:
    print(col)
