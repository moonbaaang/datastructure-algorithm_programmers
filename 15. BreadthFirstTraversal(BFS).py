'''
Binary Trees
깊이 우선 순회 (depth first traversal) (DFS)
    - 중위 순회 (in-order traversal) = ltr
    - 전위 순회 (pre-order traversal) = rlr

    - 후위 순회 (post-order traversal) = lrt

넓이 우선 순회 Breadth first traversal (BFS)
    원칙
        - 수준(level)이 낮은 노드를 우선으로 방문
        - 같은 수준의 노드들 사이에는
            - 부모 노드의 방문 순서에 따라 방문 (부모노드가 먼저 방문된 노드들)
            - 왼쪽 자식 노드를 오른쪽 자식보다 먼저 방문
                
                    A
            B               C
        D       E       F       G
    H                      J

    순서 : A B C D E F G H J 

    한 노드 방문시
        - 나중에 방문할 노드들을 순서대로 기록해두어야함
        - 큐 (queue) 이용

넓이 우선 순회 알고리즘 설계

위 트리에서 A를 방문시 queue에 B, C가 순서대로 들어감 > queue[B, C]
node A처리가 끝났을 때 B방문, queue에 D, E를 넣음> queue[C, D, E]
node B처리가 끝났을 때 queue에서 C를 뽑아 방문, queue에 F, G를 넣음 > queue[D, E, F, G]

1. (초기화) traversal < 빈리스트, q < 빈 큐
2. 빈 트리가 아니면, root node 를 큐에 추가 (enqueue)
3. 큐가 비어있지 않은 동안
    (1) node < q에서 원소 추출 (dequeue)
    (2) node 방문
    (3) node의 왼쪽, 오른쪽 자식(있으면)을 queue에 추가
4. queue가 빈 queue가 되면 모든 노드 방문 완료
'''
class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def bft(self):
        Q = ArrayQueue()   
        bfs = []
        if self.root:
            Q.enqueue(self.root)
    
        while not Q.isEmpty():
            node = Q.dequeue()
            if node.left:
                Q.enqueue(node.left)
            if node.right:
                Q.enqueue(node.right)
            bfs.append(node.data)
        return bfs
