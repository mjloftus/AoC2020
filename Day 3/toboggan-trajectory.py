import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 3')

def slopeCheck(fp='input.txt', dX=3, dY=1):
    chart = []
    with open(fp) as f:
        for line in f:
            chart.append(line.strip('\n'))
    treeCount = 0
    curX = 0
    curY = 0
    while curY < len(chart):
        if chart[curY][curX] == '#':
            treeCount += 1
        curX += dX
        curX %= len(chart[0])
        curY += dY
    print(treeCount)
    return treeCount

def slopeCompile(fp='input.txt', slopes=[(1,1), (3,1), (5,1), (7,1), (1,2)]):
    prod = 1
    for pair in slopes:
        prod *= slopeCheck(fp, pair[0], pair[1])
    return prod
