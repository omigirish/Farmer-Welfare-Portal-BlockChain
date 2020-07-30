from flask import Flask , render_template,jsonify,request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mapbasic')
def index2():
    return render_template('graph.html')

@app.route('/json')
def json():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/farmer')
def farmer():
    return render_template('farmer.html')

@app.route('/Addp')
def Addp():
    return render_template('Addp.html')

@app.route('/accept')
def accept():
    return render_template('accept1.html')

@app.route('/Farmdetails')
def Farmddetails():
    return render_template('Farmdetails.html')

@app.route('/quality')
def quality():
    return render_template('qual.html')

@app.route('/track')
def track():
    return render_template('track.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='5005')

