'''
중위 표기법 (infix notation) - 연산자가 피연산자들의 사이에 위치
    ex) (A+B)*(C+D) // A*B+C // A+B*C // A+B+C
후위 표기법 (postfix notation) - 연산자가 피연산자들의 뒤에 위치
    ex) AB+CD+* // AB*C+ // ABC*+ // AB+C+

괄호 처리
여는 괄호는 스택에 push
닫는 괄호를 만나면 여는 괄호가 나올 때까지 pop
연산자를 만났을때 여는 괄호 너머까지 pop하지 않도록
여는 괄호의 우선순위는 가장 낮게 설정

(A+(B-C))*D >> ABC-+D*
A*(B-(C+D)) >> ABCD+-*

알고리즘의 설계
연산자의 우선순위 설정

중위 표현식을 왼쪽부터 한글자씩 읽어
    피연산자이면 그냥 출력
    '('이면 스택에 push
    ')'이면 '('이 나올때까지 스택에서 pop, 출력
    연산자이면 스택에서 이보다 높(거나 같)은 우선순위 것들을 pop, 출력
        그리고 이 연산자는 스택에 push
스택에 남아있는 연산자는 모두 pop, 출력
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

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for c in S:
        if c not in prec and c != ')':
            answer += c
            continue
        if c == '(':
            opStack.push(c)
            continue
        if c in prec:
            while opStack.size() > 0 and prec[opStack.peek()] >= prec[c]:
                answer += opStack.pop()
            opStack.push(c)
            continue
        while opStack.peek() != '(':
            answer += opStack.pop()
        opStack.pop()
    while opStack.isEmpty() == False:
        answer += opStack.pop() 
    return answer


test = '(A+B)*(D+E)'
print(solution(test))
test = 'A*B+C'
print(solution(test))
test = "A+B*C"
print(solution(test))
test = 'A+B+C'
print(solution(test))

