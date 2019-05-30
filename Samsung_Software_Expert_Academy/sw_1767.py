from copy import deepcopy

T = int(input())


di = [0,0,1,-1]
dj = [1,-1,0,0]

MAXI_cell = 0
MINI_score = 1000000
cell_list = []
MAP = []

def check(cell, k):
    i,j = cell
    can_connected =True
    while (True):
        i += di[k]
        j += dj[k]
        if not (0 <= i < N and 0 <= j < N):
            break
        if MAP[i][j] != 0:
            can_connected = False
            break
    return can_connected

def draw_map(cell, k):
    i,j = cell
    add_Score = 0
    while (True):
        i += di[k]
        j += dj[k]
        if not (0 <= i < N and 0 <= j < N):
            break

        MAP[i][j] = 2
        add_Score +=1

    return add_Score

def return_map(cell,k):

    # print("--")
    # for _ in range(N):
    #     print(MAP[_])

    if k == 0:

        for j in range(N-1,cell[1],-1):
            MAP[cell[0]][j] = 0

    elif k == 1:

        for j in range(0,cell[1]):
            MAP[cell[0]][j] = 0

    elif k == 2:

        for i in range(N-1,cell[0],-1):
            MAP[i][cell[1]] = 0

    elif k == 3:

        for i in range(0,cell[0]):
            MAP[i][cell[1]] = 0
    #
    # print("after--")
    # for _ in range(N):
    #     print(MAP[_])

def dfs(idx,cnt,score):
    global cell_list, MAXI_cell, MINI_score, MAP

    if idx == len(cell_list):

        # if cnt == 9:
        #     print("---")
        #     print(score, cnt)
        #     for _ in range(N):
        #         print(MAP[_])

        if cnt > MAXI_cell:
            MAXI_cell = cnt
            MINI_score = score
        elif cnt == MAXI_cell:

            MINI_score = min(score,MINI_score)

    else:

        if cell_list[idx][0] == 0 or cell_list[idx][0] == N-1 or cell_list[idx][1] == 0 or cell_list[idx][1] == N-1:
            dfs(idx+1, cnt+1, score)

        else:
            dfs(idx + 1, cnt, score)
            for k in range(4):

                if check(cell_list[idx],k):

                    temp_score = draw_map(cell_list[idx],k)

                    dfs(idx+1,cnt+1,score+temp_score)

                    return_map(cell_list[idx],k)

def simulate():
    num_core = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1:
                cell_list.append((i,j))
    dfs(0,0,0)


    return MINI_score

for t in range(1,T+1):
    N = int(input())
    MAXI_cell = 0
    MINI_score = 1000000
    cell_list = []
    MAP = [list(map(int, input().split())) for _ in range(N)]

    ans = simulate()

    print("#",end="")
    print(t,ans)