#  Binary Search
#  https://www.acmicpc.net/problem/1920


N = int(input())
Arr = list(map(int, input().split()))
M = int(input())
goal = list(map(int,input().split()))
Arr.sort()

def binary_search(Arr, n):

    st = 0
    ed = len(Arr)

    while st <= ed:
        md = (st + ed) // 2
        if md == len(Arr) or md == [-1]:
            break

        # print('md',st,ed,md)
        if Arr[md] > n: #이 수보다 크면
            ed = md-1
        elif Arr[md] < n: #이 수보다 작으면
            st = md+1
        else:
            return 1

    return 0
for _ in range(M):

    n = goal[_]

    print(binary_search(Arr,n))