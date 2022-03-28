from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.artist import Artist
from flask_app.models.painting import Painting
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regpost', methods=['POST'])
def regpost():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirmpass": request.form["confirmpass"]
    }
    if not Artist.validate_artist(data):
        return redirect('/')
    data['password'] = bcrypt.generate_password_hash(request.form['password'])
    artist_id = Artist.register(data)
    session['artist_id'] = artist_id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    artist_id = session['artist_id']
    artist = Artist.get_all()
    painting = Painting.getall_paintings()
    return render_template('dashboard.html', artist=artist, paint=painting)

@app.route('/login', methods=['POST'])
def login():
    data = {"email": request.form['email']}
    artist_in_db = Artist.get_email(data)
    if not artist_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(artist_in_db.password, request.form['password']):
        flash('Invalid Email/Password')
        return redirect('/')
    session['artist_id'] = artist_in_db.id
    return redirect('/dashboard')

@app.route('/addpainting')
def addpainting():
    return render_template('addpainting.html')

@app.route('/postpainting', methods=['POST'])
def postpainting():
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        'artist_id': session['artist_id']
    }
    if not Painting.validate_painting(data):
        return redirect('/addpainting')
    painting_id = Painting.save(data)
    session['painting_id'] = painting_id
    return redirect('/dashboard')

@app.route('/editpainting/<int:id>')
def editpainting(id):
    data = {
        "id": id
    }
    painting = Painting.pickone(data)
    return render_template('edit.html', painting=painting)

@app.route('/postedit/<int:id>', methods=['POST'])
def postedit(id):
    data = {
        "title": request.form['title'],
        "description": request.form['description'],
        "price": request.form['price'],
        "id":id
    }
    if not Painting.validate_painting(data):
        return redirect(f'/editpainting/{id}')
    Painting.update(data)
    return redirect('/dashboard')

@app.route('/paintings/<int:id>')
def showpainting(id):
    painting = Painting.pickone({'id': id})
    artist = Artist.get_artist({'id':painting.artist_id})
    return render_template('painting.html', artist=artist, painting=painting)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    Painting.delete(data)
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

