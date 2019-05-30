
from itertools import combinations
from collections import deque
from copy import deepcopy,copy

di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs(t_cell):
    MAP = deepcopy(copy_MAP)

    for i,j in t_cell:
        MAP[i][j] = 1

    q = deque(t_cell)

    while(q):

        i,j = q.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != -1 and MAP[ni][nj] == 0:

                MAP[ni][nj] = MAP[i][j] + 1
                q.append((ni,nj))

    # print("-")
    # print(t_cell)
    # for _ in range(N):
    #     print(MAP[_])

    t = 1
    for i in range(N):
        for j in range(N):
            if (i,j) in cell_list:
                continue
            if MAP[i][j] == 0:
                return 1000000000
            else:
                t = max(t,MAP[i][j])
    return t

def simulate():
    MINI = 100000000
    for comb in combinations(cell_list,M):

        t_cell = comb
        temp = bfs(t_cell)
        MINI = min(temp,MINI)

    return MINI




N,M = list(map(int,input().split()))

MAP = [list(map(int,input().split())) for _ in range(N)]

cell_list = []

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 2:
            cell_list.append((i,j))
            MAP[i][j] = 0
        elif MAP[i][j] == 1:
            MAP[i][j] = -1

copy_MAP = deepcopy(MAP)

ans = simulate()

if ans == 100000000:
    ans = -1
    print(ans)
else:
    print(ans-1)