# 피보나치 순열
def solution(x):   
    if x<2:
        return x
    else: 
        return solution(x-1) + solution(x-2)

# 재귀 알고리즘 응용
'''
n개의 서로 다른 원소에서 m개를 택하는 경우의수
n! / m!(n-m)!
from math import factorial as f
def combi(n,m):
    return f(n)/(f(m)*f(n-m))

def combi(n,m):
    return combi(n-1, m) + combi(n-1, m-1)
    >> trivial case를 고려하지 않은 실수


def combi(n,m):
    if n==m:
        return 1
    elif m ==0:
        return 1
    else:
        return combi(n-1, m) + combi(n-1, m-1)
    >> 효율성? 떨어짐


하노이의 탑
세 기둥에 끼어있는 원반 옮기기 (지름이 더 큰 원반은 작은 워반 위에 있을 수 없음)

피보나치 수열
fibo(4) = fibo(3)+fibo(2)
        = fibo(2) + fibo(1)    = fibo(1) + fibo(0)
        = fibo(1) + fibo(0)


재귀적 이진 탐색
def binseasrch(L,x,lower,upper):
    if ___ :
        return -1
    mid = (lower+upper)//2

    if x==L[mid]:
        return mid
    elif x<L[mid]:
        return ____
    else:
        return ____
'''

def solution(L, x, l, u):
    if l>u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid-1)
    else:
        return solution(L, x, mid+1, u)

