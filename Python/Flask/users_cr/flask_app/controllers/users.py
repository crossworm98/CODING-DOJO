from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User

@app.route('/user')
def user():
    return render_template('create.html')
@app.route('/create', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    userid = User.save(data)
    return redirect(f'/read/{userid}')

@app.route('/read/<int:id>')
def read_user(id):
    data = {
        "id": id
    }
    user = User.pickone(data)
    return render_template('read.html', user = user)

@app.route('/edit/<int:id>')
def edit_user(id):
    data = {
        "id": id
    }
    user = User.pickone(data)
    return render_template('edit.html', user = user)

@app.route('/postedit/<int:id>', methods=["POST"])
def postedit(id):
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "id": id
    }
    User.pickone(data)
    userid = User.update(data)
    return redirect(f'/read/{id}')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/showall')

@app.route('/showall')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)