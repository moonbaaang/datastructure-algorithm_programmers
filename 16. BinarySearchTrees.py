'''
이진 탐색 트리 (Binary search trees)

모든 노드에 대해서, 
    - 왼쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 작고
    - 오른쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 큰 성질

(장점) : 데이터 원소 추가, 삭제 용이
(단점) : 공간 소요가 큼

데이터 표현 - 각 노드는 (key, value) 쌍으로
                5,john
          2,David             8,Mary
    1,Patrick   4,Sue   6,Anne      9,Clara
                           7,Peter

key를 이용해 검색 가능
보다 복잡한 데이터 레코드로 확장 가능

연산의 정의
 - insert(key, data) - 트리에 주어진 데이터 원소를 추가
 - remove(key) - 특정 원소를 트리로부터 삭제
 - lookup(key) - 특정 원소를 검색
 - inorder() - 키의 순서대로 데이터 원소를 나열
 - min(), max() - 최소 키, 최대 키를 가지는 원소 탐색

 lookup()
 입력인자 : 찾으려는 대상 키
 리턴 : 찾은 노드와 그것의 부모 노드

 각각, 없으면 None으로

'''

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self 

    def lookup(self, key, parent=None): # parent=None? parent라는 인자를 주지 않으면 None으로 기본값 설정
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self) # parent=self? self를 parent 인자에 담아 전달 
            
            else:
                return None, None
       
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        
        else:
            return self, parent # key = self, parent > self의 parent


    def insert(self, key, data):
        if self.key > key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key,data)
        elif self.key < key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError("Key Error")
            
        return True


class BinSearchTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None

    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)