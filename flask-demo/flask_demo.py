from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route("/sayhello/<username>")
def sayhello(username):
    return "Hello " + username

app.run()
