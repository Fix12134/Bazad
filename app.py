from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3 as _sqlite3


app = Flask(__name__)

with sql.connect("base.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        login_name TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        registration_date DATE DEFAULT CURRENT_DATE
        )""")

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page" + name + "-" + str(id)





if __name__ == "__main__":
    app.run(debug=True)