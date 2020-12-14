
from itertools import permutations, product as iterproduct
from time import time


completestart = time()

with open('input14.txt', 'r') as file:
    f = file.readlines()





# commands consist of idx and val
# commands are grouped into bitmasks.
# { {"bitmask"   
#   [ ("idx", "val") ] }
commands = [

]

for i in range(0, len(f)):
    line = f[i]
    if "mask" in line:
        coms = []
        i += 1
        cur_mask = line.replace("mask = ", "")[:-1]
        line = f[i]
        while i < len(f):
            line = f[i]
            if "mask" in line:
                break
            idx, val = line.split(" = ")
            val = val.replace("\n", "")
            idx = idx.replace("mem[", "").replace("]", "")
            coms.append((int(idx), int(val)))
            i += 1
        
        commands.append({
            "mask_xs"   : int(cur_mask.replace("1", "0").replace("X", "1"),2),
            "mask_one"  : int(cur_mask.replace("X", "0").encode("ascii"),2),
            "mask_zero" : int(cur_mask.replace("1", "X").replace("0", "1").replace("X","0"),2),
            "coms" : coms
        })
            

start1 = time()
# part 1
mem = {}

for boi in commands:
    mask_one = boi["mask_one"]
    mask_zero = boi["mask_zero"]

    coms = boi["coms"]
    for com in coms:  
         mem[com[0]] = (com[1] & ~(com[1] & int(mask_zero))  | int(mask_one))
         #print(bin(com[1]))


res = 0
for i, v in mem.items():
    res += v

print(res)

print("------")

def bits(n):
    while n:
        b = n & (~n+1)
        yield b
        n ^= b

# part 2

mem2_electric_boogalooo = {}

#print(commands)

end1 = time()


start2 = time()

for boi in commands:

    mask_one = boi["mask_one"]
    mask_zero = boi["mask_zero"]    
    mask_xs = boi["mask_xs"]

    xs_count = len([x for x in bin(mask_xs) if x == "1"])

    itrboi = bin(mask_xs)[2:][::-1]
    zros = ""

    mults = []

    for i in itrboi:
        if i == "1":
            mults.append(int(("1"+zros).encode("ascii"),2))
        zros += "0"

    arrs = [[int(x) for x in seq] for seq in iterproduct("01", repeat=xs_count)]


    ones_lads = []
    zeros_lads = []
    for arr in arrs:
        ones_lad = 0
        zeros_lad = 0

        for k in range(0, len(arr)):
            if arr[k] == 0:
                zeros_lad += mults[k]
            else:
                ones_lad += mults[k] 

        ones_lads.append(ones_lad)
        zeros_lads.append(zeros_lad)

    #print("mults", mults)
    lads = [([x*y for x,y in zip(arr,mults)]) for arr in arrs]   
    lads = [sum(x) for x in lads]
    
    coms = boi["coms"]
    for com in coms:
        yeeter = com[0] | int(mask_one)
        
        for l in range(0, len(ones_lads)):
            
            ones_lad = ones_lads[l]
            zeros_lad = zeros_lads[l]


            #idx = (yeeter | lad) & ~lad 
            idx = (yeeter & ~(yeeter & zeros_lad)) | ones_lad
            # (com[1] & ~(com[1] & int(mask_zero))  | int(mask_one))
            
            mem2_electric_boogalooo[idx] = com[1]


end2 = time()
print(sum(mem2_electric_boogalooo.values()))

print("part 1 elapsed: ", end1-start1)
print("part 2 elapsed: ", end2-start2)
print("total w/ file reading: ", end2-completestart)