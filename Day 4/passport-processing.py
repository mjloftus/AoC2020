import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 4')

import re

def validateData(passport):
    try:
        if int(passport['byr']) not in range(1920, 2003):
            return False
        if int(passport['iyr']) not in range(2010, 2021):
            return False
        if int(passport['eyr']) not in range(2020, 2031):
            return False
        if 'cm' in passport['hgt']:
            if int(passport['hgt'].split('cm')[0]) not in range(150, 194):
                return False
        elif 'in' in passport['hgt']:
            if int(passport['hgt'].split('in')[0]) not in range(59, 77):
                return False
        else:
            return False
        if re.compile('^#[a-f0-9]{6}$').fullmatch(passport['hcl']) == None:
            return False
        if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        if re.compile('^[0-9]{9}$').fullmatch(passport['pid']) == None:
            return False
        return True
    except:
        return False

def countValidPassports(fp='input.txt'):
    reqFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optFields = ['cid']
    validFields = 0
    validPassports = 0
    with open(fp) as f:
        p = f.read().rstrip().split('\n\n')
        for line in p:
            passport = {}
            fields = line.replace('\n', ' ').rstrip('').split(' ')
            for field in fields:
                passport[field.split(':')[0]] = field.split(':')[1]
            if set(reqFields).difference(passport.keys()).issubset(optFields):
                validFields += 1
                if validateData(passport) == True:
                    validPassports += 1
    return validFields, validPassports
