T = int(input())

di = [0,0,1,-1]
dj = [1,-1,0,0]

class Cell:
    def __init__(self,y,x,h,nh):
        self.y = y
        self.x = x
        self.h = h
        self.nh = nh

    def __repr__(self):
        return str(self.h)+","+str(self.nh)

from collections import deque

for t in range(1,T+1):

    N,M,K = list(map(int,input().split()))

    MAP = [list(map(int,input().split())) for _ in range(N)]

    not_active_q = deque()
    active_q = deque()
    MAP_dic = {}

    for i in range(N):
        for j in range(M):
            if MAP[i][j] >= 1:
                MAP_dic[(i,j)] = True
                not_active_q.append(Cell(i, j, int(MAP[i][j]), int(MAP[i][j])))

    for k in range(K):

        # print(active_q, not_active_q)

        len_not_active_q = len(not_active_q)

        will_active = []

        for _ in range(len_not_active_q):
            cell = not_active_q.popleft()

            cell.nh -= 1

            # print(cell)

            if cell.nh != 0:
                not_active_q.append(cell)

            else:
                cell.nh = int(cell.h)
                will_active.append(cell)

        will_not_active = []


        len_active_q = len(active_q)
        active_q = deque(sorted(active_q, key = lambda x: x.h, reverse=True))
        for _ in range(len_active_q):
            cell = active_q.popleft()

            if cell.nh == cell.h:

                for dir in range(4):
                    ny = cell.y + di[dir]
                    nx = cell.x + dj[dir]

                    if (ny, nx) not in MAP_dic:
                        MAP_dic[(ny, nx)] = True
                        will_not_active.append(Cell(ny,nx,int(cell.h),int(cell.h)))

            cell.nh -= 1

            if cell.nh != 0:
                active_q.append(cell)

        not_active_q += will_not_active
        active_q += will_active

    print("#",end="")
    print(t,len(not_active_q) + len(active_q))