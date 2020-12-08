from functools import reduce

with open('input6.txt', 'r') as file:
    f = file.read().replace('\n\n', '+')
    f = f.replace('\n', ' ')

# part 1
_sum = sum(map(lambda x: len(set(x)), f.replace(' ', '').split('+')))

print(_sum)

# part 2
charset = set("abcdefghijklmnopqrstuvwxyz")

_sum = sum(map(lambda grp: len(reduce(lambda x,y: x-set(y), map(lambda z: charset-set(z), grp.split(' ')), charset)), f.split('+'))) 
print(_sum)