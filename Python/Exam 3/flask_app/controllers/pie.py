from re import M
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.pie import Pie
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/regpost', methods=['POST'])
def regpost():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email'],
        "password": request.form['password'],
        "confirmpass": request.form['confirmpass']
    }
    if not User.validate_user(data):
        return redirect('/')
    data['password'] = bcrypt.generate_password_hash(request.form['password'])
    user_id = User.register(data)
    session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    data = {'email': request.form['email']}
    user_in_db = User.get_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    id = session['user_id']
    user = User.get_user({'id': id})
    pie = Pie.get_pies({'id': id})
    return render_template('dashboard.html', user=user, pies=pie)

@app.route('/postpie', methods=['POST'])
def postpie():
    data = {
        'name': request.form['name'],
        'filling': request.form['filling'],
        'crust': request.form['crust'],
        'users_id': session['user_id']
    }
    if not Pie.validate_pie(data):
        return redirect('/dashboard')
    pie_id = Pie.save(data)
    session['pie_id'] = pie_id
    return redirect('/dashboard')

@app.route('/editpie/<int:id>')
def editpie(id):
    data = {
        "id": id
    }
    pie = Pie.pickone(data)
    print(pie)
    return render_template('editpie.html', pie=pie)

@app.route('/postedit/<int:id>', methods=['POST'])
def postedit(id):
    data = {
        'name': request.form['name'],
        'filling': request.form['filling'],
        'crust': request.form['crust'],
        'id': id
    }
    if not Pie.validate_pie(data):
        return redirect(f'/editpie/{id}')
    Pie.update(data)
    return redirect('/dashboard')

@app.route('/pies')
def derby():
    pies = Pie.get_all()
    return render_template('derby.html', pies=pies)

@app.route('/show/<int:id>')
def show(id):
    pie = Pie.pickone({"id": id})
    user_id = session['user_id']
    user = User.get_user({'id': user_id})
    return render_template('show.html', pie=pie, user=user)

@app.route('/addvote/<int:id>', methods=['POST'])
def addvote(id):
    Pie.addvote({'id': id})
    return redirect('/pies')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_pie(id):
    Pie.delete({'id': id})
    return redirect('/dashboard')
