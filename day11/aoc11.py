import copy

def yeet(x):
    return [convert(z) for z in x if z != "\n"]

def convert(i):
    if i == "L":
        return False
    elif i == ".":
        return None




with open('input11.txt', 'r') as file:
    fff = file.readlines()
    j = [yeet(x) for x in fff]

f = copy.deepcopy(j)
g = copy.deepcopy(j)
print(len(fff))
print(len(fff[0]))


def flipShit(y, x, N):

    if N[y][x] == None:
        return None


    neigbourinos = set([
        (-1,-1), (-1,0), (-1,1),
        ( 0,-1),         ( 0,1),
        ( 1,-1), ( 1,0), ( 1,1)  
    ])
    if x==0:
        for naughty in [(-1,-1),(0,-1),(1,-1)]:
            if naughty in neigbourinos:
                neigbourinos.remove(naughty)
    if x==len(N[y])-1:
        for naughty in [(-1,1),(0,1),(1,1)]:
            if naughty in neigbourinos:
                neigbourinos.remove(naughty)
    if y==0:
        for naughty in [(-1,-1),(-1,0),(-1,1)]:
            if naughty in neigbourinos:
                neigbourinos.remove(naughty)
    if y==len(N)-1:
        for naughty in [(1,-1),(1,0),(1,1)]:
            if naughty in neigbourinos:
                neigbourinos.remove(naughty)
    
    occupado = 0
    for yi,xi in neigbourinos:
        place = N[y+yi][x+xi]
        if place != None:
            if place:
                #print(occupado)
                occupado += 1
    
    
    if occupado > 0 and y == 0:
        #print("---")
        for yi,xi in neigbourinos:
            pass #print(f[y+yi][x+xi])

    if occupado == 0 and not N[y][x] :
        return True
    if occupado >= 4 and N[y][x]:
        return False

    return N[y][x]

new_f = copy.deepcopy(f)
loopin = True


# part 1
while loopin:

    for y in range(0, len(f)):
        for x in range(0, len(f[y])):
            new_f[y][x] = flipShit(y,x,f)
    
    if new_f == f:
        loopin = False

    f = copy.deepcopy(new_f)

counterino = 0
for y in range(0, len(f)):
        for x in range(0, len(f[y])):
            if f[y][x]:
                counterino += 1


print(counterino)


# part 2

def flipVisibleShit(y,x,N):

    if N[y][x] == None:
        return None

    neigbourinos = set([
        (-1,-1), (-1,0), (-1,1),
        ( 0,-1),         ( 0,1),
        ( 1,-1), ( 1,0), ( 1,1)  
    ])
    if x==0:
        for naughty in [(-1,-1),(0,-1),(1,-1)]:
            if naughty in neigbourinos:
                neigbourinos.remove(naughty)
    if x==len(N[y])-1:
        for naughty in [(-1,1),(0,1),(1,1)]:
            if naughty in neigbourinos:
                neigbourinos.remove(naughty)
    if y==0:
        for naughty in [(-1,-1),(-1,0),(-1,1)]:
            if naughty in neigbourinos:
                neigbourinos.remove(naughty)
    if y==len(N)-1:
        for naughty in [(1,-1),(1,0),(1,1)]:
            if naughty in neigbourinos:
                neigbourinos.remove(naughty)

    # neigbourinos are actually directionerinos, but we are 
    # not renamingerinos them becauserino too longerino

    occupado = 0
    
    for direction in neigbourinos:
        yi,xi = direction
        done = False
        while not done:
            if y+yi >= 0 and x+xi >= 0 \
            and y+yi < len(N) \
            and x+xi < len(N[y]):
                if N[y+yi][x+xi] != None:
                    if N[y+yi][x+xi]:
                        occupado += 1
                    done = True

                yi += direction[0]
                xi += direction[1]
            else:
                done = True


    if occupado >= 5 and N[y][x]:
        return False
    elif occupado == 0 and not N[y][x]:
        return True

    return N[y][x]

            


loopin = True
new_g = copy.deepcopy(g)
while loopin:

    for y in range(0, len(g)):
        for x in range(0, len(g[y])):
            new_g[y][x] = flipVisibleShit(y,x,g)
    
    if new_g == g:
        loopin = False

    g = copy.deepcopy(new_g)

counterino = 0
for y in range(0, len(g)):
        for x in range(0, len(g[y])):
            if g[y][x]:
                counterino += 1
print(counterino)