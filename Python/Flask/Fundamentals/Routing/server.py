from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<string:name>')
def say_flask(name):
    print(name)
    return "Hello, " + name
@app.route('/repeat/<int:num>/<string:name>')
def repeat(name, num):
    print(num)
    print(name)
    return f'{name}' * num
# Return the string 'Hello World!' as a response

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
