# import the Flask (web app) framework for Python
from flask import Flask

# variable for assigning the script as a programme or module based on line 13
app = Flask(__name__)

# take the user to the URL '/' i.e. homepage and display text
@app.route('/')
def index():
    return '<h1>Hello there, Jay</h2>'

# only execute code if run as a programme (opposed to as a module)
if __name__ == "__main__":
    app.run(debug=True)