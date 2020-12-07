import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 2')

def passwordCheck(fp='input.txt'):
    valid = 0
    with open(fp) as f:
        for line in f:
            s = line.split()
            v = s[0].split('-')
            targMin = int(v[0])
            targMax = int(v[1])
            target = s[1].strip(':')
            count = s[2].count(target)
            if count >= targMin and count <= targMax:
                valid += 1
    return valid

def newPasswordCheck(fp='input.txt'):
    valid = 0
    with open(fp) as f:
        for line in f:
            s = line.split()
            v = s[0].split('-')
            low = int(v[0])
            high = int(v[1])
            target = s[1].strip(':')
            if (s[2][low-1] == target) != (s[2][high-1] == target):
                valid += 1
    return valid
