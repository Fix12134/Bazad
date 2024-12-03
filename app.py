from flask import Flask, render_template, url_for, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('Main.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        login_name TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        registration_date DATE DEFAULT CURRENT_DATE
    )''')

    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('Main.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/register', methods=['POST'])
def register():
    login_name = request.form['login_name']
    password = request.form['password']
    email = request.form['email']

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO Users (login_name, password, email) VALUES (?, ?, ?)',
                       (login_name, password, email))
        conn.commit()
    except sqlite3.IntegrityError:
        print("не туда попал")
    finally:
        conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)