from math import ceil, floor

f = None
with open("input4.txt") as fl:
    f = fl.readlines()

def go_left(tpl):
    return (tpl[0], ceil((tpl[1]+tpl[0])/2))

def go_right(tpl):
    return (ceil((tpl[0]+tpl[1])/2), tpl[1])


_max = 0
ids = []
for line in f:
    row, col = None, None
    rows, cols = (0,127), (0,7)

    for command in line:
        if command == "L":
            cols = go_left(cols)
        elif command == "R":
            cols = go_right(cols)
        elif command == "F":
            rows = go_left(rows)
        elif command == "B":
            rows = go_right(rows)
        print(command)
        print(rows)

    ids.append(rows[0]*8+cols[0])
    if _max < (rows[0]*8+cols[0]):
        _max = rows[0]*8+cols[0]

print(_max)

for i in range(0, 127*8+7):
    if i not in ids:
        if i+1 in ids and i-1 in ids:
            print(i)
            break

