from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.users import User
from flask_app.models.shows import Show
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regpost', methods=['POST'])
def regpost():
    data = {
        "fname": request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirmpass': request.form['confirmpass']
    }
    if not User.validate_user(data):
        return redirect('/')
    data['password'] = bcrypt.generate_password_hash(request.form['password'])
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    shows = Show.get_shows()
    user_id = session['user_id']
    user = User.get_user({'id':user_id})
    return render_template('dashboard.html', user=user, shows=shows)

@app.route('/login', methods=['POST'])
def login():
    data = {'email': request.form['email']}
    user_in_db = User.get_email(data)
    if not user_in_db:
        flash('Invalid email/password')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid email/password')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/addshow')
def addshow():
    return render_template('addshow.html')

@app.route('/postshow', methods=['POST'])
def postshow():
    data = {
        'title': request.form['title'],
        'network': request.form['network'],
        'release_date': request.form['date'],
        'comments': request.form['comments']
    }
    if not Show.validate_show(data):
        return redirect('/addshow')
    show_id = Show.save(data)
    session['show_id'] = show_id
    return redirect('/dashboard')

@app.route('/showdetails/<int:id>')
def showdetails(id):
    show = Show.get_show({'id':id})
    user_id = session['user_id']
    user = User.get_user({'id':user_id})
    return render_template('show.HTML', shows=show, user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    Show.delete(data)
    return redirect('/dashboard')

@app.route('/editshow/<int:id>')
def editshow(id):
    data = {
        "id": id
    }
    show = Show.pickone(data)
    return render_template('edit.html', show=show)

@app.route('/postedit/<int:id>', methods=['POST'])
def postedit(id):
    data = {
        "title": request.form['title'],
        "network": request.form['network'],
        "date": request.form['date'],
        "comments": request.form['comments'],
        "id":id
    }
    if not Show.validate_show(data):
        return redirect(f'/editshow/{id}')
    Show.update(data)
    return redirect('/dashboard')