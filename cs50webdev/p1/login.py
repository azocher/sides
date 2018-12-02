from flask import render_template, redirect, url_for, session

def login_check(db, username, password):

    #if already loged in, redirect to Main
    if 'username' in session:
        return redirect(url_for('index'))

    # ELSE, query db to see if login credentials valid
    user = db.execute("SELECT * FROM users WHERE username = :username", {"username": username})
    user_db = user.rowcount
    if user_db < 1:
        return render_template("login.html", registered = False)
    else:
        user_pass = db.execute("SELECT password FROM users WHERE username = :username", {"username": username}).first()
        if user_pass[0] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template("login.html", error = True)


def register_check(db, username, password):
    print("made it into the function")
    user_num = db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).rowcount
    print("Got username check. Result: ")
    print(user_num)
    if user_num < 1:
        unique_id = db.execute("SELECT * FROM users").rowcount + 1
        db.execute("INSERT INTO users (unique_id, username, password) VALUES (:unique_id, :username, :password)", {"unique_id": unique_id, "username": username, "password": password})
        db.commit()
        return redirect(url_for('login', registered = True))
    else:
        return render_template("register.html", error = True)
