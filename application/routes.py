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
    #cavern_map = ['01011011100011110010']
    '''
    cavern_row = cavern_map[0].split('0')
    cavern_row = [i for i in cavern_row if i]
    print(cavern_row)
    '''
    m='1'
    n='0'
    cnt = 0
    pnts = []
    for i in cavern_map[0]:
        if i == n:
            cnt += 1
        else:
            pnts.append(cnt)
            cnt = 1
            m,n = n,m
    pnts.append(cnt)
    for i in range(1,len(pnts),2):
        x = random.randint(0,4)
        if x == 1:
            pnts[i-1] -= 1
            pnts[i] += 1
    print(pnts)
    new_row = ""
    for l in range(15):
        b = '0'
        li = ['0', '1', '2', '3']
        x = random.choices(li, k=8)
        print (x)
        for i in pnts:
            new_row += b*i
            if b == '0':
                b = '1'
            else:
                b = '0'
        print(new_row)
        cavern_map.append(new_row)
    return render_template("cavern2.html", map=cavern_map, nav_cavern2="active")

@app.route("/cavern3")
def cavern3():
    cavern_seed = random.randrange(1000,9999)*1000
    cavern_map = ['00000001111110000000']
    cavern_map = ['00011111100011110000']
    cavern_row = []
    test = '0'
    temp = ''
    for i in range(len(cavern_map[0])):
        print("###" + str(i))
        if cavern_map[0][i] == test:
            temp += test
        else:
            cavern_row.append(i)
            temp = '1' if temp == '0' else '0'
    cavern_row.append(temp)
    print(cavern_row)
    paths = random.randrange(0, 2**(len(cavern_row)//2)+1)
    print(paths)
    #for j in cavern_row:
    #    print(j)
    return render_template("cavern2.html", map=cavern_map, nav_cavern2="active")