di = [-1, 0, 1, 0] #상,우,하,좌
dj = [0, 1, 0, -1]
pr = 0
pc = 0
black_hole_li = []
inif = False
MAXI = 0
MAXI_dir = 0

import sys
# sys.setrecursionlimit(1000000)

def dfs(s_dir,i,j,k,cnt,visited):
    global black_hole_li, N,M, MAP, li_right_up, li_right_down, MAXI, inif, MAXI_dir

    # print(i,j,k,visited,li_right_up,li_right_down)

    if (i,j,k) in visited:
        MAXI_dir = s_dir
        inif = True
        return
    # print(i,j,k)
    # print(visited)
    visited.add((i,j,k))

    if (i,j) in black_hole_li or not (0 <= i < N and 0 <= j < M):

        if cnt > MAXI:
            MAXI_dir = s_dir
            MAXI = cnt

    else:
        nk = k
        ni = i
        nj = j
        if (i,j) in li_right_up:
            # print("!")
            if k == 0:
                nk = 1
            elif k == 1:
                nk = 0
            elif k == 2:
                nk = 3
            elif k == 3:
                nk = 2

        elif (i,j) in li_right_down:

            if k == 0:
                nk = 3
            elif k == 1:
                nk = 2
            elif k == 2:
                nk = 1
            elif k == 3:
                nk = 0

        while(True):
            ni = ni + di[nk]
            nj = nj + dj[nk]
            cnt += 1
            # print(ni,nj)

            if not (0 <= ni < N and 0 <= nj < M):
                break

            if (ni, nj) in li_right_up or (ni, nj) in li_right_down or (ni, nj) in black_hole_li:
                # print("~")
                break

        dfs(s_dir, ni, nj, nk, cnt, visited)

def simulate():
    global pr,pc,MAXI,MAXI_dir

    dictt = {0:"U",1:"R",2:"D",3:"L"}

    for _ in range(4):
        dfs(_,pr,pc,_,0,set())
        if inif == True:
            MAXI = "Voyager"
            break

    print(dictt[MAXI_dir])
    print(MAXI)


N,M = list(map(int,input().split()))
MAP = []

for _ in range(N):
    MAP.append(input())

pr,pc = list(map(int,input().split()))

pr -= 1
pc -= 1

black_hole_li = []

li_right_up = []
li_right_down = []

# print(MAP)

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'C':
            black_hole_li.append((i,j))

        elif MAP[i][j] == "/":
            li_right_up.append((i,j))

        elif ord(MAP[i][j]) == 92:
            li_right_down.append((i,j))


simulate()


