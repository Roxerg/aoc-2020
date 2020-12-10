with open('input10.txt', 'r') as file:
    f = [int(x) for x in file.readlines()]
    f.sort()
    f = [0]+f+[(f[-1]+3)]  


diffs = [1,2,3]
dropping = None


# part 1
c1 = 0
c3 = 0

# idxs for part 2
idxs = [0]

for i in range(0,len(f)-1):
    diff = f[i+1]-f[i]
    if diff in diffs:
        #print("{}-{}={}".format(f[i+1], f[i], diff))
        if diff == 1:
            c1 += 1
        elif diff == 3:
            idxs.append(i)
            c3 += 1
    else:
        print("FUCK")
        
    
print(c1,c3, c1*c3)

# part 2


def get_valids(min_guy, max_guy, valid):

    new_valids = []
    for e in range(0, len(valid)):
        _valid = list(valid)
        _valid.remove(valid[e])
        if len(_valid) > 0:
            if _valid[0]-min_guy <= 3 and max_guy-_valid[-1] <= 3:
                good = True
            
                for i in range(0, len(_valid)-1):
                    if _valid[i+1]-_valid[i] > 3:
                        good = False
                if good:
                    if not _valid in new_valids:
                        new_valids.append(_valid)
        elif max_guy-min_guy <=3 and not _valid in new_valids:
            new_valids.append(_valid)
    
    before_valids = []
    while before_valids != new_valids:
        before_valids = new_valids.copy()
        for nonempty in before_valids:
            if nonempty != []:
                for i in get_valids(min_guy, max_guy, nonempty):
                    if not i in new_valids:
                        new_valids.append(i)

    return new_valids

g = f.copy()
gg = []
for i in range(0, len(idxs)-1):
    sub = g[idxs[i]:idxs[i+1]+1]
    gg.append(sub)


gg = [x for x in gg if len(x)>2]
print(gg[0][1:-1])

perms = 1
itr = 0
print(gg)

print(itr, gg[3], get_valids(gg[3][0], gg[3][-1], gg[3][1:-1]))
for boi in gg:
    print(itr, boi, get_valids(boi[0], boi[-1], boi[1:-1]))
    perms *= len(get_valids(boi[0], boi[-1], boi[1:-1]))+1
    itr += 1

print(perms)