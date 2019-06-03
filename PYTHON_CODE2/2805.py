#  Binary Search

#  https://www.acmicpc.net/problem/2805

N, M = list(map(int,input().split()))

Arr = list(map(int,input().split()))
Arr.sort()

def binary_search():
    ans = 0
    st = 0
    ed = Arr[-1]

    while st <= ed:

        md = (st+ed) // 2

        temp = 0

        for tree in Arr:
            if tree > md:
                temp += tree - md

        if temp >= M:
            ans = md
            st = md + 1
        else:
            ed = md - 1

    return ans

print(binary_search())