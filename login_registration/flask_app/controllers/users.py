from flask_app import app
from flask_app.models.user import User
from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")


# Create new user
@app.route('/register', methods=['POST'])
def register():
    # Validate registration
    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/')
    
    # If registration is valid, save
    new = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(new)
    if not id:
        flash("Email already in use")
        return redirect('/')
    session['user_id'] = id
    return redirect('/home')


# User Login
@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)

# Check if user is in db and if password is correct
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Incorrect Email/Password")
        return redirect('/')

# Log user in
    session['user_id'] = user_in_db.id
    return redirect('/home')

# User Page
@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/')
    data = { "id": session['user_id']}
    user = User.get_one(data)
    return render_template("user.html", user=user)

# Logout, clears session
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')