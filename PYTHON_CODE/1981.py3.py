#이분탐색 + BFS

N = int(input())

MAP = []

for _ in range(N):
    MAP.append(list(map(int, input().split())))

MAXI = 0
MINI = 200
for i in range(N):
    for j in range(N):
        MAXI = max(MAXI, MAP[i][j])
        MINI = min(MINI, MAP[i][j])

from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(md):



    for cc in range(MINI,MAXI+1):
        check_route = [[1] * N for _ in range(N)]
        # print(cc,cc+md)
        for ii in range(N):
            for jj in range(N):
                if MAP[ii][jj] < cc:
                    check_route[ii][jj] = 1
                if cc <= MAP[ii][jj] <= cc+md:
                    check_route[ii][jj] = 0
                else:
                    check_route[ii][jj] = 1
        # print(md, "init", cc, MINI+md)
        # for _ in range(N):
        #     print(check_route[_])
        # print('')
        if check_route[0][0] == 1:
            continue
        if check_route[N-1][N-1] == 1:
            continue
        # if check_route[N-1][N-1] == True:
        #     return False

        check_route[0][0] = 2
        q = deque()
        q.append((0, 0))
        while(q):

            i, j = q.popleft()

            for k in range(4):

                ni, nj = i + di[k], j + dj[k]

                if not (0 <= ni < N and 0 <= nj < N):
                    continue

                if check_route[ni][nj] > 0:
                    continue

                check_route[ni][nj] = 2
                q.append((ni, nj))

        # print(md, check[N-1][N-1])
        # print(diff)
        # for _ in range(N):
        #     print(check_route[_])

        if check_route[N-1][N-1] == 2:
            return True

    return False

def binary_search_with_bfs(MINI,MAXI):
    global ans

    st = 0
    ed = MAXI-MINI

    while st <= ed:

        md = (st+ed)//2
        # print('~~~~~',st,ed,md)



        if bfs(md): #해당 diff로 가능하다? #더 낮춰서 해보자~
            # print('yes')
            # ans = md
            ed = md - 1
        else:       #해당 diff로 불가능하다? #돌려서 해보자~
            # print('no')
            st = md + 1


    return ed+1
# ans = 300
print(binary_search_with_bfs(MINI,MAXI))
# print(ans)


# 3
# 2 4 9
# 1 2 2
# 9 2 4