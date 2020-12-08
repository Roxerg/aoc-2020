with open('input8.txt', 'r') as file:
    f = file.readlines()

def traverse(com, val, acc, i):
    if com == "acc":
        acc += int(val)
        i += 1
    if com == "nop":
        i += 1
    if com == "jmp":
        i += int(val)
    return acc, i


exec_ids = set([])


# part 1
acc = 0
i = 0
prev_i = 0
while True:
    if i in exec_ids:
        print(acc)
        break

    exec_ids.add(i)
    com, val = f[i].split(" ")
    acc, i = traverse(com,val,acc,i)



# part 2
# fuck it try all of them
iters = 0
for l in range(0,len(f)):
    if "jmp" in f[l] or "nop" in f[l]:
        iters += 1
        g = f.copy()
        if "jmp" in f[l]:
            g[l] = f[l].replace("jmp", "nop") 
        else:
            g[l] = f[l].replace("nop", "jmp")
        
        exec_ids = set([])
        i = 0
        acc = 0
        while True:
            if i in exec_ids:
                break

            exec_ids.add(i)
            com, val = g[i].split(" ")
            acc, i = traverse(com,val,acc,i)
            if i == len(g):
                print(acc)
                break

print(iters)