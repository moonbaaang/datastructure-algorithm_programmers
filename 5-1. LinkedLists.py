class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount

'''
연결리스트 원소 삽입의 복잡도
맨앞 삽입 : O(1)
중간 삽입 : O(n)
맨끝 삽입 : O(1)

# 연결리스트 연산 - 원소 삭제
def popAt(self, pos):

> pos가 가리키는 위치 (1<=pos<=nodeCount)
> node 삭제 , node의 데이터를 리턴

r = L.popAt(pos)

pos-1 > pos > pos+1

prev =  pos-1
curr = pos
prev.next > curr.next 로 변경
curr의 데이터 r 리턴
nodeCount -= 1

주의사항 
(1) 삭제하려는 node가 맨 앞일 경우
    > prev 없음, HEAD 조정 필요
(2) 맨 끝의 node 삭제
    > Tail 조정 필요
(3) 유일한 노드 삭제
    > 이 두 조건에 의해 처리되지 않는지?
(4) 삭제하려는 node가 마지막 node일 때
    > pos == nodeCount 인 경우?
    > tail로 prev값을 찾을 수 없음
    > tail 직전의 pos-1번째 node를 찾아야함

연결리스트 원소 삭제의 복잡도
맨앞 삭제 : O(1)
중간 삭제 : O(n)
맨끝 삭제 : O(n)


# 두 리스트의 연결
def concat(self, L):
    self.tail.next = L.head
    if L.tail:
        self.tail = L.tail
    celf.nodeCount += L.nodeCount

L1.concat(L2)
(L1) self.tail.next = L2.head
self.tail = L2.tail
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


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        if pos<1 or pos> self.nodeCount:
            raise IndexError
        
        if self.nodeCount == 1:
            result = self.head
            self.head = None
            self.tail = None
            
        else:
            if self.nodeCount == pos:
                result = self.head
                prev = self.getAt(pos-1)
                prev.tail = None
            else: 
                result = self.head
                prev = self.getAt(pos-1)
                curr = self.getAt(pos)
                prev.next = curr.next
            return result


    def popAt(self, pos):

        if pos < 1 or pos > self.nodeCount:
            raise IndexError 

        prev = self.getAt(pos - 1)
        curr = self.getAt(pos)
        if self.nodeCount == 1:
            self.head = None
            self.tail = None
        else : 
            if pos  == 1:
                self.head = curr.next
            elif pos == self.nodeCount:
                self.tail = prev
                prev.next = None
            else: 
                prev.next = curr.next
        self.nodeCount -= 1
        return curr.data



    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0