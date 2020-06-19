from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", nav_index="active")

@app.route("/cavern")
def cavern():
    x = [1,0,0]
    return render_template("cavern.html", nav_cavern="active")