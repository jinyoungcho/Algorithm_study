from copy import deepcopy

N = int(input())

from collections import deque

MAP = [list(map(int,input().split())) for _ in range(N)]

di = [0,0,1,-1]
dj = [1,-1,0,0]

class Shark:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.size = 2
        self.eatten = 0


shark = Shark(0, 0)

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 9:
            shark = Shark(i,j)
            MAP[i][j] = 0

# check_for_copy=[[-1] * N for _ in range(N)]

ans = 0

while(True):

    check = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((shark.i,shark.j))
    check[shark.i][shark.j] = 0
    MAP[shark.i][shark.j] = 0
    can_eat = []
    temp_moved = 10000

    # print("--",shark.size,shark.eatten)
    # print(ans)
    # for _ in range(N):
    #     print(MAP[_])

    while(q):
        shark_i, shark_j = q.popleft()

        for k in range(4):
            ni = shark_i + di[k]
            nj = shark_j + dj[k]

            if not(0 <= ni < N and 0 <= nj < N):
                continue

            if MAP[ni][nj] > shark.size:
                continue

            if not check[ni][nj] == -1:
                continue

            check[ni][nj] = check[shark_i][shark_j]+1
            q.append((ni,nj))

            if 0 < MAP[ni][nj] < shark.size and check[ni][nj]:

                if temp_moved >= check[ni][nj]:
                    temp_moved = check[ni][nj]
                    can_eat.append((ni, nj, MAP[ni][nj],check[ni][nj]))

    if len(can_eat) == 0:
        break

    # print(can_eat)

    i_distance = -100000
    j_distance = 100000

    chosen_fish=[]

    for fish in can_eat:
        if shark.i - fish[0] > i_distance:
            i_distance = shark.i - fish[0]
            j_distance = shark.j - fish[1]
            chosen_fish = fish

        elif shark.i - fish[0] == i_distance:
            if shark.j - fish[1] > j_distance:
                i_distance = shark.i - fish[0]
                j_distance = shark.j - fish[1]
                chosen_fish = fish

    shark.i = chosen_fish[0]
    shark.j = chosen_fish[1]
    shark.eatten += 1
    ans += chosen_fish[3]
    if shark.eatten == shark.size:
        shark.size += 1
        shark.eatten = 0





print(ans)
