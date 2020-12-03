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