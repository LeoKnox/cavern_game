from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", nav_index="active")

@app.route("/cavern")
def cavern():
    x = [0,1,1,0]
    cavern_map = [
        [0,1,1,0,0],
        [0,1,1,1,0]
    ]
    return render_template("cavern.html", map=cavern_map, nav_cavern="active")