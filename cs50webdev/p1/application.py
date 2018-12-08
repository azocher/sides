import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# personal functions
from login import login_check, register_check

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        # collect inputs
        type = str(request.form.get("type")).lower()
        input = str(request.form.get("input"))

        # search for type criteria in db
        statement = "SELECT * FROM books WHERE " + type + " = :input"
        results = db.execute(statement, {"input": input}).fetchall()
        print(len(results))
        return render_template('main.html', results=results)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = str(request.form.get("username"))
        password = str(request.form.get("password"))
        return login_check(db, username, password)
    else:
        return render_template('login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = str(request.form.get("username"))
        password = str(request.form.get("password"))
        return register_check(db, username, password)
    else:
        return render_template('register.html')

@app.route("/logout", methods=['GET'])
def logout():
    session.pop('username', None)
    return render_template('logout.html')
