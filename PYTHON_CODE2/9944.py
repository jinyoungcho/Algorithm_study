# 3차원 bfs 문제

N,M,K = list(map(int,input().split()))

si,sj = 0,0
gi,gj = N-1,M-1


MAP = []
for _ in range(N):
    # MAP.append(list(map(int,input().split())))
    MAP.append(list(map(int,list(input()))))
check = [[[0]*(K+1) for _ in range(M)] for __ in range(N)]

from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs(si, sj):

    i = si; j = sj; b_b = 0

    q = deque()

    q.append((i, j, b_b))

    check[i][j][b_b] = 1

    while(q):
        i, j, b = q.popleft()

        for k in range(4):

            ni = i + di[k]
            nj = j + dj[k]

            if not(0 <= ni < N and 0 <= nj < M):
                continue

            if b < K:
                if MAP[ni][nj] == 1:

                    if check[ni][nj][b+1] != 0:
                        continue

                    check[ni][nj][b+1] = check[i][j][b] + 1
                    q.append((ni, nj, b+1))

                elif MAP[ni][nj] == 0:

                    if check[ni][nj][b] != 0:
                        continue

                    check[ni][nj][b] = check[i][j][b] + 1
                    q.append((ni, nj, b))

            elif b == K:

                if check[ni][nj][b] != 0:
                    continue

                if MAP[ni][nj] == 0:
                    check[ni][nj][b] = check[i][j][b] + 1
                    q.append((ni, nj, b))


bfs(si,sj)

# print(check[gi][gj])

MINI = 10000000
for _ in check[gi][gj]:
    if _ == 0:
        continue
    else:
        MINI = min(MINI ,_)

if MINI == 10000000:
    print(-1)
else:
    print(MINI)

# if check[gi][gj][0] == 0 and check[gi][gj][1] == 0:
#     print(-1)
# elif check[gi][gj][0] != 0 and check[gi][gj][1] != 0:
#     print(min(check[gi][gj])-1)
# elif check[gi][gj][0] == 0 and check[gi][gj][1] != 0:
#     print(check[gi][gj][1] - 1)
# elif check[gi][gj][0] != 0 and check[gi][gj][1] == 0:
#     print(check[gi][gj][0] - 1)

# for _ in range(N):
#     print(check[_])
