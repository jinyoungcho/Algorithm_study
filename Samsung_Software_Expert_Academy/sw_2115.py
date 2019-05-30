T = int(input())
ans = 0
N,M,C = 4,2,13
MAP = []
MAXI1 = 0
MAXI2 = 0

def dfs_for_get_score2(li, capa ,index, score):
    global MAXI2
    # print("li: ",li, capa ,index, score)
    if index == len(li):
        if capa < 0:
            MAXI2 = max(MAXI2, 0)
        else:
            MAXI2 = max(MAXI2, score)
    else:
        #선택함
        if capa - li[index] >= 0:
            dfs_for_get_score2(li, capa-li[index], index+1,score + li[index] ** 2)
            #선택안함
            dfs_for_get_score2(li, capa, index + 1, score)
        else:
            dfs_for_get_score2(li, capa, index + 1, score)

def dfs_for_get_score1(li, capa ,index, score):
    global MAXI1
    # print("li: ",li, capa ,index, score)
    if index == len(li):
        if capa < 0:
            MAXI1 = max(MAXI1, 0)
        else:
            MAXI1 = max(MAXI1, score)
    else:
        #선택함
        if capa - li[index] >= 0:
            dfs_for_get_score1(li, capa-li[index], index+1,score + li[index] ** 2)
            #선택안함
            dfs_for_get_score1(li, capa, index + 1, score)
        else:
            dfs_for_get_score1(li, capa, index + 1, score)

# def dfs(i,j,cnt,index,first_list):
#     first_score = 0
#     if cnt == M: #2개를 전부 선택했다면
#         print(first_list)
#         first_score = dfs_for_get_score(first_list,C,0,0)
#         return first_score
#     else:
#         return dfs(i,j+1,cnt+1,index+1,first_list + [MAP[i][j]])


def simulate():
    global MAXI1
    global MAXI2
    global ans
    ans = 0

    for i in range(N):
        for j in range(N-M+1):
            f_li = MAP[i][j:j+M]
            MAXI1=0
            dfs_for_get_score1(f_li, C,0,0)
            # print(f_li,MAXI1)

            for ii in range(i,N):
                if i == ii and j + M <= N-M:
                    for jj in range(j+M,N-M+1):
                        MAXI2 = 0
                        s_li = MAP[ii][jj:jj + M ]
                        dfs_for_get_score2(s_li, C, 0, 0)
                        # print(s_li, MAXI2)
                elif i != ii:
                    for jj in range(N-M+1):
                        MAXI2 = 0
                        s_li = MAP[ii][jj:jj + M ]
                        dfs_for_get_score2(s_li, C, 0, 0)
                        # print(s_li, MAXI2)

                        ans = max(ans,MAXI1+MAXI2)



    # print(MAXIMI)






for t in range(1,T+1):
    ans = 0

    N, M, C = list(map(int, input().split()))

    MAP = [list(map(int, input().split())) for _ in range(N)]


    simulate()

    print("#",end="")
    print(t,ans)