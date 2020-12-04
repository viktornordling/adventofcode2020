from math import prod
import re

def hgt_valid(hgt):
    if "cm" in hgt:
        part = int(hgt.split("cm")[0])
        return part >= 150 and part <= 193
    elif "in" in hgt:
        part = int(hgt.split("in")[0])
        return part >= 59 and part <= 76

def hair_valid(hcl):
    hair_valid = re.search("^#([\da-f]){6}$", hcl)
    return hair_valid is not None

def ecl_valid(ecl):
    parts = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    g = ecl in parts
    return ecl in parts

def pid_valid(pid):
    ff = re.search("^\d{9}$", pid) is not None
    return ff

def is_valid_1(passport):
    nparts = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    parts = passport.split(" ")
    key_values = { key.split(":")[0]:key.split(":")[1] for key in parts if key.split(":")[0] != "cid" }
    keys = set([key.split(":")[0] for key in parts if key.split(":")[0] != "cid"])
    return keys == nparts


def is_valid_2(passport):
    nparts = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    parts = passport.split(" ")
    key_values = { key.split(":")[0]:key.split(":")[1] for key in parts if key.split(":")[0] != "cid" }
    keys = set([key.split(":")[0] for key in parts if key.split(":")[0] != "cid"])
    if keys != nparts:
        return False
    byr = int(key_values["byr"])
    iyr = int(key_values["iyr"])
    eyr = int(key_values["eyr"])
    hgt = key_values["hgt"]
    hcl = key_values["hcl"]
    ecl = key_values["ecl"]
    pid = key_values["pid"]
    if (byr < 1920 or byr > 2002):
        return False
    elif not (iyr >= 2010 and iyr <= 2020):
        return False
    elif not (eyr >= 2020 and eyr <= 2030):
        return False
    elif not hgt_valid(hgt):
        return False
    elif not hair_valid(hcl):
        return False
    elif not ecl_valid(ecl):
        return False
    elif not pid_valid(pid):
        return False
    return True


def count_valid_passports_1(lines):
    passports = []
    cur_pass = []

    for line in lines:
        if line.strip() != "":
            cur_pass.append(line.strip())
        else:
            passports.append(" ".join(cur_pass))
            cur_pass = []
    valids = 0
    for p in passports:
        if is_valid_1(p):
            valids += 1
    return valids

def count_valid_passports_2(lines):
    passports = []
    cur_pass = []

    for line in lines:
        if line.strip() != "":
            cur_pass.append(line.strip())
        else:
            passports.append(" ".join(cur_pass))
            cur_pass = []
    valids = 0
    for p in passports:
        if is_valid_2(p):
            valids += 1
    return valids


    # lines = open('easy.txt', 'r').readlines()
lines = open('input.txt', 'r').readlines()

print("Part 1:", count_valid_passports_1(lines))
print("Part 2:", count_valid_passports_2(lines))
