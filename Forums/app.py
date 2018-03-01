import models
import stores
from flask import Flask, render_template
import models
import stores
import dummy_data as dm

app = Flask(__name__)

post_store = stores.PostStore()
for post in dm.create_posts():
    post_store.add(post)


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())



app.run()
