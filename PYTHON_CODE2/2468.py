N = int(input())
MAP = []

for _ in range(N):
    MAP.append(list(map(int, input().split())))

rain=set()

for i in range(N):
    for j in range(N):
        rain.add(MAP[i][j])

rain = sorted(list(rain))
len_rain = len(rain)
# print(rain)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

from collections import deque

def bfs(i, j, cn,r):

    q = deque()
    check[i][j] = cn
    q.append((i,j))

    while(q):
        i,j = q.popleft()

        for k in range(4):
            ni,nj = i+di[k], j+dj[k]

            if not (0 <= ni < N and 0 <= nj < N):
                continue

            if check[ni][nj] != 0:
                continue

            if MAP[ni][nj] <= r:
                continue

            check[ni][nj] = cn
            q.append((ni,nj))



MAXI = 1
# for r in rain:
for r in range(max(rain)):
    cn = 1
    check = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if check[i][j] != 0:
                continue
            if MAP[i][j] <= r:
                continue
            bfs(i,j,cn,r)
            cn += 1
    # print(r)
    # for _ in range(N):
    #     print(check[_])
    MAXI = max(cn,MAXI)

print(MAXI-1)
