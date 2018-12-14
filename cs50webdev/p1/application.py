import os, requests

from flask import Flask, session, render_template, request, redirect, url_for, abort, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# personal functions
from login import login_check, register_check
from stars import star_rating

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
        if 'username' in session:
            return render_template('main.html')
        else:
            return redirect(url_for('login'))
    else:
        # collect inputs
        type = str(request.form.get("type")).lower()
        input = "%" + str(request.form.get("input")) + "%"

        # search for type criteria in db
        statement = "SELECT * FROM books WHERE " + type + " LIKE :input"
        results = db.execute(statement, {"input": input}).fetchall()
        return render_template('main.html', results=results)

@app.route("/book/<isbn>", methods=['GET', 'POST'])
def book(isbn):

    if request.method == 'GET':
        # Goodreads API call
        key = os.getenv("API_KEY")
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": key, "isbns": isbn})
        data = res.json()
        rating = data["books"][0]["average_rating"]
        count = data["books"][0]["work_text_reviews_count"]
        stars = star_rating(rating)

        # make isbn call to books.csv
        info = db.execute("SELECT author, title, year FROM books WHERE isbn = :isbn", {"isbn" : isbn}).first()
        title = info['title']
        author = info['author']
        year = info['year']
        cover_img="http://covers.openlibrary.org/b/isbn/" + isbn + "-M.jpg"

        # pull all reviews
        reviews = db.execute("SELECT * FROM reviews WHERE isbn = :isbn", {"isbn" : isbn}).fetchall()

        # check for reviews by current user
        offer = True
        for review in reviews:
            print(review)
            if (review[0] == session['username']):
                offer = False

        return render_template('book.html', title=title, author=author, cover_img=cover_img, year=year, stars=stars, count=count, offer=offer, reviews=reviews)
    else:
        rating = float(request.form.get("rating"))
        title = str(request.form.get("title"))
        review = str(request.form.get("review"))

        db.execute("INSERT INTO reviews (username, isbn, rating, title, review_text) VALUES (:username, :isbn, :rating, :title, :review_text)", {"username": session['username'], "isbn": isbn, "rating": rating, "title": title, "review_text": review})
        db.commit()
        return redirect(url_for('book', isbn=isbn))


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

@app.route("/api/<isbn>")
def api(isbn):
    # get info from Books.csv file
    info = db.execute("SELECT author, title, year FROM books WHERE isbn = :isbn", {"isbn" : isbn}).first()
    # if no instance of isbn, return 404 error
    if info == None:
        return abort(404)
    title = info['title']
    author = info['author']
    year = info['year']

    # get info from reviews DB
    reviews = db.execute("SELECT * FROM reviews WHERE isbn = :isbn", {"isbn" : isbn}).fetchall()
    review_count = len(reviews)
    average = db.execute("SELECT AVG(rating) FROM reviews WHERE isbn = :isbn", {"isbn" : isbn}).first()

    return jsonify(title=title, author=author, year=year, isbn=isbn, review_count=review_count, average_score=average[0])
