from application import app
from flask import render_template
import random

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", nav_index="active")

@app.route("/cavern")
def cavern():
    cavern_seed = random.randrange(1000,9999)*1000
    cavern_map = ['00000001111110000000']
    print(cavern_map[0].index('1'))
    return render_template("cavern.html", map=cavern_map, nav_cavern="active")