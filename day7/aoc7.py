with open('input7.txt', 'r') as file:
    f = file.readlines()


# part 1

# get first bags
shiny = "shiny gold"
bags = set([])
for rule in f:
    if shiny in rule and shiny != rule[0:len(shiny)]:
        bags.add(rule.split(" bags ")[0])

bags_before = None
while bags_before != bags:
    bags_before = set(bags)
    bags_new = set(bags)
    for rule in f:
        for bag in bags:
            if bag in rule and bag != rule[0:len(bag)]:
                bags_new.add(rule.split(" bags ")[0])
    bags = set(bags_new)

print(len(bags))

# part 2


def get_count(bag):

    rule = None
    for r in f:
        if bag == r[0:len(bag)]:
            rule = r
    
    if rule == None:
        return 0

    rule_lst = rule.replace(",", "").replace(".", "").split(" ")
    
    summo = 0
    for e in range(0,len(rule_lst)):
        if rule_lst[e].isdigit():
            summo += int(rule_lst[e]) + int(rule_lst[e])*get_count(rule_lst[e+1] + " " + rule_lst[e+2])
    
    return summo

print(get_count(shiny))
