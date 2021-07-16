# Linked List 
'''
장점
1. 원소를 중간에서 끊어 하나를 삭제하거나 다른 원소를 삽입할 때 선형배열의 경우보다 빠른 시간 내에 처리가 가능
 - 원소의 삽입/삭제가 빈번히 일어나는 응용에서 많이 이용됨

단점
1. 메모리 소요가 큼
2. 특정 웟노 접근까지 시간이 더 오래 걸림

추상적 자료구조 (abstract data structures)
1. Data : 정수, 문자열, 레코드
2. A set of operations : 삽입, 삭제, 순회 / 정렬, 탐색 

Node 내 데이터는 다른 구조로 이루어질 수 있음 ex)문자열, 레코드, 다른 연결리스트 (Data, Link(next))
HEAD -> ...(of nodes : n) -> Tale

class Node:
    def __init__(self, item):
        self.data= = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

연산 정의
1. 특정 원소 참조(k번째)
2. 리스트 순회
3. 길이 얻어내기
4. 원소 삽입
5. 원소 삭제
6. 두 리스트 합치기

head -> 인덱스를 1로 설정, 0은 사용할 때가 있을 경우가 있음

1. 특정 원소 참조
def getAt(self, pos):
    if pos <= 0 or pos > self.nodeCount:
        return None

    i = 1
    curr = self.head
    while i<pos:
        curr = curr.next
        i+=1

배열과 비교한 연결 리스트

                배열                연결 리스트
저장 공간       연속한 위치         임의의 위치
특정 원소 지칭  매우 간편           선형 탐색과 유사
                O(1)                O(n)

2. 리스트 순회 (List Traverse)
Head > next >>>>> Tail

'''

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        l = []
        node = self.head
        while node != None:
            l.append(node.data)
            node = node.next
        return l


# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0