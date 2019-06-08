# connected component

import copy

N, M = list(map(int, input().split()))

MAP = []

for _ in range(N):
    MAP.append(list(input()))

check_for_copy = [[-1] * M for _ in range(N)]


from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(i, j, check):

    q = deque()

    q.append((i, j))

    check[i][j] = 0

    ccnt = 0

    while(q):

        i, j = q.popleft()

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]

            if not (0 <= ni < N and 0 <= nj < M):
                continue

            if MAP[ni][nj] == 'W':
                continue

            if check[ni][nj] != -1:
                continue

            check[ni][nj] = check[i][j] + 1
            ccnt = max(ccnt, check[ni][nj])
            q.append((ni, nj))

    return ccnt




dist = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'L':
            check = copy.deepcopy(check_for_copy)
            # print(i,j)
            new_dist = bfs(i, j,check)

            # for _ in range(N):
            #     print(check[_])
            #
            # print(new_dist)

            dist = max(new_dist, dist)

print(dist)