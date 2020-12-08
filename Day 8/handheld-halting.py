import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 8')

def op(inst, sp, acc):
    inst = inst.split(' ')
    if inst[0] == 'nop':
        sp += 1
    elif inst[0] == 'acc':
        acc += int(inst[1])
        sp += 1
    elif inst[0] == 'jmp':
        sp += int(inst[1])
    return sp, acc

def findAccVal(fp='input.txt'):
    prog = open(fp).read().strip('\n').split('\n')
    sp = 0
    acc = 0
    visitedInst = set()
    while sp not in visitedInst:
        visitedInst.add(sp)
        sp, acc = op(prog[sp], sp, acc)
    print(acc)

    for addr in visitedInst:
        tempInst = ''
        if 'nop' in prog[addr]:
            tempInst = prog[addr].replace('nop', 'jmp')
        elif 'jmp' in prog[addr]:
            tempInst = prog[addr].replace('jmp', 'nop')
        sp = 0
        acc = 0
        fixedVisitedInst = set()
        while sp not in fixedVisitedInst and sp < len(prog):
            fixedVisitedInst.add(sp)
            inst = prog[sp]
            if sp == addr:
                inst = tempInst
            sp, acc = op(inst, sp, acc)
        if sp not in fixedVisitedInst:
            return acc
    return None
