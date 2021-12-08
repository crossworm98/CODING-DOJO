from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', times = 4, times2 = 4)
@app.route('/custom/<int:num>')
def custom(num):
    return render_template('index.html', times = 4, times2 = num)
@app.route('/custom/<int:num>/<int:num2>')
def custom2(num, num2):
    return render_template('index.html', times = num, times2 = num2)

if __name__=="__main__":
    app.run(debug=True)