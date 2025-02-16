from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS
from letterfly_db import *
from letterfly_translate import *
import os

app = Flask(__name__, static_url_path='/static')
CORS(app)
session = {'logged_in': False,
           'username': None, 
           'name': None, 
           'reads_in': None, 
           'writes_in': None, 
           'unread_letters': None, 
           'bottled_letters': None, 
           'read_letters': None}


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
        return jsonify({"status": "error", "message": "Could not connect to the database."}), 500  # Internal Server Error

    user = get_user(conn, username)
    if not user:
        return jsonify({"status": "error", "message": "User not found."}), 404  # Not Found

    if password != user[1]:
        return jsonify({"status": "error", "message": "Incorrect password."}), 401  # Unauthorized

    session['logged_in'] = True
    session['username'] = username
    return jsonify({"status": "success", "message": f"Login successful! Welcome, {session['username']}."})
    
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

    # Database connection
    conn = connect_db(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    if not conn:
        return jsonify({"status": "error", "message": "Could not connect to the database."}), 500

    # Try inserting user into the database
    if not insert_user(conn, username, password, name, reads_in, writes_in):
        return jsonify({"status": "error", "message": "Could not insert user."}), 500

    # Return success response
    return jsonify({"status": "success", "message": "Signup successful!"})

@app.route('/dashboard')
def dashboard():
    if not session['logged_in']:
        return redirect(url_for('letterfly'))
    username = session['username']
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
    language = detect_lang(content)
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

@app.route('/read', methods=['GET'])
def read():
    target_lang = request.args.get('target_lang')
    letter_id, time_sent = session['unread_letters'].pop()
    conn = connect_db(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    if not conn:
        return jsonify({"error": "Could not connect to the database."}), 500
    # Mark letter as read
    update_letter(conn, letter_id, status='read')
    # Get letter info
    letter = get_letter(conn, letter_id)
    writer = letter[3]
    writer_name = get_user(conn, writer)[2]
    html_content = letter[1]
    if target_lang:
        html_content = translate_html(html_content, target_lang)
    return render_template('read.html', from_name=writer_name, to_name=session['name'], content=html_content)


if __name__ == '__main__':
    conn = connect_db(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    if not conn:
        print("Exiting...")
        exit()
    init_db(conn)
    conn.close()
    app.run(host="localhost", port=5000, debug=True)
    

