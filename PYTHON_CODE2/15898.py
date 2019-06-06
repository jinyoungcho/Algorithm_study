#connected component

di=[0,0,1,-1,-1,-1,1,1]
dj=[1,-1,0,0,-1,1,-1,1]

from collections import deque

def bfs(i, j):

    q = deque()
    q.append((i,j))
    check[i][j] = True

    while(q):

        i, j = q.popleft()
        # print(i,j)
        for k in range(8):

            ni, nj = i + di[k], j + dj[k]

            if not (0<= ni < N and 0 <= nj < M):
                continue
            if check[ni][nj] == True:
                continue
            if MAP[ni][nj] == 0:
                continue

            check[ni][nj] = True
            q.append((ni,nj))


while(True):

    M, N = list(map(int, input().split()))

    if M == 0 and N == 0:
        break

    MAP = []

    for _ in range(N):
        MAP.append(list(map(int, input().split())))

    # print(MAP)

    check = [[False]*M for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if check[i][j] == False and MAP[i][j] != 0:
                bfs(i,j)
                cnt+=1
    print(cnt)