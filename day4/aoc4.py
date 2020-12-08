


th = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]



def valid_check(s): 

    things = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

    for t in things:
        if t not in s:
            return False
    
    s = s.replace("\n", " ")
    s = s.split(" ")

    s = [a for a in s if a != ""]

    err = ""
    
   
    n = 0
    for a in s: 
        try:
            fld, val = a.split(":")    
        except ValueError:
            #print("AAAA" + a + "AAA")
            #print(a)
            if (a != " "):
                pass #print(a)
            pass
  
        if fld == "byr":
            try:
                int(val)
            except ValueError:
                err = "byr"
                # return False
            if int(val) <= 2002 and int(val) >= 1920:
                pass
            else:
                #pass
                err = "byr" #return False
        elif fld == "iyr":
            try:
                int(val)
            except ValueError:
                #return False
                err = "iyr"
            if int(val) <= 2020 and int(val) >= 2010:
                pass
            else:
                err = "iyr"
                #return False
        elif fld == "eyr":
            try:
                int(val)
            except ValueError:
                err = "eyr_i"
                #return False
            if int(val) <= 2030 and int(val) >= 2020:
                pass
            else:
                err = "eyr"
                #return False
        elif fld == "hgt":

            __val = val
            val_l = len(val)
            val = val.replace("cm", "")
            is_cm = val_l != len(val)
            val = val.replace("in", "")

                

            try:
                int(val)
            except ValueError:
                err = "hgt_f"
                # return False
            if is_cm and int(val) <= 193 and int(val) >= 150:
                pass
            elif not is_cm and int(val) <= 76 and int(val) >= 59:
                pass
            else:
                err = "hgt"
                #return False
            
        elif fld == "hcl":
            if val[0] == "#" and len(val) == 7:
                pass
            else:
                err = "hcl0"
                #return False

            for i in range(1, len(val)):
                if val[i] in "0123456789" or val[i] in "abcdef":
                    pass
                else:
                    err = "hcl"
                    #return False
        elif fld == "ecl":
            if len(val) != 3:
                err = "ecl"
            if val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                pass
            else:
                err = "ecl"
                #return False
        elif fld == "pid":
            if len(val) == 9:
                pass
            else:
                err = "pid"
            for x in val:
                if x in "0123456789":
                    pass
                else:
                    err = "pid"
                    #return False
        elif fld == "cid":
            pass       
        n += 1

    #print(s)
    if err != "":
        #print(err)
        return False
    print("passed: ", s)
    return True




f = None
with open("input3.txt") as fl:
    f = fl.readlines()



passports = []
i = 0
while i < len(f):

    passport = ""
    while i < len(f):
        if f[i] == "\n":
            break
        passport += f[i]
        i += 1
    i += 1
    passports.append(passport)



things = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
c = 0
for passport in passports:
    valid = True
    for t in things:
        if t not in passport:
            valid = False
            break
    if valid:
        c += 1

print(c)

c = 0
for passport in passports:
    valid = True

    valid = valid_check(passport)

    if valid:
        c += 1

print(c)

