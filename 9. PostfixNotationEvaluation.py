'''
후위 표기 수식 계산

 - 수식을 왼쪽부터 차례로 읽음
 - 피연산자가 나타나면 스택에 push
 - 연산자가 나타나면 스택에 들어있는 피연산자를 두개 pop후 연산을 적용, 
   그 결과를 다시 스택에 넣음
'''

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            
            valProcessing == False
            tokens.append(c)
    
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*':3,
        '/':3,
        '+':2,
        '-':2,
        '(':1
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)

        elif token == '(':
            opStack.push(token)

        elif token == ')':
            while opStack.peek != '(':
                postfixList.append(opStack.pop(token))
            opStack.pop()

        else:
            while not opStack.isEmpty():
                if prec[token] > prec[opStack.peek()]:
                    break
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList

def postfixEval(tokenList):
    valStack = ArrayStack()

    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
        
        elif token == '*':
            num1 = valStack.pop()
            num2 = valStack.pop()
            valStack.push(num1*num2)

        elif token == '/':
            num1 = valStack.pop()
            num2 = valStack.pop()
            valStack.push(num2/num1)

        elif token == '+':
            num1 = valStack.pop()
            num2 = valStack.pop()
            valStack.push(num1+num2)
        
        elif token == '-':
            num1 = valStack.pop()
            num2 = valStack.pop()
            valStack.push(num2-num1)

    return valStack.pop()

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val