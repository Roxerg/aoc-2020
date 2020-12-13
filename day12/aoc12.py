with open('input12.txt', 'r') as file:
    j = file.readlines()



# part 1
dirs = ["N", "E", "S", "W"]
dir_idx = 1
north = 0
east = 0

for i in j:
    com, num = i[:1], int(i[1:])

    if com == "R" or com == "L":
        dir_mod = (num%89)
        if com == "L":
            dir_mod *= -1
        dir_idx += dir_mod

    if com == "F":
        com = dirs[dir_idx%4]

    if com in dirs:
        if com == "N":
            north += num
        elif com == "E":
            east += num
        elif com == "S":
            north -= num
        elif com == "W":
            east -= num

manhattan_dist = abs(north) + abs(east)
print(manhattan_dist)


# part 2

from math import sin, cos, pi, ceil, floor


dirs = ["N", "E", "S", "W"]
dir_idx = 1

north = 0
east  = 0

w_north = 1
w_east = 10

for i in j:
    com, num = i[:1], int(i[1:])

    if com == "R" or com == "L":
        angle = (num)%89

        if com == "R":
            for i in range(0, angle):
                w_east, w_north = w_north, -w_east
        else:
            for i in range(0, angle):
                w_east, w_north = -w_north, w_east

    if com in dirs:
        if com == "N":
            w_north += num
        elif com == "E":
            w_east += num
        elif com == "S":
            w_north -= num
        elif com == "W":
            w_east -= num
    
    if com == "F":
        north += w_north*num
        east  += w_east*num

    

mandist = abs(north) + abs(east)
print(mandist)