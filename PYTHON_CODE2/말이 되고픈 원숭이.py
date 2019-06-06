# 3D - bfs

K = int(input())

M,N = list(map(int,input().split()))

MAP = []

for _ in range(N):
    MAP.append(list(map(int, input().split())))

from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

di2 = [-1,-2,-2,-1,  1, 2,2,1]
dj2 = [-2,-1, 1, 2, -2,-1,1,2]

def bfs():
    i, j = 0, 0

    goal_i, goal_j = M-1, N-1

    q = deque()

    q.append((i, j, 0))

    # check = [[[0] * K for __ in M] for _ in range(N)]

    check = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

    check[i][j][0] = 1

    while(q):
        i, j, k_move = q.popleft()

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]

            if not (0<= ni < N and 0 <= nj <M):
                continue
            if MAP[ni][nj] == 1:
                continue
            if check[ni][nj][k_move] != 0:
                continue

            check[ni][nj][k_move] = check[i][j][k_move] + 1
            q.append((ni, nj, k_move))

        if k_move >= K:
            continue

        for k in range(8):
            ni, nj = i + di2[k], j + dj2[k]

            if not (0<= ni < N and 0 <= nj <M):
                continue
            if MAP[ni][nj] == 1:
                continue
            if check[ni][nj][k_move+1] != 0:
                continue

            check[ni][nj][k_move+1] = check[i][j][k_move] + 1
            q.append((ni, nj, k_move+1))

    return check[N-1][M-1]

res = bfs()

ans = 100000000
for temp in res:
    if temp != 0:
        ans = min(ans,temp)

if ans == 100000000:
    print(-1)
else:
    print(ans-1)