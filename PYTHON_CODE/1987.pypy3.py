R,C = list(map(int,input().split()))

MAP = []
for _ in range(R):
    MAP.append(list(map(lambda x: ord(x)-65,input())))


di = [0,0,1,-1]

dj = [1,-1,0,0]

check = [[False] * C for _ in range(R)]

check_ = [False] * 26

MAXI = 0
def dfs(i,j,cnt):
    global MAXI
    MAXI = max(MAXI,cnt)
    # print(i,j)
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]

        if not (0<= ni <R and 0<= nj < C):
            continue

        if check_[MAP[ni][nj]] == True:
            continue

        if check[ni][nj] == True:
            continue

        check[ni][nj] = True
        check_[MAP[ni][nj]] = True
        dfs(ni, nj, cnt + 1)
        check[ni][nj] = False
        check_[MAP[ni][nj]] = False

check_[MAP[0][0]] = True
dfs(0,0,1)

print(MAXI)