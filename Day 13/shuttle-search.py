import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 13')

def findEarliestBus(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n')
    earliestTime = int(f[0])
    busIds = f[1].split(',')
    while 'x' in busIds:
        busIds.remove('x')
    minId = 0
    minWait = -1
    for i in busIds:
        if i != 'x':
            busId = int(i)
            wait = (int(earliestTime / busId) + 1) * busId - earliestTime
            if wait < minWait or minWait == -1:
                minWait = wait
                minId = busId
    return minWait * minId

def CRT(b, mod):
    N = 1
    for i in mod:
        N *= i
    Ni = []
    for i in mod:
        Ni.append(N // i)
    xi = []
    for i in range(len(mod)):
        m = mod[i]
        n = Ni[i]
        t = -(n % m) + m
        x = 1
        while (t * x) % m != 1:
            x += 1
        xi.append(x)
    bnx = []
    for i in range(len(b)):
        bnx.append(b[i] * Ni[i] * xi[i])
    return sum(bnx) % N
    
def findEarliestSync(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n')
    busIds = f[1].split(',')
    b = []
    mod = []
    for i, v in enumerate(busIds):
        if v != 'x':
            b.append(i)
            mod.append(int(v))
    return CRT(b, mod)
