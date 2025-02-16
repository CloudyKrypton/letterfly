from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from letterfly_db import *
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.getenv("SECRET_KEY")

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

@app.route('/')
@app.route('/letterfly')
def letterfly():
    return render_template('index.html')

@app.route('/submit_login', methods=['POST'])
def submit_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Database connection
    conn = connect_db(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    if not conn:
        return jsonify({"error": "Could not connect to the database."}), 500  # Internal Server Error

    user = get_user(conn, username)
    if not user:
        return jsonify({"error": "User not found."}), 404  # Not Found

    if password != user[1]:
        return jsonify({"error": "Incorrect password."}), 401  # Unauthorized

    # Store session data (if using sessions)
    session['username'] = username

    return redirect(url_for("dashboard"))  # Redirect user after login
    
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/submit_signup', methods=['POST'])
def submit_signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    reads_in = data.get('reads_in')
    writes_in = data.get('writes_in')

@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    # if not username:
    #     return redirect(url_for('letterfly'))
    conn = connect_db(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    if not conn:
        return jsonify({"error": "Could not connect to the database."}), 500
    user = get_user(conn, username)
    session['name'] = user[2]
    session['reads_in'] = user[3]
    session['writes_in'] = user[4]
    session['unread_letters'] = get_letters(conn, username, 'unread')
    session['bottled_letters'] = get_letters(conn, username, 'bottled')
    session['read_letters'] = get_letters(conn, username, 'read')
    return render_template('dashboard.html')

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/send_letter', methods=['POST'])
def send_letter():
    data = request.get_json()
    writer = session['username']
    content = data.get('content')
    # language = data.get('language')
    language = 'English'
    recipient = data.get('recipient')

    conn = connect_db(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    if not conn:
        return jsonify({"error": "Could not connect to the database."}), 500

    letter_id = insert_letter(conn, content, language, session['username'])
    if not letter_id:
        return jsonify({"error": "Could not insert letter."}), 500

    if not send_letter(conn, letter_id, recipient):
        return jsonify({"error": "Could not send letter."}), 500

    return jsonify({"success": "Letter sent successfully."})

@app.route('/read')
def read():
    letter_id, time_sent = session['unread_letters'].pop()
    conn = connect_db(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    if not conn:
        return jsonify({"error": "Could not connect to the database."}), 500
    # Mark letter as read
    update_letter(conn, letter_id, status='read')
    # Get letter info
    letter = get_letter(conn, letter_id)
    content = letter[1]
    writer = letter[3]
    writer_name = get_user(conn, writer)[2]

    return render_template('read.html', from_name=writer_name, to_name=session['name'], content=content)


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
    

