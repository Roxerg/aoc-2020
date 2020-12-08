





f = None
with open("input.txt") as fl:
    f = fl.readlines()



## Part 1
count = 0
for fl in f:
    rule, l, pwd = fl.split(" ")
    min_l, max_l = rule.split("-")

    l, _ = l.split(":")

    min_l, max_l = int(min_l), int(max_l)

    if len(pwd) < min_l:
        print("pass")
        continue

    cnt = pwd.count(l)

    if cnt >= min_l and cnt <= max_l:
        count += 1

print(count)

## Part 2

count = 0
for fl in f:
    rule, l, pwd = fl.split(" ")
    min_l, max_l = rule.split("-")

    l, _ = l.split(":")

    min_l, max_l = int(min_l), int(max_l)

    if len(pwd) < min_l:
        print("pass")
        continue

    char1 = pwd[min_l-1]
    char2 = pwd[max_l-1]

    if (char1 == l) != (char2 == l):
        count += 1

print(count)