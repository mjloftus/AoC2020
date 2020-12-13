import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 10')

def findDiff(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n')
    vals = [0]
    for v in f:
        vals.append(int(v))
    vals.sort()
    vals.append(vals[len(vals)-1]+3)
    diff1 = 0
    diff3 = 0
    for i, v in enumerate(vals[:len(vals)-1]):
        if vals[i+1] - v == 1:
            diff1 += 1
        elif vals[i+1] - v == 3:
            diff3 += 1
    return diff1 * diff3
                          
def countArrangements(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n')
    vals = [0]
    sums = [1]
    for v in f:
        vals.append(int(v))
    vals.append(max(vals)+3)
    vals.sort()
    curInd = 1
    while curInd < len(vals):
        if curInd - 3 >= 0 and vals[curInd] - vals[curInd-3] <= 3:
            sums.append(sums[curInd-3] + sums[curInd-2] + sums[curInd-1])
        elif curInd - 2 >= 0 and vals[curInd] - vals[curInd-2] <= 3:
            sums.append(sums[curInd-2] + sums[curInd-1])
        else:
            sums.append(sums[curInd-1])
        curInd += 1
    return sums[len(sums)-1]
