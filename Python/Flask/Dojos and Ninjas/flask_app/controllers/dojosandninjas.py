from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
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