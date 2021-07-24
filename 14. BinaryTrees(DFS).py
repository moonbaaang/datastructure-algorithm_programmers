'''
이진 트리 (Binary trees)

이진 트리의 추상적 자료구조
연산의 정의
 - size() - 현재 트리에 포함되어 있는 노드의 수
 - depth() - 현재 트리의 깊이 (또는 높이; height)
 - 순회(traversal)

이진 트리의 구현 - Node

        data
    left    right

    Node :
            - Data
            - Left Child
            - Right Child

이진 트리의 구현 - size()
    전체 이진 트리의 size() =
        left subtree의 size() + right subtree의 size() + 1 (root)

이진 트리의 구현 - depth()
    전체 이진 트리의 depth() = left subtree의 depth()와 right subtree의 depth()중 더 큰 것 + 1

이진 트리의 순회 (traversal)
                    A
            B               C
        D       E       F       G
    H                       J(parent > F)    

 - 깊이 우선 순회 (depth first traversal) DFS
    - 중위 순회 (in-order traversal)
        > (1) Left subtree (2) 자기자신 (3) Right subtree
        > H D B E A F J C G
    - 전위 순회 (pre-order traversal)
        > (1) 자기자신 (2) Left subtree (3) Right subtree
        > A B D H E C F J G
    - 후위 순회 (post-order traversal)
        > (1) Left subtree (2) Right subtree (3) 자기자신
        > H D E B J F G C A

 - 넓이 우선 순회 (breadth first traversal) BFS
'''

class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        #return max(l, r) + 1
        return l + 1 if l > r else r + 1

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal


class BinaryTree:
    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0 # case : empty tree
        
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []