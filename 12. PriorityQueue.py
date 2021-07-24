'''
우선순위 큐 (priority Queue)
 - 큐가 FIFO 방식을 따르지 않고 원소들의 우선순위에 따라
   큐에서 빠져나오는 방식

    예) 운영체제의 CPU 스케쥴러

우선순위 큐의 구현
    (1) Enqueue 할 때 우선순위 순서를 유지하도록 > 이 방식이 더 유리
    (2) Dequeue 할 때 우선순위 높은 것을 선택

    서로 다른 두가지 재료를 이용할 수 있음
        - 선형 배열 이용 > 공간적으로 유리
        - 연결 리스트 이용 > 시간적으로 유리
            (원소들의 우선순위를 유지, 데이터 삽입이 빈번)
'''

from doublylinkedlist import Node, DoublyLinkedList

class PriorityQueue:
    def __init__(self, x):
        self.queue = DoublyLinkedList()

    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head
        while curr.next.data != None and curr.next.data > x:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data

def solution(x):
    return 0