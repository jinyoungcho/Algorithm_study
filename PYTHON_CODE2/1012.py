T = int(input())

from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs(i,j):
    q = deque()
    check[i][j] = True
    q.append((i,j))

    while q:

        i,j = q.popleft()

        for k in range(4):

            ni = i+di[k]
            nj = j+dj[k]

            if not (0<=ni<N and 0<=nj<M):
                continue
            if check[ni][nj]:
                continue
            if MAP[ni][nj] == 0:
                continue

            q.append((ni, nj))
            check[ni][nj] = True

for t in range(T):

    M, N, K = list(map(int, input().split()))

    MAP = [[0]*M for _ in range(N)]
    check = [[False] * M for _ in range(N)]

    for _ in range(K):
        j,i = list(map(int,input().split()))
        MAP[i][j] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 1 and check[i][j] != True:
                bfs(i,j)
                cnt += 1

    print(cnt)