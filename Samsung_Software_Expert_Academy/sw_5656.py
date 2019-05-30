from collections import deque
from copy import deepcopy

T = int(input())

for t in range(1, T + 1):

    N, W, H = list(map(int, input().split()))

    MAP = [list(map(int, input().split())) for _ in range(H)]

    MINI = W * H


    def drop(fixed_j):
        q = deque()

        for i in range(H):
            if MAP[i][fixed_j] != 0:
                q.append((i, fixed_j, MAP[i][fixed_j]))
                break
        # print(q)
        while (q):
            i, j, boom = q.popleft()

            MAP[i][j] = 0

            # 상
            for next_i in range(i - 1, i - boom, -1):
                if next_i < 0:
                    break
                else:
                    q.append((next_i, j, MAP[next_i][j]))
            # 하
            for next_i in range(i + 1, i + boom):
                if next_i >= H:
                    break
                else:
                    q.append((next_i, j, MAP[next_i][j]))
            # 좌
            for next_j in range(j - 1, j - boom, -1):
                if next_j < 0:
                    break
                else:
                    q.append((i, next_j, MAP[i][next_j]))
            # 우
            for next_j in range(j + 1, j + boom):
                if next_j >= W:
                    break
                else:
                    q.append((i, next_j, MAP[i][next_j]))


    def organize():
        q = deque()
        for j in range(W):
            for i in range(H - 1, -1, -1):
                if MAP[i][j] != 0:
                    q.append(MAP[i][j])
                    MAP[i][j] = 0
            i = H - 1
            while (q):
                MAP[i][j] = q.popleft()
                i -= 1


    def dfs(cnt, index):
        global MAP, MINI

        if cnt == N:
            temp = 0

            for i in range(H):
                for j in range(W):
                    if MAP[i][j] != 0:
                        temp += 1

            MINI = min(MINI, temp)

        else:
            for col in range(W):
                MAP2 = deepcopy(MAP)

                drop(col)

                organize()

                dfs(cnt + 1, col)

                MAP = deepcopy(MAP2)


    dfs(0, 0)

    print("#", end="")
    print(t, MINI)