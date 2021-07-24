# 이진 탐색 트리 (Binary Search Trees) 이전 강의에 remove() 연산 추가
'''
이진 탐색 트리에서 원소 삭제
    1. key를 이용해 노드를 찾는다.
        - 해당 키의 노드가 없으면 삭제할 것도 없음
        - 찾은 노드의 부모 노드도 알고 있어야함 ( 2번이 이유 )
    
    2. 찾은 노드를 제거하고도 이진 탐색 트리 성질을 만족하도록 트리의 구조를 정리

인터페이스의 설계
    입력 : key
    출력 : 삭제한 경우 True / 해당 키의 노드가 없는 경우 False

class BinSearchTress:
    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            ....
            return True
        else:
            return False

삭제되는 노드가
    1. 말단(leaf) 노드인 경우
        - 그냥 노드를 삭제하면 됨
            > 해당 노드를 빼고도 이진 트리 유지
            > 부모 노드의 링크를 조정(좌? 우?)
            > 해당 노드가 왼쪽이었는지 오른쪽이었는지 판단 후 None 반환
            > 삭제되는 노드가 root node 인 경우는 ? > tree 전체가 없어짐
    2. 자식을 하나 가지고 있는 경우
        - 삭제되는 노드 자리에 그 자식을 대신 배치
        - 자식이 왼쪽이었는지 오른쪽이었는지? 확인 후 기존의 부모노드에 연결
        - 부모 노드의 링크를 조정 (좌, 우)
         > 삭제되는 노드가 root node인 경우 > 대신 들어오는 자식이 새로 root가 됨
    3. 자식을 둘 가지고 있는 경우
        - 삭제되는 노드보다 바로 다음(큰 또는 작은) 키를 가지는(5 삭제시 6) 노드를 찾아 
        그 노드를 삭제되는 노드 자리에 대신 배치하고(successer / parent도 변경) 이 노드를 대신 삭제

이진 탐색 트리가 효율적이지 못한 경우
    T = BinSearchTree()
    T.insert(1, 'john')
    T.insert(2, 'Mary')
    T.insert(3, 'Anne')
    T.insert(4, 'Peter')
    > 선형 탐색과 동등한 복잡도를 가짐 (한쪽으로 치우침) 

높이의 균형을 유지함으로써 O(logn)의 탐색복잡도 보장
> 삽입, 삭제 연산이 보다 복잡
> AVL tree / Red-black tree
'''
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)

        if key > self.key:
            if self.right:    
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError("Key %s is already exist." %key)

    
    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, key

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal        

    def countChildren(self): # 어떤 노드의 자식 수
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

class BinSearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None

    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case if no children
            if nChildren == 0:
                # 만약 parent가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단해
                # parent.left 또는 parent.right 를 None으로 하여
                # leaf node 였던 자식을 트리에서 끊어내 없앰
                if parent:
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None
                # 만약 parent가 없으면 (node는 root인 경우)
                # self.root 를 None으로 하여 빈 트리로 만듬
                else:
                    self.root = None

            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지 판단해
                # 그 자식을 어떤 변수가 가리키도록 함
                if node.left:
                    newnode = node.left
                else:
                    newnode = node.right
                # 만약 parent가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단해
                # 위에서 가리킨 자식을 대신 node의 자리에 넣음
                if parent:
                    if parent.left == node:
                        parent.left = newnode
                    else:
                        parent.right = newnode
                # 만약 parent가 없으면 (node 는 root인 경우)
                # self.root에 위에서 가리킨 자식을 대신 넣음
                else:
                    self.root = newnode

            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent는 node 를 가리키고 있고
                # successor는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor는 바로 다음 키를 가진 노드를,
                # 그리고 parent는 그 노드의 부모 노드를 가리키도록 찾아냄
                while successor.left:
                    parent = successor
                    successor = successor.left
                # 삭제하려는 노드인 node에 successor의 key, data를 대입
                node.key = successor.key
                node.data = successor.data
                # 이제 successor가 parent의 왼쪽 자식인지 오른쪽 자식인지 판단해
                # 그에 따라 parent.left 또는 parent.right를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 함
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
            return True

        else:
            return False


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

def solution(x):
    return 0