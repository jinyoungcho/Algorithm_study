N = int(input())

di = [0,0,0,1,-1]
dj = [0,1,-1,0,0]

MAP = []
check = [[False] * N for _ in range(N)]
for _ in range(N):
    MAP.append(list(map(int, input().split())))

# for i in range(1,N-1):
#     for j in range(1,N-1):
#
MINI = 10000
def dfs(cnt,cost):
    global MINI
    if cnt == 3:
        # print(cost,"~")
        # for _ in range(N):
        #     print(check[_])
        MINI = min(MINI, cost)
        return



    for i in range(1,N-1):
        for j in range(1,N-1):
            c = True
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]

                if check[ni][nj] == True:
                    c = False
                    break

            if c == True:

                sample_cost = 0
                for k in range(5):
                    ni = i + di[k]
                    nj = j + dj[k]
                    check[ni][nj] = True
                    sample_cost+= MAP[ni][nj]

                dfs(cnt + 1, cost + sample_cost)

                for k in range(5):
                    ni = i + di[k]
                    nj = j + dj[k]
                    check[ni][nj] = False

dfs(0,0)

print(MINI)