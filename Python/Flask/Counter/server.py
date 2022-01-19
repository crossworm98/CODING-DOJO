from flask import Flask, session, render_template, request, redirect
app = Flask(__name__)  
app.secret_key = 'random'

@app.route("/")
def counter():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html')

@app.route("/add2")
def addcount():
    session['count'] += 1
    return redirect('/')

@app.route("/reset")
def reset():
    session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)