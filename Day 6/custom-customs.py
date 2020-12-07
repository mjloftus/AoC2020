import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 6')

def findYesCountAny(fp='input.txt'):
    count = 0
    with open(fp) as f:
        i = f.read().split('\n\n')
        for line in i:
            line.strip('\n')
            a = set()
            for c in line:
                a.add(c)
            if '\n' in a:
                a.remove('\n')
            count += len(a)
    return count

def findYesCountAll(fp='input.txt'):
    count = 0
    with open(fp) as f:
        groups = f.read().split('\n\n')
        for group in groups:
            group = group.strip('\n')
            groupAns = []
            group = group.split('\n')
            for ind in group:
                ans = set()
                for a in ind:
                    ans.add(a)
                groupAns.append(ans)
            allAns = groupAns[0]
            for indAns in groupAns[1:]:
                allAns = allAns.intersection(indAns)
            if '\n' in allAns:
                allAns.remove('\n')
            count += len(allAns)
    return count
