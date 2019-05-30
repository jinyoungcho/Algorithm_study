import copy
from collections import deque

N, M = list(map(int, input().split()))
MAP = []

di = [1,-1,0,0]
dj = [0,0,1,-1]

for _ in range(N):
    MAP.append(list(map(int,input().split())))

def check_MAP():
    find = True
    for i in range(1,N-1):
        for j in range(1,M-1):
            if MAP[i][j] == 1:
                return False
    return find


def bfs_air():
    air_check = [[False] * M for _ in range(N)]
    q = deque()
    q.append((0,0))
    air_check[0][0] = True

    li_next_air = []

    while(q):
        i,j = q.popleft()

        for k in range(4):
            ni,nj = i+di[k], j+dj[k]

            if not (0<= ni <N and 0 <= nj < M):
                continue

            if air_check[ni][nj] == True:
                continue

            if MAP[ni][nj] == 1:
                li_next_air.append((ni,nj))
                continue

            q.append((ni,nj))
            air_check[ni][nj] = True

    return li_next_air

t = 0
asdf = 0
while(True):

    li_next_air = bfs_air()

    if check_MAP():
        break

    # 1. bfs air
    # + 가장자리 치즈 갯수


    for i,j in set(li_next_air):
        MAP[i][j] = 0

    # print(set(li_next_air))
    asdf = len(set(li_next_air))
    t+=1

print(t)
print(asdf)