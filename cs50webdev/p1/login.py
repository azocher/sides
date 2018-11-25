from flask import render_template, redirect, url_for

def login_check(db, username, password):
    user_db = db.execute("SELECT * FROM users WHERE username = :username", {"username": username})
    if user_db < 1:
        return "Error"
    else:
        user_pass = db.execute("SELECT password FROM users WHERE username = :username", {"username: username"})
        if user_pass == password:
            return render_template('main.html')
        else:
            return "Passwords do not match"


def register_check(db, username, password):
    print("made it into the function")
    user_num = db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).rowcount
    print("Got username check. Result: ")
    print(user_num)
    if user_num < 1:
        unique_id = db.execute("SELECT * FROM users").rowcount + 1
        db.execute("INSERT INTO users (unique_id, username, password) VALUES (:unique_id, :username, :password)", {"unique_id": unique_id, "username": username, "password": password})
        db.commit()
        return render_template("login.html", registered = True)
    else:
        return render_template("register.html", error = True)
