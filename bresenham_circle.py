from math import *


def draw_circle(start_point: list, rayon: int):
    circle = []
    circle_slice = []
    x = 0
    y = rayon
    d = (5.0 / 4.0) - rayon
    xc = start_point[0]
    yc = start_point[1]
    print("d0="+str(d))
    print("incE=2x+3")
    print("incSE=2x-2y+5")
    print("X | Y |      D       | dir | inc      |")
    while y >= x:
        incE = 2 * x + 3
        incSE = 2 * x - 2 * y + 5
        if d < 0:
            print(str(xc+x)+" | ",str(yc+y)," | ",str(d)," | ","E"," | ",str(incE))
            circle_slice.append([xc + x, yc+y,"deltax: "+str(x),"deltay:"+str(y), "E",incE])
            d = d + incE
        else:
            print(str(xc+x)+" | ",str(yc+y)," | ",str(d)," | ","SE"," | ",str(incSE))
            circle_slice.append([xc + x, yc+y,"deltax: "+str(x),"deltay:"+str(y), "SE",incSE])
            d = d + incSE
            y = y - 1
        circle.append([xc + x, yc + y])
        circle.append([xc + x, yc - y])
        circle.append([xc + y, yc + x])
        circle.append([xc + y, yc - x])
        circle.append([xc - x, yc - y])
        circle.append([xc - y, yc - x])
        circle.append([xc - x, yc + y])
        circle.append([xc - y, yc + x])
        x = x + 1
    print(str(xc+x)+" | ",str(yc+y)," | ","-"," | ","-"," | ","-")
    circle_slice.append([xc + x, yc + y,"deltax: "+str(x),"deltay:"+str(y)])
    return circle_slice
