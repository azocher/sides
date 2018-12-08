import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import csv

# Connect to DB for import
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Create db/table schema
db.execute("CREATE TABLE books (isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year INTEGER NOT NULL);")
db.commit()

# open .csv file
books = open('books.csv', "r", newline='')
reader = csv.DictReader(books)
for line in reader:
    #organize values
    isbn = line['isbn']
    title = line['title']
    author = line['author']
    year = line['year']

    db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn": isbn, "title": title, "author": author, "year": year})
    db.commit()
    print("Added new line")
