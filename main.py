from flask import Flask, jsonify, render_template, request

app = Flask(__name__, static_url_path='/static')


@app.route('/')
@app.route('/letterfly')
def letterfly():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)