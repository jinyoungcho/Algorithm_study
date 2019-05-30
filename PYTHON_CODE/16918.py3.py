R,C,N = list(map(int,input().split()))
MAP = [input() for _ in range(R)]

MAP2 = [[0]*C for _ in range(R)]

from collections import deque



for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'O':
            MAP2[i][j] = 3


di = [1,-1,0,0]
dj = [0,0,1,-1]

for _ in range(N):

    if _ == 0:
        for i in range(R):
            for j in range(C):
                if MAP2[i][j]:
                    MAP2[i][j] -= 1
    else:

        boom_li = []

        for i in range(R):
            for j in range(C):
                if not MAP2[i][j]:
                    MAP2[i][j] = 3
                else:
                    MAP2[i][j] -= 1
                    if MAP2[i][j] == 0:
                        boom_li.append((i,j))

        for i, j in boom_li:
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]

                if 0 <= ni < R and 0<= nj < C:
                    MAP2[ni][nj] = 0



for i in range(R):
    for j in range(C):
        if MAP2[i][j] == 0:
            print(".",end="")
        else:
            print("O",end="")
    print("")