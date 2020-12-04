from flask import Flask, render_template, request
    
    
app = Flask(__name__)
    
  
@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('month') == 'January':
            a=request.form.get('month')
            print(a)
            return render_template("index2.html")
        if request.form.get('month') == 'February':
            a=request.form.get('month')
            print(a)
            return render_template("index2.html")
            '''
          if request.form.get('January') == 'January':
            # pass
            print("Encrypted")
            elif  request.form.get('February') == 'February':
            # pass # do something else
            print("Decrypted")
            else:
            # pass # unknown
            return render_template("index2.html")
            '''
        elif request.method == 'GET':
        # return render_template("index.html")
            print("No Post Back Call")
        
    return render_template("index2.html")   
    
    
    

if __name__ == '__main__':
    app.run( debug=True)