
#https://www.acmicpc.net/problem/11060

#단순 1차원 bfs문제


N = int(input())

Arr = [0] + list(map(int, input().split()))

check = [0] * (N+1)

# print(N,Arr)

now = 1

from collections import deque

q = deque()

q.append(now)
check[now] = 1

while(q):

    num = q.popleft()

    for k in range(1,Arr[num]+1):

        if not (1<= num+k < N+1):
            continue

        if check[num+k] != 0:
            continue

        check[num+k] = check[num] + 1
        q.append(num+k)


print(check[-1]-1)
