
from collections import deque





T = int(input())
N,M,K = 0,0,0 # N 격자크기, M 시간, K 개 미생물

di = [0,-1,1,0,0] #1,2,3,4 상 하 좌 우
dj = [0,0,0,-1,1]

#1 -> 2, 2->1
#3 -> 4, 4->3

class Cell:
    def __init__(self,i,j,size,dir):
        self.i = i
        self.j = j
        self.size = size
        self.dir = dir

    def __repr__(self):
        return str(self.size)+","+str(self.dir)

def simulate():

    global cell_dic

    for _ in range(M):
        # print(_,"일")
        cell_q = deque()
        # print(cell_dic)
        #queue 에 넣기
        for i,j in list(cell_dic.keys()):

            cell_q.append(cell_dic[(i,j)])

            del cell_dic[(i,j)]

        cell_q = deque(sorted(cell_q,key=lambda cell:cell.size,reverse=True))

        # print(cell_q)
        while(cell_q):
            cell = cell_q.popleft()

            cell.i += di[cell.dir]
            cell.j += dj[cell.dir]

            if cell.i == 0 or cell.j == 0 or cell.i == N-1 or cell.j == N-1:

                cell_size = int(cell.size/2)

                if cell_size == 0: continue

                cell.size = cell_size

                if cell.dir == 1:
                    cell.dir = 2
                elif cell.dir == 2:
                    cell.dir = 1
                elif cell.dir == 3:
                    cell.dir = 4
                elif cell.dir == 4:
                    cell.dir = 3

                cell_dic[(cell.i, cell.j)] = cell

            else:

                if (cell.i,cell.j) in cell_dic:

                    pre_cell = cell_dic[(cell.i,cell.j)]


                    if pre_cell.size < cell.size:
                        pre_cell.dir = cell.dir

                    pre_cell.size += cell.size


                else:
                    cell_dic[(cell.i,cell.j)] = cell

    temp = 0
    for i,j in cell_dic.keys():
        temp += cell_dic[(i,j)].size


    return temp







for t in range(1,T+1):

    N, M, K = list(map(int, input().split()))


    cell_dic = {}

    ans = 0

    for _ in range(K):
        i, j, num, dir = list(map(int, input().split()))
        cell_dic[(i,j)] = Cell(i,j,num,dir)

    ans = simulate()

    print("#",end="")
    print(t, ans)