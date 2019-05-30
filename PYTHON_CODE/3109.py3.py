from collections import deque

R, C = list(map(int,input().split()))

MAP = [list(input()) for _ in range(R)]

check = [[False] * C for _ in range(R)]

di = [-1,0,1]
dj = [1,1,1]

def dfs(i, j):
    if j == C-1:
        # print("~")
        return True

    for k in range(3):

        ni = i + di[k]
        nj = j + dj[k]

        if not (0 <= ni < R and 0 <= nj < C):
            continue

        if MAP[ni][nj] != '.':
            continue
        MAP[ni][nj] = '~'
        if dfs(ni,nj):

            return True

    return False



cnt = 0
for _ in range(R):
    # print("!!!",_)
    if dfs(_,0):
        cnt += 1

    # for _ in range(R):
    #     print(MAP[_])

print(cnt)