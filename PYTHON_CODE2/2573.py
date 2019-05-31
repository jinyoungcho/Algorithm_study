#BFS + connected component 문제입니다..!

N,M = list(map(int, input().split()))

MAP = []

for _ in range(N):
    MAP.append(list(map(int, input().split())))

from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def bfs(i,j,check):

    count_MAP = [[0]*M for _ in range(N)]
    q = deque()
    q.append((i,j))
    check[i][j] = True

    while(q):

        i,j = q.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if not (0 <= ni < N and 0 <= nj < M):
                continue

            if check[ni][nj] == True:
                continue

            if MAP[ni][nj] == 0:
                count_MAP[i][j] += 1
                continue

            q.append((ni,nj))
            check[ni][nj] = True

    # print("~")
    # for _ in range(N):
    #     print(count_MAP[_])

    for i in range(N):
        for j in range(M):
            MAP[i][j] -= count_MAP[i][j]
            if MAP[i][j] < 0:
                MAP[i][j] = 0




def simulate():

    t = 0
    while(True):
        # print("~t")
        check = [[False]*M for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(M):

                if MAP[i][j] == 0:
                    continue

                if check[i][j]:
                    continue

                bfs(i, j,check)
                cnt += 1
                # print(cnt)
                if cnt >= 2:
                    # print("~?")
                    return t

        if cnt == 0:
            return 0

        # print("~")
        # for _ in range(N):
        #     print(MAP[_])

        # break
        t += 1

print(simulate())