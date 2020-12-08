
f = None
with open("input2.txt") as fl:
    f = fl.readlines()


trees = 0
x = 0
for line in f:
    #print(x, len(line))
    #print(line)
    if line[x] == '#':
        trees += 1
    x += 3
    if x >= len(line)-1:
        x = x % (len(line)-1)

#print (trees)

## part 2


for xy in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    xx,yy = xy
    print(xx,yy,xy)
    x,y,trees = 0,0,0
    while y < len(f):
        line = f[y]
        if line[x] == '#':
            trees += 1
        y += yy
        x += xx
        if x >= len(line)-1:
            x = x % (len(line)-1)
    print(trees)

for line in f:
    #print(x, len(line))
    #print(line)
    if line[x] == '#':
        trees += 1
    x += 3
    if x >= len(line)-1:
        x = x % (len(line)-1)