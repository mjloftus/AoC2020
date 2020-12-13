import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 11')

def part1(fp='input.txt'):    
    layout = open(fp).read().strip('\n').split('\n')
    for i in range(len(layout)):
        layout[i] = [char for char in layout[i]]
    
    change = True
    while change == True:
        changelog = []
        for i in range(len(layout)):
            changelog.append([0]*len(layout[0]))
        for rownum, row in enumerate(layout):
            for seatnum, seat in enumerate(row):
                if layout[rownum][seatnum] != '#':
                    continue
                if seatnum > 0:
                    changelog[rownum][seatnum-1] += 1
                if rownum > 0:
                    changelog[rownum-1][seatnum] += 1
                if seatnum < len(layout[0])-1:
                    changelog[rownum][seatnum+1] += 1
                if rownum < len(layout)-1:
                    changelog[rownum+1][seatnum] += 1
                if seatnum > 0 and rownum > 0:
                    changelog[rownum-1][seatnum-1] += 1
                if seatnum > 0 and rownum < len(layout)-1:
                    changelog[rownum+1][seatnum-1] += 1
                if seatnum < len(layout[0])-1 and rownum > 0:
                    changelog[rownum-1][seatnum+1] += 1
                if seatnum < len(layout[0])-1 and rownum < len(layout)-1:
                    changelog[rownum+1][seatnum+1] += 1
        change = False
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if layout[i][j] == 'L' and changelog[i][j] == 0:
                    layout[i][j] = '#'
                    change = True
                elif layout[i][j] == '#' and changelog[i][j] >= 4:
                    layout[i][j] = 'L'
                    change = True
    count = 0
    for row in layout:
        count += row.count('#')
    return count

def part2(fp='input.txt'):    
    layout = open(fp).read().strip('\n').split('\n')
    for i in range(len(layout)):
        layout[i] = [char for char in layout[i]]
    
    change = True
    while change == True:
        changelog = []
        for i in range(len(layout)):
            changelog.append([0]*len(layout[0]))
        for rownum, row in enumerate(layout):
            for seatnum, seat in enumerate(row):
                if layout[rownum][seatnum] != '#':
                    continue
                if seatnum > 0:
                    r = rownum
                    s = seatnum-1
                    while layout[r][s] == '.' and s > 0:
                        s -= 1
                    changelog[r][s] += 1
                if rownum > 0:
                    r = rownum-1
                    s = seatnum
                    while layout[r][s] == '.' and r > 0:
                        r -= 1
                    changelog[r][s] += 1
                if seatnum < len(layout[0])-1:
                    r = rownum
                    s = seatnum+1
                    while layout[r][s] == '.' and s < len(layout[0])-1:
                        s += 1
                    changelog[r][s] += 1
                if rownum < len(layout)-1:
                    r = rownum+1
                    s = seatnum
                    while layout[r][s] == '.' and r < len(layout)-1:
                        r += 1
                    changelog[r][s] += 1
                if seatnum > 0 and rownum > 0:
                    r = rownum-1
                    s = seatnum-1
                    while layout[r][s] == '.' and s > 0 and r > 0:
                        r -= 1
                        s -= 1
                    changelog[r][s] += 1
                if seatnum > 0 and rownum < len(layout)-1:
                    r = rownum+1
                    s = seatnum-1
                    while layout[r][s] == '.' and s > 0 and r < len(layout)-1:
                        r += 1
                        s -= 1
                    changelog[r][s] += 1
                if seatnum < len(layout[0])-1 and rownum > 0:
                    r = rownum-1
                    s = seatnum+1
                    while layout[r][s] == '.' and s < len(layout[0])-1 and r > 0:
                        r -= 1
                        s += 1
                    changelog[r][s] += 1
                if seatnum < len(layout[0])-1 and rownum < len(layout)-1:
                    r = rownum+1
                    s = seatnum+1
                    while layout[r][s] == '.' and s < len(layout[0])-1 and r < len(layout)-1:
                        r += 1
                        s += 1
                    changelog[r][s] += 1
        change = False
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if layout[i][j] == 'L' and changelog[i][j] == 0:
                    layout[i][j] = '#'
                    change = True
                elif layout[i][j] == '#' and changelog[i][j] >= 5:
                    layout[i][j] = 'L'
                    change = True
    count = 0
    for row in layout:
        count += row.count('#')
    return count               
