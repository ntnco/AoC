from aoc_2020 import get_input
import re

inp = get_input(4).split('\n\n')
res = 0

byr = re.compile("^\d{4}$")
hgt_cm = re.compile("^\d{3}cm$")
hgt_in = re.compile("^\d{2}in$")
hcl = re.compile("^#[a-f0-9]{6}$")
pid = re.compile("^\d{9}$")

def check_line(line_fields):
    req = set(["ecl", "eyr", "hcl", "byr", "iyr", "hgt", "pid"])
    for lf in line_fields:
        key, val = lf.split(":")
        if key in req:
            ok = False
            if key == "byr":
                ok = byr.match(val) and 1920 <= int(val) <= 2002
            elif key == "iyr":
                ok = byr.match(val) and 2010 <= int(val) <= 2020
            elif key == "eyr":
                ok = byr.match(val) and 2020 <= int(val) <= 2030
            elif key == "hgt":
                ok = hgt_cm.match(val) and 150 <= int(val[:3]) <= 193 or\
                hgt_in.match(val) and 59 <= int(val[:2]) <= 76
            elif key == "hcl":
                ok = hcl.match(val)
            elif key == "pid":
                ok = pid.match(val)
            elif key == "ecl":
                ok = val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if ok:
                req.remove(key)
            if len(req) == 0:
                return True
    return False 

for line in inp:
    fields = re.split('\s', line)
    res += check_line(fields)
print(res)

### def check_line(line_fields):
###     req = set(["ecl", "eyr", "hcl", "byr", "iyr", "hgt"])
###     for lf in line_fields:
###         key = lf.split(":")[0]
###         if key in req:
###             req.remove(key)
###             if len(req) == 0:
###                 return True
###     return False
### 
### 
### 
### for line in inp:
###     line = " ".join(line.split('\n'))
###     print(line + "   !!!")
### 
###     fields = line.split(" ")
### 
###     res += check_line(fields)
### 
### print(res)
### 
### print(len(inp))
