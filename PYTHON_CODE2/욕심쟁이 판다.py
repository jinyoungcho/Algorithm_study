import copy

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N = int(input())

MAP = []

for _ in range(N):
    MAP.append(list(map(int, input().split())))


import sys

sys.setrecursionlimit(1000000)

MAXI = 0
check = [[False] * N for _ in range(N)]
DP = [[0]*N for _ in range(N)]



def dfs(i,j):

    if DP[i][j] != 0:
        return DP[i][j]

    DP[i][j] = 1
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if not(0 <= ni < N and 0 <= nj < N):
            continue
        if MAP[ni][nj] <= MAP[i][j]:
            continue
        DP[i][j] = max(DP[i][j], dfs(ni, nj)+1)
    return DP[i][j]



for i in range(N):
    for j in range(N):
        MAXI = max(dfs(i,j),MAXI)

print(MAXI)