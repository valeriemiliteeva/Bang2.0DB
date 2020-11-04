import data  # projects definitions are placed in different file


# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL of server to render home.html

@app.route('/')
def home_route():
    return render_template("base.html", projects=data.setup())


# connects /hello path of server to render hello.html
@app.route('/hello/')
def hello_route():
    return render_template("hello.html", projects=data.setup())


# connects /flask path of server to render flask.html
@app.route('/flask/')
def flask_route():
    return render_template("flask.html", projects=data.setup())

@app.route('/period2/')
def period2_route():
    return render_template("period2.html", projects=data.setup())

@app.route('/period4/')
def period4_route():
    return render_template("period4.html", projects=data.setup())

@app.route('/period5/')
def period5_route():
    return render_template("period5.html", projects=data.setup())

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
