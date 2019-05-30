from copy import deepcopy
from collections import deque
di = [0,0,1,-1]
dj = [1,-1,0,0]

def other_clock_wise(c):
    ci = c[0]
    cj = c[1]

    q = deque()
    q.append(0)
    for j in range(1,C):
        q.append(MAP[ci][j])
        MAP[ci][j] = q.popleft()

    for i in range(ci-1,-1,-1):
        q.append(MAP[i][C-1])
        MAP[i][C-1] = q.popleft()

    for j in range(C-2,-1,-1):
        q.append(MAP[0][j])
        MAP[0][j] = q.popleft()

    for i in range(1,ci):
        q.append(MAP[i][cj])
        MAP[i][cj] = q.popleft()

def clock_wise(c):
    ci = c[0]
    cj = c[1]
    q = deque()
    q.append(0)

    for j in range(1,C):
        q.append(MAP[ci][j])
        MAP[ci][j] = q.popleft()
    # print(q)
    for i in range(ci+1,R):
        q.append(MAP[i][C-1])
        MAP[i][C-1] = q.popleft()
    # print(q)
    for j in range(C-2,-1,-1):
        q.append(MAP[R-1][j])
        MAP[R-1][j] = q.popleft()
    # print(q)
    for i in range(R-2,ci,-1):
        q.append(MAP[i][0])
        MAP[i][0] = q.popleft()

    # print(q)

def simulate():

    temp = 0

    for t in range(T):

        # copy_MAP = deepcopy(MAP)
        copy_B = deepcopy(B)

        for i in range(R):
            for j in range(C):
                if MAP[i][j] > 0:
                    cnt = 0

                    for k in range(4):
                        ni = i+di[k]
                        nj = j+dj[k]
                        if (ni,nj) not in cleaner and 0<= ni < R and 0<= nj < C:
                            cnt += 1
                            copy_B[ni][nj] += MAP[i][j] // 5
                    MAP[i][j] = MAP[i][j] - ((MAP[i][j]//5) * cnt)

        for i in range(R):
            for j in range(C):
                MAP[i][j] += copy_B[i][j]

        #cleaner
        other_clock_wise(cleaner[0])
        clock_wise(cleaner[1])





    for i in range(R):
        # print(MAP[i])
        temp += sum(MAP[i])
        # for j in range(C):
        #     if MAP[i][j] > 0:
        #         temp += MAP[i][j]

    return temp+2


R,C,T = list(map(int,input().split()))

MAP = [list(map(int,input().split())) for _ in range(R)]
B = [[0]*C for _ in range(R)]
cleaner = []

for i in range(R):
    for j in range(C):
        if MAP[i][j] == -1:
            cleaner.append((i,j))


ans = simulate()

print(ans)