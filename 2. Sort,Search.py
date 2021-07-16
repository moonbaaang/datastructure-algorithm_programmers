L = [3,4,6,7,8,2,5,1,9]
L2 = sorted(L)
print(L2)

L3 = sorted(L, reverse=True)
print(L3)

L.sort()
print(L)

L.sort(reverse=True)
print(L)

L = ['abcd', 'xyz', 'spam']
L2 = sorted(L, key=lambda x: len(x))
print(L2)

L = [{'name':'john', 'score':83}, {'name':'paul', 'score':92}]
L.sort(key=lambda x:x['score'], reverse=True)
print(L)
L.sort(key=lambda x:x['name'])
print(L)

# sort() > 리스트 자체를 정렬시켜줌
# sorted() > 리스트를 정렬 후 새로운 리스트로 생성 


# Linear Search > 리스트의 길이에 비례하는 시간 소요 O(n)
def linear_search(L, x):
    i = 0
    while i < len(L) and L[i] != x:
        i += 1
    if i < len(L):
        return i
    else:
        return -1

S = [3,8,2,7,6,10,9]
print(linear_search(S,6))

# 이진 탐색 (Binary Search) O(log n)
# 탐색하려는 리스트가 이미 정렬되어있는 경우에만 적용 (크기순으로 정렬되어있다는 성질 이용)
def binary_search(L, x):
    lower = 0
    upper = len(L)-1
    idx = -1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            return middle
        elif L[middle] > x:
            upper = middle-1
        else:
            lower = middle+1

    return -1

S.sort()
print(binary_search(S, 9))