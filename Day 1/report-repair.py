import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 1')

def findProduct(fp='input.txt', target=2020):
    x = []
    with open(fp) as f:
        for line in f:
            line = int(line)
            if line in x:
                return line * (target - line)
            x.append(target - line)

def findThreeProduct(fp='input.txt', target=2020):
    vals = []
    with open(fp) as f:
        for line in f:
            line = int(line)
            vals.append(line)
    for i, x in enumerate(vals):
        for j, y in enumerate(vals):
            for k, z in enumerate(vals):
                if x == y or x == z or y == z:
                    continue
                if x+y+z == target:
                    return x*y*z
