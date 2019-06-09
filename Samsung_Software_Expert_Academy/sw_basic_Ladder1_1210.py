di = [0,0,1] # 동 서 남
dj = [1,-1,0] # 0 1 2

from collections import deque

def simulate(start_j):
    i = 0
    j = start_j

    q = deque()
    q.append((i,j))

    check = [[False] * 100 for _ in range(100)]
    check[i][j] = True

    while(q):
        i,j = q.popleft()

        if MAP[i][j] == 2:
            # print(i,j)
            return True

        for k in range(3):
            ni = i+di[k]
            nj = j+dj[k]

            if not (0 <= ni < 100 and 0 <= nj < 100):
                continue

            if check[ni][nj]:
                continue

            if MAP[ni][nj] == 0:
                continue

            check[ni][nj] = True
            q.append((ni,nj))
            break

    return False




for testcase in range(10):

    t = int(input())
    MAP = []
    for _ in range(100):
        MAP.append(list(map(int,input().split())))
    ans = -1
    for j in range(100):
        if MAP[0][j] == 1:
            if simulate(j):
                ans = j
                break
    print("#",end='')
    print(t,ans)