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
    j = '1'
    walls = []
    i = 0
    while i < 20 and cavern_map[0].find(j) != -1:
        if cavern_map[0].find(j) == -1:
            break;
        t = cavern_map[0].index(j, i)
        walls.append(t)
        print(walls)
        i = t
        if j == '1':
            j = '0'
        else:
            j = '1'
        i += 1
    print(walls)
    return render_template("cavern.html", map=cavern_map, nav_cavern="active")