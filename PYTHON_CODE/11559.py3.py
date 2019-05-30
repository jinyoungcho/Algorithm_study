N = 12
M = 6

MAP = []

for _ in range(N):
    MAP.append(list(input()))

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

from collections import deque

def bfs(i, j, block):

    q = deque()
    q.append((i, j, block))
    check[i][j] = 1


    will_boom_li = [(i, j)]

    while(q):

        i, j, shape = q.popleft()

        for k in range(4):

            ni = i + di[k]
            nj = j + dj[k]

            if not ( 0<= ni < N and 0 <= nj < M):
                continue

            if MAP[ni][nj] != shape:
                continue

            if check[ni][nj] != 0:
                continue

            will_boom_li.append((ni, nj))

            check[ni][nj] = check[i][j] + 1

            q.append((ni, nj, shape))


    if len(will_boom_li) >= 4:
        return will_boom_li

    else:
        return False

def delete(delete_list):

    for li in delete_list:
        for i,j in li:
            MAP[i][j] = '.'

    # print("before")
    # for i in range(N):
    #     for j in range(M):
    #         print(MAP[i][j],end='')
    #     print()

def organize():


    for j in range(M):
        q = deque()
        for i in range(N-1,-1,-1):
            if MAP[i][j] != '.':
                q.append((MAP[i][j]))
                MAP[i][j] = '.'

        i = N-1
        while(q):
            MAP[i][j] = q.popleft()
            i-=1

    # print("after")
    # for i in range(N):
    #     for j in range(M):
    #         print(MAP[i][j],end='')
    #     print()

ans = 0

while(True):

    find = False

    let_me_check=[]

    check = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == '.':
                continue
            elif check[i][j] == 0:
                res = bfs(i, j, MAP[i][j])
                if res != False:
                    find = True
                    let_me_check.append(res)


    if find == False:
        break
    delete(let_me_check)
    ans += 1

    organize()


print(ans)