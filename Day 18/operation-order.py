def mathSum(fp='input.txt'):
    f = open(fp).read().strip('\n').replace('(', '( ').replace(')', ' )').split('\n')
    res = []
    for eq in f:
        stack = []
        eq = eq.split(' ')
        curToken = 0
        while eq[curToken] == '(':
            stack.append('(')
            curToken+=1
        stack.append(int(eq[curToken]))
        curToken += 1
        while curToken < len(eq):
            print(stack)
            curVal = int(stack.pop())
            if eq[curToken] == '+' or eq[curToken] == '*':
                if eq[curToken+1].isnumeric():
                    curVal = eval(str(curVal) + eq[curToken] + eq[curToken+1])
                    stack.append(curVal)
                    curToken += 2
                else:
                    if eq[curToken+1] == '(': #begin parentheses
                        stack.append(curVal)
                        stack.append(eq[curToken])
                        stack.append(eq[curToken+1])
                        curToken += 2
                        while eq[curToken] == '(':
                            stack.append('(')
                            curToken += 1
                        stack.append(eq[curToken])
                        curToken += 1
                        print('(', stack)
            elif eq[curToken] == ')': #end parentheses
                parenVal = curVal
                #parenVal = eval(parenVal + eq[curToken] + str(curVal))
                ##
                if len(stack) < 2:
                    stack.pop()
                    stack.append(curVal)
                    curToken += 1
                    continue
                ##
                backTok = stack.pop()
                backVal = stack.pop()
                while backTok != '(':
                    parenVal = eval(str(parenVal) + backTok + str(backVal))
                    backTok = stack.pop()
                    backVal = stack.pop()
                if backVal == '(':
                    stack.append(backVal)
                else:
                    curVal = int(stack.pop())
                    curVal = eval(str(curVal) + str(backVal) + str(parenVal))
                    #stack.append(backVal)
                    #stack.append(parenVal)
                stack.append(curVal)
                curToken += 1
        res.append(stack[0])
    return sum(res)

def mathSumWithPrec(fp='input.txt'):
    f = open(fp).read().strip('\n').replace('(', '( ( ').replace(')', ' ) )').replace('*', ') * (').split('\n')
    res = []
    for eq in f:
        stack = []
        eq = '( ' + eq + ' )'
        eq = eq.split(' ')
        curToken = 0
        while eq[curToken] == '(':
            stack.append('(')
            curToken+=1
        stack.append(int(eq[curToken]))
        curToken += 1
        while curToken < len(eq):
            curVal = int(stack.pop())
            if eq[curToken] == '+' or eq[curToken] == '*':
                if eq[curToken+1].isnumeric():
                    curVal = eval(str(curVal) + eq[curToken] + eq[curToken+1])
                    stack.append(curVal)
                    curToken += 2
                else:
                    if eq[curToken+1] == '(': #begin parentheses
                        stack.append(curVal)
                        stack.append(eq[curToken])
                        stack.append(eq[curToken+1])
                        curToken += 2
                        while eq[curToken] == '(':
                            stack.append('(')
                            curToken += 1
                        stack.append(eq[curToken])
                        curToken += 1
            elif eq[curToken] == ')': #end parentheses
                parenVal = curVal
                if len(stack) < 1:
                    stack.append(curVal)
                    curToken += 1
                    continue
                if len(stack) < 2:
                    stack.pop()
                    stack.append(curVal)
                    curToken += 1
                    continue
                backTok = stack.pop()
                backVal = stack.pop()
                while backTok != '(':
                    parenVal = eval(str(parenVal) + backTok + str(backVal))
                    backTok = stack.pop()
                    backVal = stack.pop()
                if backVal == '(':
                    stack.append(backVal)
                else:
                    curVal = int(stack.pop())
                    curVal = eval(str(curVal) + str(backVal) + str(parenVal))
                stack.append(curVal)
                curToken += 1
        res.append(stack[0])
    return sum(res)
