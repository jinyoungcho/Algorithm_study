from collections import deque

R, C = map(int, input().split())
a = [list(map(str,list(input()))) for _ in range(R)]

water = []
obs = []
start = (0,0)
goal = (0,0)
w_a = [[-1 for i in range(C)] for j in range(R)]
di = [1,-1,0,0]
dj = [0,0,1,-1]

check_goal = True
check_water = True
check_start = True

for i in range(R):
    for j in range(C):
        if a[i][j] == "*":
            water.append((i,j))
            check_water = False
            
        elif a[i][j] == "X":
            obs.append((i,j))
        elif a[i][j] == "D":
            goal = (i,j)
            check_goal = False
        elif a[i][j] == "S":
            start = (i,j)
            check_start = False
            
        if a[i][j] == "." or a[i][j] == "S":
            w_a[i][j] = 0
        elif a[i][j] == "*":
            w_a[i][j] = 1

if check_water == True:
    for i in range(R):
        for j in range(C):
            w_a[i][j] = 100000
else:


    q = deque()


    for kk in water:
        q.append((kk[0],kk[1]))


    while q:
        i,j = q.popleft()
        for k in range(4):
            ii = i + di[k]
            jj = j + dj[k]

            if 0 <= ii < R and 0 <= jj < C:
                if w_a[ii][jj] == 0:
                    w_a[ii][jj] = w_a[i][j]+1
                    q.append((ii,jj))



    w_a[goal[0]][goal[1]] = 100000

    
dist = [[0 for i in range(C)]for j in range(R)]

for i in range(R):
    for j in range(C):
        if a[i][j] == "X" or a[i][j] == "*" :
            dist[i][j] = -1
        elif a[i][j] == "S":
            dist[i][j] = 1
    
    
q2 = deque()

q2.append(start)

while q2:
    i,j = q2.popleft()
    
    for k in range(4):
        ii = i + di[k]
        jj = j + dj[k]
        
        if 0 <= ii < R and 0 <= jj < C:
            if dist[ii][jj] == 0 and (dist[i][j]+1 < w_a[ii][jj] or w_a[ii][jj]==0 ) :
                dist[ii][jj] = dist[i][j] + 1
                q2.append((ii,jj))

if check_goal == True or check_start == True:
    print("KAKTUS")              
elif dist[goal[0]][goal[1]] != 0:
    print(dist[goal[0]][goal[1]] -1)
elif dist[goal[0]][goal[1]] == 0:
    print("KAKTUS")