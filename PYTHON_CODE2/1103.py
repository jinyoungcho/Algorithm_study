N,M = list(map(int,input().split()))

MAP = []

for i in range(N):
    MAP.append(list(input()))

DP = [[0]* M for _ in range(N)]

visited = [[False] * M for _ in range(N)]

di = [0,0,1,-1]
dj = [1,-1,0,0]
flag = False


def dfs(i, j):



    #종료조건들

    if not (0 <= i < N and 0<= j <M):
        return 0
    # print(N,M)
    # print(i,j)
    if MAP[i][j] == 'H':
        return 0

    print("_")
    for _ in range(N):
        print(DP[_])

    if DP[i][j] != 0:
        return DP[i][j]

    if visited[i][j]:
        return -1
    #방문처리
    visited[i][j] = True


    move = ord(MAP[i][j]) - ord('0')
    max_result = 0 #일단 으로 처리

    for k in range(4):
        ni = i + (di[k]*move)
        nj = j + (dj[k]*move)

        ret = dfs(ni,nj)

        if ret == -1: #이 방향으로 보낸게 무한루프라면
            return -1

        # print(ni,nj,max_result)

        max_result = max(max_result, ret+1)
    DP[i][j] = max_result
    visited[i][j] = False

    return max_result

print(dfs(0,0))

for _ in range(N):
    print(DP[_])