import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 7')

def constructDict(inp):
    d = {}
    for line in inp:
        key = line.split(' ')[0].strip() + ' ' + line.split(' ')[1].strip()
        if 'no other bags' in line:
            d[key] = []
            continue
        vals = []
        line = line.split(' ')
        ind = 4
        while ind + 1 < len(line):
            vals.append((int(line[ind]), line[ind+1] + ' ' + line[ind+2]))
            ind += 4
        d[key] = vals
    return d

def findContainingBags(fp='input.txt'):
    inp = open(fp).read().strip('\n').split('\n')
    d = constructDict(inp)
    targ = {'shiny gold'}
    repeat = True
    while repeat == True:
        repeat = False
        for key in d:
            if key not in targ and targ.intersection(set(i[1] for i in d[key])):
                targ.add(key)
                repeat = True
    return len(targ) - 1

def findContainedBags(fp='input.txt'):
    inp = open(fp).read().strip('\n').split('\n')
    d = constructDict(inp)
    count = 0
    stack = [(1, 'shiny gold')]
    while len(stack) > 0:
        curKey = stack.pop()
        for val in d[curKey[1]]:
            stack.append((curKey[0]*val[0], val[1]))
            count += curKey[0]*val[0]
    return count
            
