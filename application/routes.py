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
    while i < 20 or cavern_map[0].count(j, i):
        i = cavern_map[0].find(j, i)
        if i == -1:
            break
        walls.append(i)
        if j == '0':
            j = '1'
        else:
            j = '0'
        i += 1
    for x in range(15):
        r = random.randrange(1,4)
        cavern_map2 = list(cavern_map[x])
        if r == 1:
            if random.randrange(0,3):
                cavern_map2[walls[0]-1] = '1'
                walls[0] -= 1
            else:
                cavern_map2[walls[0]+1] = '0'
                walls[0] += 1
        elif r == 2:
            if random.randrange(0,3):
                cavern_map2[walls[1]] = '1'
                walls[1] += 1
            else:
                cavern_map2[walls[1]-1] = '0'
                walls[1] -= 1
        cavern_map2 = "".join(cavern_map2)
        cavern_map.append(cavern_map2)
        print (cavern_map)
    return render_template("cavern.html", map=cavern_map, nav_cavern="active")