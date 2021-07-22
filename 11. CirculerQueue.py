'''
큐(Queue)의 활용

 - 자료를 생성하는 작업과 자료를 이용하는 작업이 비동기적(asynchronously)으로 일어나는 경우
 - 자료를 생성하는 작업이 여러 곳에서 일어나는 경우
 - 자료를 이용하는 작업이 여러 곳에서 일어나는 경우
 - 자료를 생성하는 작업과 그 자료를 이용하는 작업이 양쪽 다 여러곳에서 일어나는 경우
 - 자료를 처리하여 새로운 자료률 생성하고, 나중에 그 자료를 또 처리해야하는 작업의 경우

환형 큐(circular Queue)
 - 정해진 개수의 저장 공간을 빙 돌려가며 이용
 - 데이터를 꺼내는 포인터 - front
 - 데이터를 넣는 포인터 - rear

    큐가 가득 차면 더이상 원소를 넣을 수 없음 (큐 길이를 기억해야함)

연산의 정의
size() - 현재 큐에 들어있는 데이터 원소 수를 구함
isEmpty() - 현재 큐가 비어있는지 판단
isFull() - 큐에 데이터 원소가 꽉 차있는지 판단
enqueue(x) - 데이터 원소 x를 큐에 추가
dequeue() - 큐의 맨 앞에 저장된 데이터 원소를 제거, 반환
peek() - 큐의 맨 앞에 저장된 데이터 원소를 반환

배열로 구현한 환형 큐
정해진 길이 n의 리스트 확보
Q.enqueue(A) > rear 가 A를 가리키도록 함
Q.enqueue(B) > rear 가 B를 가리키도록 함

r1 = Q.dequeue() > front 가 A를 가리키도록 함 > 데이터가 없어짐(유효하지 않은 데이터)

'''

class CircularQueue:

    def __init__(self, n):
        self.maxCount = n
        self.data = [None]*n
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = (self.rear+1) % self.maxCount
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        self.front = (self.front+1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front+1) % self.maxCount]