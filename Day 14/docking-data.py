import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 14')

def valueDecode(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n')
    mask = 2**35
    mem = dict()
    for i in f:
        if 'mask' in i:
            mask = i.split(' ')[2]
        elif 'mem' in i:
            s = i.split(' ')
            addr = int(s[0].lstrip('mem[').rstrip(']'))
            val = bin(int(s[2])).lstrip('0b').zfill(36)
            maskedVal = ''
            for j in range(len(val)):
                if mask[j] == 'X':
                    maskedVal += val[j]
                if mask[j] == '1':
                    maskedVal += '1'
                if mask[j] == '0':
                    maskedVal += '0'
            mem[addr] = int(maskedVal, 2)
    return sum(mem.values())

def addressDecode(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n')
    mask = 2**35
    mem = dict()
    for i in f:
        if 'mask' in i:
            mask = i.split(' ')[2]
        elif 'mem' in i:
            s = i.split(' ')
            baseAddr = bin(int(s[0].lstrip('mem[').rstrip(']'))).lstrip('0b').zfill(36)
            val = int(s[2])
            addrs = ['']
            ind = 0
            while ind < len(mask):
                newAddrs = []
                for addr in addrs:
                    if mask[ind] == 'X':
                        newAddrs.append(addr+'0')
                        newAddrs.append(addr+'1')
                    elif mask[ind] == '0':
                        newAddrs.append(addr+baseAddr[ind])
                    elif mask[ind] == '1':
                        newAddrs.append(addr+'1')
                ind += 1
                addrs = newAddrs
            for addr in addrs:
                addr = int(addr, 2)
                mem[addr] = val
    return sum(mem.values())
