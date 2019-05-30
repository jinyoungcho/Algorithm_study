N,M = list(map(int,input().split()))

MAP = [input() for _ in range(N)]

# print(MAP)

check = [[False] * M for _ in range(N)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

def make_False():
    for i in range(N):
        for j in range(M):
            check[i][j] = False

def dfs(i,j,cnt):
    global can
    # print(i, j,cnt)
    if can == True:
        return

    for k in range(4):

        ni = i + di[k]
        nj = j + dj[k]

        if cnt >= 4 and zi == ni and zj == nj:
            # print("?")
            can = True
            return

        if not(0 <= ni < N and 0 <= nj < M):
            continue

        if check[ni][nj] == True:
            continue

        if MAP[ni][nj] != MAP[zi][zj]:
            continue



        check[ni][nj] = True
        dfs(ni,nj,cnt+1)
        check[ni][nj] = False


can = False

for zi in range(N):
    for zj in range(M):
        make_False()
        check[zi][zj] = True
        dfs(zi,zj,1)

        # print(can)

        if can == True:
            break

    if can == True:
        break

print("Yes" if can == True else "No")