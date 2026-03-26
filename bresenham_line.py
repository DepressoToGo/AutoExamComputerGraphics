
def draw_line(start_point: list[int], end_point: list[int]):
    if start_point[0] != end_point[0]:
        bresenham_no_restrictions = prepare_bresenham(start_point[0], start_point[1], end_point[0], end_point[1])
        x1 = bresenham_no_restrictions[0]
        y1 = bresenham_no_restrictions[1]
        x2 = bresenham_no_restrictions[2]
        y2 = bresenham_no_restrictions[3]
        dy = bresenham_no_restrictions[4]
        dx = x2 - x1
        ydecrement = bresenham_no_restrictions[5]
        modifications = bresenham_no_restrictions[6]
        
        line = bresenham(x1, y1, x2, dx, dy, ydecrement,y2)
        
        final_line = finalize_bresenham(line, modifications)

    else:
        final_line = draw_vert_line(start_point[0], start_point[1], end_point[1])

    return final_line

def prepare_bresenham(x1: int, y1: int, x2: int, y2: int):
    modifications = []
    dy = y2 - y1
    dx = x2 - x1
    m = dy / dx
    ydecrement = False

    while (x1 > x2) or (abs(m) > 1) or (m < 0):
        if x1 > x2:
            tempx = x1
            tempy = y1
            x1 = x2
            y1 = y2
            x2 = tempx
            y2 = tempy
            dy = y2 - y1
            dx = x2 - x1
            m = dy / dx
            modifications.append("invert_p1p2")

        elif abs(m) > 1:
            tempp1 = [x1, y1]
            tempp2 = [x2, y2]
            x1 = tempp1[1]
            y1 = tempp1[0]
            x2 = tempp2[1]
            y2 = tempp2[0]
            dy = y2 - y1
            dx = x2 - x1
            m = dy / dx
            modifications.append("invert_xy")
        elif m < 0:
            dy = abs(dy)
            ydecrement = True
            m = dy / dx

    return x1, y1, x2, y2, dy, ydecrement, modifications


def bresenham(x1: int, y1: int, x2: int, dx: int, dy: int, ydecrement: bool, y2:int):
    line = []
    incE = 2 * dy
    incNE = 2 * dy - 2 * dx
    d = 2 * dy - dx
    y = y1
    directiony = 1
    print("Pour Bresenham")
    print("P1= ("+str(x1)+","+str(y1)+")")
    print("P2= ("+str(x2)+","+str(y2)+")")
    print("dx= "+str(dx))
    print("dy= "+str(dy))
    if ydecrement:
        directiony = -1
        print("y--")
    else:
        print("y++")
    print("incE = 2dy= "+str(incE))
    print("incNE = 2dy - 2dx= "+str(incNE))
    print("X     | Y     |      D  | dir |")
    for x in range(x1, x2 + 1):
        if d <= 0:
            d += incE
            print(str(x)+" | ",str(y)," | ",str(d)," | ","E"," | ")
            line.append([x, y,"E"])
        else:
            d += incNE
            print(str(x)+" | ",str(y)," | ",str(d)," | ","NE"," | ")
            line.append([x, y, "NE"])
            y = y + directiony
    return line


# Défaire Modifications
def finalize_bresenham(line: list, modifications: list):
    new_line = []
    while modifications:
        modif = modifications.pop()
        if modif == 'invert_p1p2':
            line.reverse()
        elif modif == 'invert_xy':
            while line:
                current_point = line.pop(0)
                new_line.append([current_point[1], current_point[0],current_point[2]])
            line = new_line
    return line


def draw_vert_line(x1: int, y1: int, y2: int):
    line = []
    if y2 < y1:
        for y in range(y2, y1):
            line.append([x1, y])
        line.reverse()
    else:
        for y in range(y1, y2):
            line.append([x1, y])
    return line
