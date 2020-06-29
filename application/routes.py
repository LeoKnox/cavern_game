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

@app.route("/cavern2")
def cavern2():
    cavern_seed = random.randrange(1000,9999)*1000
    cavern_map = ['00000001111110000000']
    cavern_map = ['00011111100011110000']
    cavern_row = []
    test = '0'
    temp = ''
    for i in range(len(cavern_map[0])):
        print(i)
        if cavern_map[0][i] == test:
            temp += test
        else:
            cavern_row.append(temp)
            temp = ''
            if test == '0':
                test = '1'
            else:
                test = '0'
    cavern_row.append(temp)
    print(cavern_row)
    paths = random.randrange(0, 2**(len(cavern_row)//2)+1)
    print(paths)
    #for j in cavern_row:
    #    print(j)
    return render_template("cavern2.html", map=cavern_map, nav_cavern2="active")