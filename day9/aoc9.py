with open('input9.txt', 'r') as file:
    f = file.readlines()


preamble_len = 25#25
bad_boi = 0


# part 1
preamble = []
for i in range(0, preamble_len):
    preamble.append(int(f[i]))

for i in range(preamble_len, len(f)):
    num = int(f[i])
    subt = [num-x for x in preamble]
    contains = False
    for e in subt:
        if e in preamble:
            print("{}+{}={}".format(e,preamble,f[i]))
            contains = True
    if not contains:
        bad_boi = int(f[i])
        print(f[i])
        break

    preamble = [int(f[x]) for x in range(i-preamble_len+1, i+1)]


import numpy as np
# part 2
f = [int(x) for x in f]
g = f.copy()
summy = bad_boi-np.array(f)
for i in range(1, len(f)):
    g = [0] + g[0:-1]
    summy = summy - g
    print(summy)
    if 0 in summy:
        bois = []
        print(np.where(summy == 0)[0][0])
        for ii in range(0,i+1):
            bois.append(f[np.where(summy == 0)[0][0]-ii])
        print(bois)
        print("min", min(bois))
        print("max", max(bois))
        print("sum ", max(bois)+min(bois))
        break;
        

