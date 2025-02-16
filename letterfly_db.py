import psycopg2
        
def connect_db(db_name, db_user, db_password, db_host, db_port):
    """Connect to PostgreSQL and return the connection."""
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print(f"Connected to {db_name} successfully as {db_user}!")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def init_db(conn, testing=False):
    """Initialize the database. Returns True on success, False on failure."""
    try:
        cursor = conn.cursor()
        with open("init_db.sql", "r") as file:
            init_commands = file.read()
        cursor.execute(init_commands)

        if testing:
            with open("test_data.sql", "r") as file:
                test_inserts = file.read()
            cursor.execute(test_inserts)

        conn.commit()
        return True
    except Exception as e:
        print(f"Error initializing the database: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()

def insert_user(conn, username, pwd, name, reads_in, writes_in):
    """Insert a new user into the LetterflyUser table. Returns True on success, False on failure."""
    try:
        cursor = conn.cursor()
        ADD_USER = """INSERT INTO LetterflyUser VALUES (%s, %s, %s, %s, %s);"""
        cursor.execute(ADD_USER, (username, pwd, name, reads_in, writes_in))

        print(f"Added user: {username}")
        conn.commit()
        return True
    except Exception as e:
        print(f"Error inserting user: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()

def get_user(conn, username):
    """Retrieve a user from the users table. Returns a tuple, or None on failure/user does not exist."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM LetterflyUser WHERE username = %s;", (username,))
        user = cursor.fetchone()
        if user:
            return user
        else:
            return None
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None
    finally:
        cursor.close()

def add_friendship(conn, user1, user2):
    """Add a friendship between two users. Returns True on success, False on failure."""
    try:
        cursor = conn.cursor()
        ADD_FRIENDSHIP = """INSERT INTO Friends VALUES (%s, %s);"""
        cursor.execute(ADD_FRIENDSHIP, (user1, user2))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding friendship: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()

def get_friends(conn, username):
    """Retrieve all friends of a user. Returns a list of tuples, or None on failure"""
    try:
        cursor = conn.cursor()
        GET_FRIENDS = """((SELECT friend2 FROM Friends WHERE friend1 = %s)
                         UNION
                         (SELECT friend1 FROM Friends WHERE friend2 = %s))"""
        cursor.execute(GET_FRIENDS, (username, username))
        friends = cursor.fetchall() # This is formatted [(friend1,), (friend2,), ...]
        return [friend[0] for friend in friends]
    except Exception as e:
        print(f"Error fetching friends: {e}")
        return None
    finally:
        cursor.close()

def insert_letter(conn, content, language, writer):
    """Insert a letter into the Letter table. Returns the letter_id on success, None on failure."""
    try:
        cursor = conn.cursor()
        ADD_LETTER = """INSERT INTO Letter (content, language, writer)
                        VALUES (%s, %s, %s)
                        RETURNING letter_id;"""
        cursor.execute(ADD_LETTER, (content, language, writer))
        letter_id = cursor.fetchone()[0]
        conn.commit()
        return letter_id
    except Exception as e:
        print(f"Error inserting letter: {e}")
        conn.rollback()
        return None
    finally:
        cursor.close()

def update_letter(conn, letter_id, content=None, language=None, status=None):
    """Update a letter's content and language. Returns True on success, False on failure."""
    if not (content or language or status):
        return True
    try:
        cursor = conn.cursor()
        if content:
            UPDATE_LETTER_CONTENT = """UPDATE Letter SET content = %s WHERE letter_id = %s;"""
            cursor.execute(UPDATE_LETTER_CONTENT, (content, letter_id))
        if language:
            UPDATE_LETTER_LANGUAGE = """UPDATE Letter SET content = %s WHERE letter_id = %s;"""
            cursor.execute(UPDATE_LETTER_LANGUAGE, (language, letter_id))
        if status:
            UPDATE_LETTER_STATUS = """UPDATE Letter SET content = %s WHERE letter_id = %s;"""
            cursor.execute(UPDATE_LETTER_STATUS, (status, letter_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating letter: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()

def delete_letter(conn, letter_id):
    """Delete a letter. Returns True on success, False on failure."""
    try:
        cursor = conn.cursor()
        DELETE_LETTER = """DELETE FROM Letter WHERE letter_id = %s;"""
        cursor.execute(DELETE_LETTER, (letter_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error deleting letter: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()

def get_letter(conn, letter_id):
    """Retrieve a letter from the Letter table. Returns a tuple, or None on failure."""
    try:
        cursor = conn.cursor()
        GET_LETTER = """SELECT * FROM Letter WHERE letter_id = %s;"""
        cursor.execute(GET_LETTER, (letter_id,))
        letter = cursor.fetchone()
        return letter
    except Exception as e:
        print(f"Error fetching letter: {e}")
        return None
    finally:
        cursor.close()

def get_letters(conn, username, status=None):
    """Retrieve all letters sent to a user. Returns a list of tuples, or None on failure."""
    try:
        cursor = conn.cursor()
        if status:
            GET_LETTERS = """SELECT letter, time_sent FROM SentTo
                             WHERE recipient = %s AND status = %s
                             ORDER BY time_sent DESC;"""
            cursor.execute(GET_LETTERS, (username, status))
        else:
            GET_LETTERS = """SELECT letter, time_sent FROM SentTo
                             WHERE recipient = %s
                             ORDER BY time_sent DESC;"""
            cursor.execute(GET_LETTERS, (username,))
        letters = cursor.fetchall()
        return letters
    except Exception as e:
        print(f"Error fetching letters: {e}")
        return None
    finally:
        cursor.close()

def send_letter(conn, letter_id, recipient):
    """Send a letter to a recipient. Returns True on success, False on failure."""
    try:
        cursor = conn.cursor()
        SEND_LETTER = """INSERT INTO SentTo (recipient, letter, status) VALUES (%s, %s, 'unread');"""
        cursor.execute(SEND_LETTER, (recipient, letter_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error sending letter: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()

def send_msg_in_bottle(conn, letter_id, letter_language, writer_reads_in):
    """Send a message in a bottle to a random compatible user. Returns the recipient's username, 
    or None if no compatible user exists/failure."""
    try:
        cursor = conn.cursor()
        FIND_RECIPIENT = """SELECT username FROM LetterflyUser
                            WHERE %s = ANY (reads_in) AND %s::VARCHAR[] && writes_in
                            ORDER BY RANDOM() LIMIT 1;"""
        cursor.execute(FIND_RECIPIENT, (letter_language, writer_reads_in))
        recipient = cursor.fetchone()
        if recipient:
            SEND_MSG_IN_BOTTLE = """INSERT INTO SentTo (recipient, letter, status) VALUES (%s, %s, 'bottled');"""
            cursor.execute(SEND_MSG_IN_BOTTLE, (recipient, letter_id))
            conn.commit()
            return recipient
        else:
            print("No compatible user found.")
            return None
    except Exception as e:
        print(f"Error sending message in bottle: {e}")
        conn.rollback()
        return None
    finally:
        cursor.close()

def get_users(conn):
    """Retrieve all users from the users table. Returns a list of tuples, or None on failure."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM LetterflyUser;")
        users = cursor.fetchall()
        for user in users:
            print(user)
        return users
    except Exception as e:
        print(f"Error fetching users: {e}")
        return None
    finally:
        cursor.close()

