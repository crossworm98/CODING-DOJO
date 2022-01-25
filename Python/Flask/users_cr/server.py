from flask import Flask, render_template, request, redirect
app = Flask(__name__)
################################################################
from user import User
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

@app.route('/read/edit/<int:id>', methods=["POST"])
def edit_user(id, data):
    data = {
        "id": id
    }
    user = User.pickone(data)
    return render_template('edit.html')


@app.route('/showall')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)


if __name__ == "__main__":
    app.run(debug=True)