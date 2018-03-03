import models
import stores
from flask import Flask, render_template
import dummy_data as dm


app = Flask(__name__)

member_store = stores.MemberStore()
post_store = stores.PostStore()

from views import *
if __name__ == "__main__":
    dm.seed_stores(member_store, post_store)
    app.run()
