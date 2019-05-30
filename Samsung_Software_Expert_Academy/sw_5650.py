#input
T = int(input())

N = 0
G = []
check=[]
ans = 0
check2 = set()

di = [0, 0, 1, -1]
dj = [1, -1 ,0 ,0]

warm_hole_index_ij_dic = {}
warm_hole_ij_nij_dic = {}
# fuctions
def start_simulate(index_i, index_j, direction):
    # print("게임시작: ", index_i, index_j, direction)
    i = index_i
    j = index_j
    k = direction
    temp_ans = 0

    ni = i
    nj = j
    while(True):


        # step1 이동
        ni = ni+di[k]
        nj = nj+dj[k]
        # 벽이라면
        if nj < 0 or nj >= N or ni < 0 or ni >= N:
            temp_ans = temp_ans + 1
            if k == 0 or k == 1:
                k = (k+1) % 2
            elif k == 2 or k == 3:
                k = 2 if k == 3 else 3

            continue
        elif G[ni][nj] == -1:
            break;
        ## 블록
        elif 1 <= G[ni][nj] <= 5:
            temp_ans = temp_ans + 1
            if G[ni][nj] == 5:
                if k == 0 or k == 1:
                    k = (k + 1) % 2
                elif k == 2 or 3:
                    k = 2 if k == 3 else 3

            # 1
            elif G[ni][nj] == 1:
                if k == 0:
                    k = 1
                elif k == 1:
                    k = 3
                elif k == 2:
                    k = 0
                elif k == 3:
                    k = 2

            elif G[ni][nj] == 2:
                if k == 0:
                    k = 1
                elif k == 1:
                    k = 2
                elif k == 2:
                    k = 3
                elif k == 3:
                    k = 0

            elif G[ni][nj] == 3:
                if k == 0:
                    k = 2
                elif k == 1:
                    k = 0
                elif k == 2:
                    k = 3
                elif k == 3:
                    k = 1

            elif G[ni][nj] == 4:
                if k == 0:
                    k = 3
                elif k == 1:
                    k = 0
                elif k == 2:
                    k = 1
                elif k == 3:
                    k = 2
        ## 웜홀!
        elif 6 <= G[ni][nj] <= 10:
            ni, nj = warm_hole_ij_nij_dic[(ni,nj)]



        #방문했었으면
        # print("after", ni, nj, k)

        # if check[ni][nj][k][temp_ans] == True:
        if (ni,nj,k,temp_ans) in check2:
            # print("게임오버: ", index_i, index_j, direction)
            break
        else:
            check2.add((ni,nj,k,temp_ans))

        #같은곳으로 돌아왔으면
        if ni==i and nj==j:
            # print("게임오버: ", index_i, index_j, direction)
            break


    return temp_ans




# main

for t in range(T):

    N = int(input())
    ans = 0
    check2 = set()
    # check = [[[[False] * 1000 for dir in range(4)] for _ in range(N)] for __ in range(N)]
    G = []
    warm_hole_ij_nij_dic = {}
    warm_hole_index_ij_dic = {}

    for i in range(N):
        G.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            if 6 <= G[i][j] <=10:
                if G[i][j] in warm_hole_index_ij_dic.keys():
                    warm_hole_ij_nij_dic[(i,j)] = warm_hole_index_ij_dic[G[i][j]]
                    warm_hole_ij_nij_dic[warm_hole_index_ij_dic[G[i][j]]] = (i,j)
                else:
                    warm_hole_index_ij_dic[G[i][j]] = (i,j)


    # print(warm_hole_ij_nij_dic)


    # start_simulate(0,2,1)

    for index_i, i_li in enumerate(G):

        for index_j, ij_element in enumerate(i_li):
            if ij_element == 0:
                for direction in range(4):

                    # if check[index_i][index_j][direction][0] == False:
                    if (index_i, index_j, direction, 0) not in check2:
                        ans = max(ans,start_simulate(index_i, index_j, direction))
                        # print("gd")


    print("#",end="")
    print(t+1,ans)

