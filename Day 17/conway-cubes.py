def sixCycle(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n')
    state = dict()
    for y, row in enumerate(f):
        for x, initState in enumerate(row):
            if initState == '.':
                state[(x,y,0)] = '.'
            elif initState == '#':
                state[(x,y,0)] = '#'

    for cycle in range(6):
        activeNeighborCount = dict()
        for key in state:
            neighbors = set()
            if state[key] != '#':
                continue
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    for dz in range(-1, 2):
                        if dx == dy == dz == 0:
                            continue
                        neighbors.add((key[0]+dx, key[1]+dy, key[2]+dz))
            for neighbor in neighbors:
                if neighbor not in activeNeighborCount:
                    activeNeighborCount[neighbor] = 1
                else:
                    activeNeighborCount[neighbor] += 1
        newState = dict()
        for cell in activeNeighborCount:
            if activeNeighborCount[cell] == 3:
                newState[cell] = '#'
            elif activeNeighborCount[cell] == 2 and cell in state and state[cell] == '#':
                newState[cell] = '#'
        state = newState

    return len(state)

def fourDim(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n')
    state = dict()
    for y, row in enumerate(f):
        for x, initState in enumerate(row):
            if initState == '#':
                state[(x,y,0,0)] = '#'

    for cycle in range(6):
        activeNeighborCount = dict()
        for key in state:
            neighbors = set()
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    for dz in range(-1, 2):
                        for dw in range(-1, 2):
                            if dx == dy == dz == dw == 0:
                                continue
                            neighbors.add((key[0]+dx, key[1]+dy, key[2]+dz, key[3]+dw))
            for neighbor in neighbors:
                if neighbor not in activeNeighborCount:
                    activeNeighborCount[neighbor] = 1
                else:
                    activeNeighborCount[neighbor] += 1
        newState = dict()
        for cell in activeNeighborCount:
            if activeNeighborCount[cell] == 3:
                newState[cell] = '#'
            elif activeNeighborCount[cell] == 2 and cell in state and state[cell] == '#':
                newState[cell] = '#'
        state = newState

    return len(state)
