di = [0,0,1] # 동 서 남
dj = [1,-1,0] # 0 1 2

from collections import deque

def simulate(start_j):
    i = 0
    j = start_j

    q = deque()
    q.append((i,j))

    check = [[-1] * 100 for _ in range(100)]
    check[i][j] = 0

    gi,gj=0,0

    while(q):
        i,j = q.popleft()
        gi,gj=i,j
        for k in range(3):
            ni = i+di[k]
            nj = j+dj[k]

            if not (0 <= ni < 100 and 0 <= nj < 100):
                continue

            if check[ni][nj] != -1:
                continue

            if MAP[ni][nj] == 0:
                continue

            check[ni][nj] = check[i][j] + 1
            q.append((ni,nj))
            break

    return check[gi][gj]




for testcase in range(10):

    t = int(input())
    MAP = []
    for _ in range(100):
        MAP.append(list(map(int,input().split())))
    ans = 10000000
    MINI_temp = 100000000
    for j in range(100):
        if MAP[0][j] == 1:
            temp = simulate(j)
            ans = min(temp,ans)

            if temp < MINI_temp:
                MINI_temp = temp
                ans = j

    print("#",end='')
    print(t,ans)