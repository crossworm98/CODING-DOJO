from flask import Flask, render_template, session, redirect,request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/dojosurvey')
def dojosurvey():
    return render_template('index.html')

@app.route('/postsurvey', methods=['POST'])
def postsurvey():
    print("Got info")
    session['name'] = request.form['name']
    session['dojolocation'] = request.form['dojoloc']
    session['dojolanguage'] = request.form['dojolang']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html', name=session['name'], dojolocation=session['dojolocation'], dojolanguage=session['dojolanguage'], comment=session['comment'])





if __name__=="__main__":
    app.run(debug=True)