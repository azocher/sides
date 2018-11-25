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
