'''
힙 (Heap)
 이진 트리의 한 종류 ( 이진 힙 - binary heap)

    1. root 노드가 언제나 최댓값 또는 최솟값을 가짐
        - max heap(최대 힙), min heap (최소 힙)
    2. 완전 이진 트리여야 함


이진 탐색 트리와의 비교
1. 원소들은 완전히 크기 순으로 정렬되어있는가? > 이진탐색 O , 힙 X (느슨한 정렬)
2. 특정 키값을 가지는 원소를 빠르게 검색할 수 있는가? > 이진탐색 O, 힙 X
3. 부가의 제약조건은 어떤 것인가? > 힙은 완전이진트리여야 함

최대 힙(max heap)의 추상적 자료구조
연산의 정의
 - __init__() : 빈 최대 힙을 생성
 - insert(item) : 새로운 원소를 삽입
 - remove() : 최대 웟노 (root node)를 반환 (그리고 동시에 이 노드를 삭제)

데이터 표현의 설계
    배열을 이용한 이진 트리의 표현 (0번 인덱스는 생각하지 않음)
    노드번호 m을 기준으로
        - 왼쪽 자식의 번호 2*m
        - 오른쪽 자식의 번호 2*m + 1
        - 부모 노드의 번호 m//2

    완전 이진 트리이므로 노드의 추가/삭제는 마지막 노드에서만 가능


최대 힙에 원소 삽입
    1. 트리의 마지막 자리에 새로운 원소를 임시로 저장
    2. 부모 노드와 키값을 비교하여 위로, 위로, 이동

    복잡도
    원소의 개수가 n인 최대 힙에 새로운 원소 삽입
     > 부모 노드와의 대소 비교 최대 회수 : log_2_n
     > 최악 복잡도 O(logn)의 삽입 연산

'''

# 빈 힙 생성
class MaxHeap:

    def __init__(self):
        self.data = [None]

    #삽입 연산의 구현
    def insert(self, item):
        self.data.append(item)
        
        idx = len(self.data)-1
        while idx>1:
            parent = idx//2
            if self.data[idx] > self.data[parent]:
                self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
                idx = parent
            else:
                break