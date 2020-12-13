import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 9')

def firstNumber(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n')
    vals = []
    for i in range(25):
        vals.append(int(f[i]))
    ind = 25
    while True:
        cVal = int(f[ind])
        for val in vals:
            if cVal - val != val and cVal - val in vals:
                vals.remove(vals[0])
                vals.append(cVal)
                ind += 1
                break
        if cVal not in vals:
            return cVal
    return None

def findSum(fp='input.txt'):
    target = firstNumber(fp)
    f = open(fp).read().strip('\n').split('\n')
    ind = f.index(str(target)) - 1
    for startInd in range(ind, -1, -1):
        curSum = []
        curInd = startInd
        while sum(curSum) + int(f[curInd]) <= target:
            curSum.append(int(f[curInd]))
            curInd -= 1                                    
        if sum(curSum) == target:
            return max(curSum) + min(curSum)
    return None
