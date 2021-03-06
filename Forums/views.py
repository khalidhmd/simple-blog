from flask import render_template, redirect, request, url_for
import models
from app import app, member_store, post_store


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts=post_store.get_all())


@app.route("/topic/add", methods = ["GET", "POST"])
def topic_add():
    if request.method == "GET":
        return render_template("topic_add.html")
    elif request.method == "POST":
        new_post = models.Post(request.form["topictitle"], request.form["topicbody"], 1)
        post_store.add(new_post)
        return redirect(url_for("home"))
