#from sqlalchemy import create_engine
#from sqlalchemy.orm import scoped_session, sessionmaker
import csv


# open .csv file
books = open('books.csv', "r")
for line in books:
    print(line)

# Connect to DB for import
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))
