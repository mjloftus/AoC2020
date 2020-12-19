def ruleMatch(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n\n')
    rules = f[0].split('\n')
    message = f[1].split('\n')
    ruledict = dict()
    for rule in rules:
        if '"' in rule:
            rule = rule.split(' ')
            ruledict[rule[0].strip(':')] = list(rule[1].strip('"'))

    count = 0
    while '0' not in ruledict:
        for rule in rules:
            rule = rule.split(':')
            lhand = rule[0]
            rhand = rule[1].strip(' ').split(' | ')
            if lhand in ruledict:
                continue
            allIndices = rule[1].strip(' ').split(' ')
            if '|' in allIndices:
                allIndices.remove('|')
            if not all(elem in ruledict for elem in allIndices):
                continue
            newRule = []
            for rulestring in rhand:
                inds = rulestring.split(' ')
                if len(inds) == 1:
                    for i in ruledict[inds[0]]:
                        newRule.append(i)
                else:
                    for i in ruledict[inds[0]]:
                        for j in ruledict[inds[1]]:
                            newRule.append(i+j)                
            ruledict[lhand] = newRule

    for m in message:
        if m in ruledict['0']:
            count += 1
    return count

import regex as re

def modRuleMatch(fp='input.txt'):
    f = open(fp).read().strip('\n').split('\n\n')
    rules = f[0].split('\n')
    message = f[1].split('\n')
    ruledict = dict()
    for rule in rules:
        if '"' in rule:
            rule = rule.split(' ')
            ruledict[rule[0].strip(':')] = list(rule[1].strip('"'))
            
    while '0' not in ruledict:
        for rule in rules:
            rule = rule.split(':')
            lhand = rule[0]
            rhand = rule[1].strip(' ').split(' | ')
            if lhand in ruledict:
                continue
            allIndices = rule[1].strip(' ').split(' ')
            if '|' in allIndices:
                allIndices.remove('|')
            if not all(elem in ruledict for elem in allIndices):
                continue
            newRule = []
            for rulestring in rhand:
                inds = rulestring.split(' ')
                if len(inds) == 1:
                    for i in ruledict[inds[0]]:
                        newRule.append(i)
                else:
                    for i in ruledict[inds[0]]:
                        for j in ruledict[inds[1]]:
                            newRule.append(i+j)                
            ruledict[lhand] = newRule

    count = 0
    for m in message:
        for i in range(2, 10):
            r = re.match(r"^\L<r8>{" + str(i) + ",}\L<r31>{1," + str((i-1)) + "}$", m, r8=ruledict['8'], r31=ruledict['31'])
            if r:
                count += 1
                break
    return count

print(modRuleMatch())
