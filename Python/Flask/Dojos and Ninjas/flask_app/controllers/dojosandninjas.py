from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', all_dojos=dojos)

@app.route('/newdojo', methods=['POST'])
def newdojo():
    data = {
        "name": request.form["name"]
    }
    dojoid = Dojo.save(data)
    return redirect('/')

@app.route('/addninja')
def newninja():
    dojos = Dojo.get_all()
    return render_template('ninjas.html', all_dojos=dojos)

@app.route('/ninjapost', methods=['POST'])
def postninja():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
        "dojoid": request.form["dojoid"]
    }
    ninjasave = Ninja.save(data)
    return redirect('/dojos')

@app.route('/dojoninjas/<int:id>')
def dojo(id):
    dojos = Dojo.pickone({'id':id})
    ninjas = Dojo.dojos_ninjas({'id':id})
    return render_template('dojosninjas.html', dojo = dojos, ninjas = ninjas)
def dojosninjas(id):
    ninjas = Dojo.dojos_ninjas({'id':id})