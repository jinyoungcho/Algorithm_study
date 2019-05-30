R,C = list(map(int,input().split()))

MAP2 = [input() for _ in range(R)]

MAP = []

for i in range(R):
    sl = []
    for j in range(C):
        sl.append(MAP2[i][j])

    MAP.append(sl)

N = int(input())

bar = list(map(int,input().split()))

# print(bar)

for _ in range(N):
    bar[_] = R - bar[_]



check=[]

from collections import deque

di = [1,-1,0,0]
dj = [0,0,1,-1]

def bfs(i,j,n_cluster):
    q = deque()

    q.append((i,j))
    check[i][j] = n_cluster

    while(q):
        i,j = q.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if not (0<= ni< R and 0<= nj <C):
                continue

            if check[ni][nj] != 0:
                continue

            if MAP[ni][nj] == ".":
                continue

            check[ni][nj] = n_cluster
            q.append((ni,nj))

def get_cluster_with_bfs():
    cnt = 1
    for ii in range(R):
        for jj in range(C):
            if check[ii][jj] == 0 and MAP[ii][jj] == "x":
                # print(ii,jj,cnt)
                bfs(ii, jj, cnt)
                cnt += 1

    return cnt

def throw_bar(k,bar_i):

    if k == 0:

        for j in range(C):

            if MAP[bar_i][j] == "x":
                MAP[bar_i][j] = "."
                break

    elif k == 1:

        for j in range(C-1,-1,-1):

            if MAP[bar_i][j] == "x":
                MAP[bar_i][j] = "."
                break

def organize(cnt):

    max_c = cnt
    c_dic = {}



    for _ in range(1,max_c):
        c_dic[_] = False

    for j in range(C):
        if check[R-1][j] != 0:
            c_dic[check[R-1][j]] = True


    air_cluster = -1
    for _ in range(1,max_c):
        if c_dic[_] == False:
            air_cluster = _
            break

    if air_cluster == -1:
        return

    #공중 군집 범위찾기

    air_range = []
    for i in range(R):
        for j in range(C):
            if check[i][j] == air_cluster:
                air_range.append(j)

    min_air_range = min(air_range)
    max_air_range = max(air_range)




    MINI = R

    for j in range(min_air_range, max_air_range+1):


        air_i = R-1

        bottom_i = R - 1

        for i in range(R-1,-1,-1):

            if check[i][j] == air_cluster:
                air_i = i
                MINI = min(MINI,bottom_i - air_i)

                break

            elif check[i][j] != 0:
                bottom_i = i-1


    # print("~~~~~")
    for j in range(min_air_range, max_air_range+1):
        for i in range(R-1,-1,-1):
            # print(i,j)
            if check[i][j] == air_cluster:
                MAP[i+MINI][j] = "x"
                MAP[i][j] = "."

def simulate():
    global check
    for idx, bar_i in enumerate(bar):
        check = [[0] * C for _ in range(R)]

        # print("-before")
        # for _ in range(R):
        #     print(MAP[_])
        #
        # print(bar_i)

        if idx % 2 == 0:
            #왼쪽
            throw_bar(0,bar_i)

        else:
            #오른쪽
            throw_bar(1,bar_i)



        cnt = get_cluster_with_bfs()

        if cnt == 1:
            continue

        # print("-after")
        organize(cnt)

        # for _ in range(R):
            # print(check[_], MAP[_])

simulate()

for _ in range(R):
    for j in range(C):
        print(MAP[_][j],end="")
    print("")