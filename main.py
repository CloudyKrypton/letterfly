from flask import Flask, jsonify, render_template, request

app = Flask(__name__, static_url_path='/static')


@app.route('/')
@app.route('/letterfly')
def letterfly():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/read')
def read():
    return render_template('read.html')

@app.route('/discover')
def discover():
    return render_template('discover.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)