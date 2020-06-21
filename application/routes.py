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
    cavern_map2 = []
    random.seed(cavern_seed)
    cavern_map = [0 for _ in range (random.randrange(6,11))]
    cavern_map.extend([1 for _ in range (5, 10)])
    cavern_map.extend([0 for _ in range (6, 10)])
    print (cavern_map)
    cavern_map2.append(cavern_map)
    print(cavern_map.index(1))
    return render_template("cavern.html", map=cavern_map2, nav_cavern="active")