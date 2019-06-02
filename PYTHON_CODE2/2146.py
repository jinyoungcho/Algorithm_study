N = int(input())

MAP = []

for _ in range(N):
    MAP.append(list(map(int,input().split())))

from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

cn_dict = {}

def bfs_for_cn(i,j,cn):

    q = deque()
    check[i][j] = True
    q.append((i,j))
    while(q):
        i, j = q.popleft()
        # print(i,j)
        MAP[i][j] = cn
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]

            if not (0<= ni < N and 0 <= nj < N):
                continue

            if MAP[ni][nj] == 0:
                if (i,j) not in cn_dict[cn]:
                    cn_dict[cn].append((i,j))
                continue

            if check[ni][nj]:
                continue

            check[ni][nj] = True
            q.append((ni, nj))



check = [[False] * N for _ in range(N)]

cn = 1
for i in range(N):
    for j in range(N):
        if check[i][j] == True or MAP[i][j]==0:
            continue
        cn_dict[cn] = []
        bfs_for_cn(i,j,cn)
        cn += 1

land = list(cn_dict.keys())
MINI = 100000

len_lan = len(land)

for ldx in range(len_lan-1):
    for ldx2 in range(ldx+1, len_lan):
        if ldx == ldx2: continue

        # print(land[ldx])


        for i,j in cn_dict[land[ldx]]:
            for i2, j2 in cn_dict[land[ldx2]]:

                temp = abs(i-i2) + abs(j-j2)

                MINI = min(MINI,temp)

print(MINI-1)