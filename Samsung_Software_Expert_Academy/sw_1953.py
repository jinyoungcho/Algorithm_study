from collections import deque
T = int(input())
N, M, R, C, L = 0,0,0,0,0
MAP=[]
check=[]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def can(now,next,k):

    if k == 0: #동
        if now in [1,3,4,5]:
            if next in [1,3,6,7]:
                return True
            else:
                return False
        else:
            return False

    elif k == 1: #서
        if now in [1,3,6,7]:
            if next in [1,3,4,5]:
                return True
            else:
                return False
        else:
            return False

    elif k == 2: #남
        if now in [1,2,5,6]:
            if next in [1,2,4,7]:
                return True
            else:
                return False
        else:
            return False

    else: #북
        if now in [1,2,4,7]:
            if next in [1,2,5,6]:
                return True
            else:
                return False
        else:
            return False



def simulate():
    global N, M, R, C, L,MAP,check
    q = deque()
    check[R][C] = 1
    q.append((R,C))

    while(q):
        i,j = q.popleft()

        for k in range(4):

            ni, nj = i+di[k], j+dj[k]

            if 0 > ni or ni >=N or 0 >nj or nj >= M: continue

            if MAP[ni][nj] == 0: continue

            now = MAP[i][j]
            next = MAP[ni][nj]

            if can(now,next,k) == False: continue

            if check[ni][nj] > 0: continue

            check[ni][nj] = check[i][j]+1
            q.append((ni,nj))

    # print("--------")
    # for _ in range(N):
    #     print(check[_])

    temp = 0
    for i in range(N):
        for j in range(M):
            if 0 < check[i][j] <=L:
                temp+=1
    return temp

for t in range(1, T+1):

    N, M, R, C, L = list(map(int, input().split()))

    MAP = [list(map(int, input().split())) for _ in range(N)]
    check = [[0] * M for _ in range(N)]
    # print(MAP)

    ans = simulate()

    print("#",end="")
    print(t,ans)