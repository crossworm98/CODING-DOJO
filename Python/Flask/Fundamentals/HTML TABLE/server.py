from flask import Flask, render_template
app = Flask(__name__)


@app.route("/<string:f_name>/<string:l_name>/<string:full_name>")
def grid(f_name, l_name, full_name):
    return render_template("index.html", fname=f_name, lname=l_name, fullname=full_name)


if __name__ == "__main__":
    app.run(debug=True)

users = [
    {'first_name': 'Michael', 'last_name': 'Choi'},
    {'first_name': 'John', 'last_name': 'Supsupin'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
