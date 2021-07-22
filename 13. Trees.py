'''
트리(Tree)

정점(node)과 간선(edge)을 이용해 데이터의 배치 형태를 추상화한 자료구조
나무에는 이파리(leaf), 뿌리(root)가 존재.
컴퓨터에서 트리 표현 시 나무를 뒤집어 둔 모양과 유사함

                A               (root node)
        B               C
        D           E       F   (내부 노드 internal node)
    G   H   J               K   (lead node (더이상 edge가 없음))
    > 10개의 노드, 9개의 간선

    node D 는 node G,H,J 의 부모node(parent node)
    node G,H,J 는 node D의 자식node(child node)
    node G,H,J 는 서로 형제간(sibling)
    
    parent의 parent - 조상 (ancestor)
    child의 child - 후손 (descendant)

    노드의 수준 (Level) > root node's level = 0 (어느 교재는 1로 표기하기도함)
    > child로 갈 수록 1씩 증가함

    트리의 높이 (height) = 최대 level + 1 (깊이 depth 라고도 함)

    부분트리 (subtree) - 위에서 B를 root node로 하는 서브트리로 생각할 수 있음
    
    노드의 차수 (Degree) - 자식(child / sub tree)의 수 / degree = 0 > leaf node

이진 트리 (Binary Tree)
    - 모든 노드의 차수가 2이하인 tree
    - 재귀적으로 정의할 수 있음
        > 빈 트리(empty tree) 이거나, 
        > 루트 노드 + 왼쪽 서브트리 + 오른쪽 서브트리
        (단, 이 때 왼쪽과 오른쪽 서브트리 또한 이진 트리)


포화 이진 트리 (Full Binary Tree)
    - 모든 레벨에서 노드들이 모두 채워져 있는 이진 트리
    - 높이가 k 이고 노드 개수가 2^k-1 인 이진트리       

완전 이진 트리 (Complete Binary Tree)
    - 높이 k인 완전 이진 트리
    - 레벨 k-2 까지는 모든 노드가 2개의 자식을 가진 포화 이진 트리
    - 레벨 k-1 에서는 왼쪽부터 노드가 순차적으로 채워져 있는 이진 트리
'''