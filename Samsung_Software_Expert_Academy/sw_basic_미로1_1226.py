from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for _ in range(1,11):

    R,C = 16,16

    t = int(input())

    MAP = [list(map(int,input())) for _ in range(R)]

    ans = 0

    st = ()
    ed = ()

    check = [[False]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):

            if MAP[i][j] == 2:
                st = (i,j)
            elif MAP[i][j] == 3:
                ed = (i,j)

    def bfs(st):
        i,j = st

        q = deque()
        q.append((i,j))
        check[i][j] = True

        while(q):
            i, j = q.popleft()

            for k in range(4):
                ni,nj = i+di[k], j+dj[k]
                if not (0<= ni < R and 0 <= nj < C):
                    continue
                if MAP[ni][nj] == 1:
                    continue
                if check[ni][nj] == True:
                    continue
                check[ni][nj] = True
                q.append((ni,nj))
    bfs(st)

    if check[ed[0]][ed[1]]:
        ans = 1
    else:
        ans = 0
    print("#",end='')
    print(t, ans)