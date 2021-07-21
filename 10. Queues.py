'''
큐 (Queues)

 - 자료(data element)를 보관할 수 있는 (선형) 구조
 - 단, 넣을 때는 한쪽 끝에서 밀어넣어야 하고 인큐(enqueue) 연산 
 - 꺼낼 때에는 반대 쪽에서 뽑아 꺼내야 함 디큐(dequeue) 연산
 - 선입선출 (FIFO) 특징

큐의 동작
 - 초기 상태 : empty queue ( Q = Queue() )
 - 데이터원소 A를 큐에 추가 ( Q.enqueue(A) )
 - 데이터원소 B를 큐에 추가 ( Q.enqueue(B) )
 - 데이터 원소 꺼내기 ( r1 = Q.dequeue()  >>  A )


큐의 추상적 자료구조 구현
 (1) 배열(Array)을 이용하여 구현
    - python리스트와 메서드 이용
 (2) 연결리스트(Linked List)를 이용하여 구현
    - 양방향 연결리스트 이용

 - 연산의 정의
    - size() - 현재 큐에 들어있는 데이터 원소의 수
    - isEmpty() - 현재 큐가 비어있는지 판단
    - enqueue(x) - 데이터원소 x를 큐에 추가
    - dequeue() - 큐의 맨앞에 저장된 데이터원소를 제거( 또한 , 반환 )
    - peek() - 큐의 맨 앞에 저장된 데이터원소를 반환 (제거하지 않음)

from pythonds.basic.queie import Queue
'''

# 배열로 구현한 큐 / 복잡도 dequeue() 만 O(n)

class ArrayQueue:

    def __init__(self): # 빈 큐를 초기화
        self.data = [] 
    
    def size(self): # 큐의 크기 리턴
        return len(self.data)
    
    def isEmpty(self): # 큐가 비어있는지 판단
        return self.size() == 0

    def enqueue(self, item): # 데이터 원소를 추가
        self.data.append(item)

    def dequeue(self): # 데이터 원소를 삭제(리턴)
        return self.data.pop(0)

    def peek(self): # 큐의 맨 앞 원소 반환
        return self.data[0]


# 양방향 연결리스트로 구현하는 큐
class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList:
    
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList : empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        
        return s

    def getLength(self):
        return self.nodeCount

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data) 
        
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount//2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1

        else: 
            i = 0
            curr = self.head
            while i < pos :
                curr = curr.next
                i += 1
            
        return curr

    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount+1:
            return None
        
        prev = self.getAt(pos-1)
        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        
        return True

    def popAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            raise IndexError('Index out of range')
           
        prev = self.getAt(pos-1)
        return self.popAfter(prev)

    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail
        self.nodeCount += L.nodeCount


class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        #return self.data.nodeCount
        return self.data.getLength()

    def isEmpty(self):
        #return self.data.nodeCount == 0
        return self.size() == 0

    def enqueue(self, item):
        node = None(item)
        #self.data.insertAfter(self.data.tail.prev, node)
        #self.data.insertAt(self.data.nodeCount+1, node)
        self.data.insertAt(self.size()+1, node)

    def dequeue(self):
        #return self.data.popAfter(self.data.head)
        return self.data.popAt(1)

    def peek(self):
        return self.data.head.next.data
        #return self.data.getAt(1).data


def solution(x):
    return 0