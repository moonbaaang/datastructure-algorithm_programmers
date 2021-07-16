def solution(L, x):
    if L[-1]<x :
        L.append(x)
    else:
        for idx, item in enumerate(L[:-1]):        
            if item>=x:
                L.insert(idx, x)
                break

    answer = L
    return answer



def solution(L, x):
    answer = []
    for idx, item in enumerate(L):
        if item == x:
            answer.append(idx)
            
    if len(answer) == 0:
        answer.append(-1)
    return answer

def solution(L, x):
    if x in L:
        return [i for i, item in enumerate(L) if item == x]
    else:
        return [-1]