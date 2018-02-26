from flask import Flask, render_template
import models
import stores

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")


app.run()