from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app.models.survey import Survey

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
    return redirect('/dojos')

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

@app.route('/dojosurvey')
def dojosurvey():
    surveyget = Survey.get_all()
    return render_template('dojosurvey.html', all_dojos=surveyget)

@app.route('/postsurvey', methods=['POST'])
def postsurvey():
    if not Survey.validate_survey(request.form):
        return redirect('/dojosurvey')
    data = {
        "name": request.form["name"],
        "dojoloc": request.form["dojoloc"],
        "dojolang": request.form["dojolang"],
        "comment": request.form["comment"]
    }
    surveysave = Survey.save(data)
    return redirect(f'/results/{surveysave}')

@app.route('/results/<int:id>')
def results(id):
    dojo = Survey.results({'id':id})
    return render_template('results.html', dojo = dojo)