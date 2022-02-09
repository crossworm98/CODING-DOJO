from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.register import Register
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/regpost", methods=["POST"])
def regpost():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirmpass": request.form["confirmpass"]
    }
    if not Register.validate_user(data):
        return redirect('/')
    data['password'] = bcrypt.generate_password_hash(request.form['password'])
    user_id = Register.save(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    user_id = session['user_id']
    user = Register.get_user({'id':user_id})
    print(user)
    return render_template('dashboard.html', user = user)

@app.route('/login', methods=["POST"])
def login():
    data = {"email": request.form['email']}
    user_in_db = Register.get_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
