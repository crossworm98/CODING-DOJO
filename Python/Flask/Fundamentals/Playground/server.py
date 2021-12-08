from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", times=5)	# notice the 2 new named arguments!
@app.route('/play/<int:num>')
def play(num):
    return render_template("index.html", times=num)
@app.route('/play/<int:num>/<string:color>')
def playcolor(num, color):
    return render_template("index.html", times=num, color=color)
if __name__=="__main__":
    app.run(debug=True)

