from flask import Flask,render_template,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/recover')
def recover():
    return render_template('recover.html')

if __name__ == '__main__':
    app.run(debug=True)