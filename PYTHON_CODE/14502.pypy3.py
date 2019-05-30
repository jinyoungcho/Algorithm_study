import copy

R, C = list(map(int, input().split()))

virus = []

MAP = []

check_for_copy = [[False]*C for _ in range(R)]

for i in range(R):
    MAP.append(list(map(int, input().split())))
    for j in range(C):
        if MAP[i][j] == 2:
            virus.append([i, j])
        if MAP[i][j] == 1:
            check_for_copy[i][j] = True

from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs(wall):

    q = deque()

    q.extend(virus)

    check = copy.deepcopy(check_for_copy)

    for i,j in virus:
        check[i][j] = True
    for i,j in wall:
        check[i][j] = True

    # print("before")
    # for _ in range(R):
    #     print(check[_])

    # print("start")
    while(q):

        i,j = q.popleft()

        for k in range(4):

            ni,nj = i+di[k], j+dj[k]

            if not ( 0<= ni < R and 0 <= nj < C ):
                continue

            if check[ni][nj]:
                continue

            check[ni][nj] = True
            q.append([ni,nj])

    # print("after")
    # for _ in range(R):
    #     print(check[_])

    temp = 0
    for i in range(R):
        for j in range(C):
            if check[i][j] == False:
                temp += 1
    return temp

# print(bfs([[0, 1], [0, 2], [0, 3]]))

ans = 0

def dfs_with_bfs(cnt,wall):
    # print(wall)
    global ans
    if cnt == 3:

        temp_ans = bfs(wall)
        # print(temp_ans)
        ans = max(temp_ans, ans)

        return



    for i in range(R):
        for j in range(C):
            if MAP[i][j] == 0:
                MAP[i][j] = 1
                dfs_with_bfs(cnt + 1, wall + [[i,j]])
                MAP[i][j] = 0

dfs_with_bfs(0,[])

print(ans)