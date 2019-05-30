T = int(input())
N,K = 0,0
MAP = []
check = []
di=[0,0,1,-1]
dj=[1,-1,0,0]
start_list=[]
answer = 0

#function

# def cut_peek():


def find_start():
    highest = -100
    start_list = []
    for i in range(N):
        for j in range(N):
            highest = max(highest, MAP[i][j])
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == highest:
                start_list.append((i, j))
    return start_list


def dfs(i,j,dir,len_r):
    global answer

    check[i][j] = True
    ni = i + di[dir]
    nj = j + dj[dir]

    if ni < 0 \
            or ni >= N \
            or nj < 0 \
            or nj >= N \
            or check[ni][nj] == True \
            or MAP[i][j] <= MAP[ni][nj]:
        # print("break")
        answer = max(len_r,answer)
        return 0

    # print(i, j, dir, len_r)

    for _dir in range(4):
        dfs(ni,nj,_dir,len_r+1)

    check[ni][nj] = False

    return

def simulate():

    global start_list
    global check
    #아무것도 안깍은 상태

    start_list = find_start()

    for i,j in start_list:
        for k in range(4):
            dfs(i,j,k,0)

    #하나하나씩 깍고나서 dfs

    for i in range(N):
        for j in range(N):
            for d in range(1,K+1):
                MAP[i][j] -= d

                # for __ in range(N):
                #     print(MAP[__])

                # print(start_list)
                for ii,jj in start_list:
                    for k in range(4):
                        # print("첫시작", ii,jj,k)
                        check = [[False]*N for _ in range(N)]
                        dfs(ii,jj,k,0)
                MAP[i][j] += d





# main

for t in range(1,T+1):

    N,K = list(map(int,input().split()))

    MAP = [list(map(int,input().split())) for _ in range(N)]


    check = [[False]*N for _ in range(N)]

    answer = 0

    simulate()

    print("#",end="")
    print(t,answer+1)