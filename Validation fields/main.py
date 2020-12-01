from flask import Flask, render_template, request
import json
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
    return render_template('inputfield.html', message=message)

'''
        if (l1 == 'sahithi' and l2 == 'int' and l3 == '7'):
            message = l2
        else:
            message = l2
'''
    

if __name__ == "__main__":   
    app.run(debug=True)