from flask import *
app = Flask("Artfolio")
import sqlite3

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

def connect_db():
    conn = sqlite3.connect('profiles.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/profile/<ID>")
def detail(ID):
    conn = connect_db()
    current_profile = conn.execute('SELECT * FROM profil', [ID]).fetchone()
    conn.close()
    return render_template("profile.html", profile=current_profile)