MAP = [list(map(int,input().split())) for _ in range(5)]

N,M = 5,5

di = [0,0,1,-1]
dj = [1,-1,0,0]

s = set()

def dfs(i,j,string, cnt):

    if cnt == 6:
        s.add(string)
        return

    else:

        # check[i][j] = True

        for k in range(4):

            ni = i+di[k]
            nj = j+dj[k]

            if not (0 <= ni < N and 0 <= nj < M):
                continue

            if check[ni][nj] == True:
                continue

            # print()
            dfs(ni,nj,string+str(MAP[ni][nj]),cnt+1)






for i in range(5):
    for j in range(5):

        check = [[False]* M for _ in range(N)]

        dfs(i,j,'',0)

print(len(s))