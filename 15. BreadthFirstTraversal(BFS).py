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
'''