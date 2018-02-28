import models
import stores
from flask import Flask, render_template
import models
import stores
import auxiliary as aux

app = Flask(__name__)

post_store = stores.PostStore()
aux.post_store_should_add_posts(aux.create_posts(), post_store)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())



app.run()
