from re import M
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.seller import Seller
from flask_app.models.car import Car
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
    if not Seller.validate_seller(data):
        return redirect('/')
    data['password'] = bcrypt.generate_password_hash(request.form['password'])
    seller_id = Seller.register(data)
    session['seller_id'] = seller_id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    id = session['seller_id']
    seller = Seller.get_seller({'id': id})
    cars = Car.get_all()
    return render_template('dashboard.html', seller=seller, cars=cars )

@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    car = Car.pickall({"id": id})
    print(car)
    seller = Seller.get_seller({"id": id})
    return render_template('view.html', car=car, seller=seller)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    data = {'email': request.form['email']}
    seller_in_db = Seller.get_email(data)
    if not seller_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(seller_in_db.password, request.form['password']):
        flash('Invalid Email/Password')
        return redirect('/')
    session['seller_id'] = seller_in_db.id
    return redirect('/dashboard')

@app.route('/addcar')
def addcar():
    return render_template('addcar.html')

@app.route('/postcar', methods=['POST'])
def postcar():
    data = {
        'make': request.form['make'],
        'model': request.form['model'],
        'year': request.form['year'],
        'description': request.form['description'],
        'price': request.form['price'],
        'sellers_id': session['seller_id']
    }
    if not Car.validate_car(data):
        return redirect('/addcar')
    car_id = Car.save(data)
    session['car_id'] = car_id
    return redirect('/dashboard')

@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    car = Car.pickone(data)
    return render_template('edit.html', car=car)

@app.route('/postedit/<int:id>', methods=['POST'])
def postedit(id):
    data = {
        'make': request.form['make'],
        'model': request.form['model'],
        'year': request.form['year'],
        'description': request.form['description'],
        'price': request.form['price'],
        'id': id
    }
    if not Car.validate_car(data):
        return redirect(f'/edit/{id}')
    Car.update(data)
    return redirect('/dashboard')


@app.route('/delete/<int:id>')
def delete_pie(id):
    Car.delete({'id': id})
    return redirect('/dashboard')