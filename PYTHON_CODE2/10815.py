#  Binary Search

#  https://www.acmicpc.net/problem/10815

#  Binary Search 할때 Arr 길이 -1 을 ed로 놔둬라!! 기억해라!!!!

N = int(input())

Arr = list(map(int,input().split()))
Arr.sort()
M = int(input())

def binary_search(Arr, n):

    st = 0
    ed = len(Arr)-1

    while st <= ed:

        md = (st+ed)//2

        # if md >= len(Arr):
        #     break

        if Arr[md] > n:
            ed = md - 1
        elif Arr[md] < n:
            st = md + 1
        else:
            return 1



    return 0


for n in list(map(int,input().split())):

    print(binary_search(Arr,n),end=' ')