def errorRate(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n\n')
    rules = f[0].split('\n')
    validValues = set()
    for rule in rules:
        rule = rule[rule.index(':')+1:].split(' or ')
        firstRange = rule[0].split('-')
        secondRange = rule[1].split('-')
        for i in range(int(firstRange[0]), int(firstRange[1])+1):
            validValues.add(i)
        for i in range(int(secondRange[0]), int(secondRange[1])+1):
            validValues.add(i)
    nearbyTickets = f[2].split('\n')[1:]
    errorRate = 0
    for ticket in nearbyTickets:
        ticket = ticket.split(',')
        for val in ticket:
            val = int(val)
            if val not in validValues:
                errorRate += val
    return errorRate

def identifyField(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n\n')
    rules = f[0].split('\n')
    validValues = dict()
    globalValidValues = set()
    fieldInds = dict()
    for rule in rules:
        field = rule[0:rule.index(':')]
        rule = rule[rule.index(':')+1:].split(' or ')
        firstRange = rule[0].split('-')
        secondRange = rule[1].split('-')
        vals = set()
        for i in range(int(firstRange[0]), int(firstRange[1])+1):
            vals.add(i)
            globalValidValues.add(i)
        for i in range(int(secondRange[0]), int(secondRange[1])+1):
            vals.add(i)
            globalValidValues.add(i)
        validValues[field] = vals
        fieldInds[field] = -1

    valuesSeenAtInd = dict()
    nearbyTickets = f[2].split('\n')[1:]
    for ticket in nearbyTickets:
        ticket = ticket.split(',')
        valsSeenInTicket = []
        for i, val in enumerate(ticket):
            val = int(val)
            if val not in globalValidValues:
                break
            valsSeenInTicket.append(val)
            if i == len(ticket)-1:
                for j, v in enumerate(valsSeenInTicket):
                    if j not in valuesSeenAtInd.keys():
                        valuesSeenAtInd[j] = set()
                    valuesSeenAtInd[j] = valuesSeenAtInd[j].union({v})

    inds = []
    for i in valuesSeenAtInd.keys():
        inds.append(i)
    while -1 in fieldInds.values():
        validField = -1
        for field in validValues:
            if fieldInds[field] != -1:
                continue
            for ind in inds:
                if valuesSeenAtInd[ind].issubset(validValues[field]):
                    if validField != -1:
                        validField = -1
                        break
                    validField = ind
            fieldInds[field] = validField
            if validField != -1:
                inds.remove(validField)

    myTicket = f[1].split('\n')[1].split(',')
    prod = 1
    for field in fieldInds:
        if 'departure' in field:
            prod *= int(myTicket[fieldInds[field]])

    return prod
