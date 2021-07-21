# Stacks
'''
data element를 보관할 수 있는 선형구조
단 넣을때는 한쪽 끝에서 밀어넣어야하고(push 연산) 꺼낼 때는 같은 족에서 뽑아 꺼내야함(pop연산)
후입선출(LIFO)의 특징

스택에서 발생하는 오류
1. 비어있는 스택에서 데이터 원소를 꺼내려 할 때
2. 꽉 찬 스택에 데이터 원소를 넣으려 할 때 (stack overflow)

(1) 배열을 이용해 구현
    - python 리스트와 메서드를 이용
(2) 연결 리스트를 이용하여 구현
    - 양방향 연결리스트 이용 가정

연산의 정의
    - size() - 현재 스택에 들어있는 데이터 원소 수를 구함
    - isEmpty() - 현재 스택이 비어있는지 판단
    - push(x) - 데이터 원소 x를 스택에 추가
    - pop() - 스택의 맨 위에 저장된 데이터 원소를 제거(, 반환)
    - peek() - 스택의 맨 위에 저장된 데이터 원소를 반환 (제거하지 않음)

연습문제
괄호의 유효성 검사
- 여는 괄호를 만나면 스택에 푸시
- 닫는 괄호를 만나면 : 
    1) 스택이 비어있으면 올바르지 않은 수식
    2) 스택에서pop, 쌍을 이루는 여는 괄호인지 검사
- 끌까지 검사 후 스택이 비어있어야 올바른 수식
'''
from doublylinkedlist import Node
from doublylinkedlist import DoublyLinkedList


class ArrayStack:

	def __init__(self):
		self.data = []

	def size(self): # 스택의 크기
		return len(self.data)

	def isEmpty(self): # 스택이 비어있는지 판단
		return self.size() == 0

	def push(self, item): # 데이터 원소를 추가
		self.data.append(item)

	def pop(self): # 데이터 원소를 삭제(리턴)
		return self.data.pop()

	def peek(self): # 데이터 원소를 반환 (삭제 X)
		return self.data[-1]


class LinkedListStack:

	def __init__(self):
		self.data = DoublyLinkedList()

	def size(self):
		return self.data.getLength()

	def isEmpty(self):
		return self.size() == 0

	def push(self, item):
		node = Node(item)
		self.data.insertAt(self.size() + 1, node)

	def pop(self):
		return self.data.popAt(self.size())

	def peek(self):
		return self.data.getAt(self.size()).data


def bracketTest(expr):
    match = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c)
        elif c in match:
            if S.isEmpty():
                return False
            else:
                t = S.pop()
                if t!=match[c]:
                    return False
    return S.isEmpty()