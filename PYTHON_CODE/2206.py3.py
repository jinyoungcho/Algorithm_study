from collections import deque

N, M = map(int, input().split())
a = [list(map(int,list(input()))) for _ in range(N)]

dist = [[[0]*2 for j in range(M)] for i in range(N)]
q = deque()
q.append((0,0,0))
dist[0][0][0] = 1
di = [1,-1,0,0]
dj = [0,0,1,-1]
while q:
    
    i,j,z = q.popleft()
    for k in range(4):
        ii = i + di[k]
        jj = j + dj[k]
        zz = z
        if 0 <= ii < N and 0 <= jj < M:
            if a[ii][jj] == 0 and dist[ii][jj][zz] == 0:
                dist[ii][jj][zz] = dist[i][j][z] + 1
                q.append((ii,jj,zz))
            if zz == 0 and a[ii][jj] == 1 and dist[ii][jj][zz+1] == 0:
                dist[ii][jj][zz+1] = dist[i][j][z] + 1
                q.append((ii,jj,zz+1))
            
if dist[N-1][M-1][0] != 0 and dist[N-1][M-1][1]  != 0:
    print(min(dist[N-1][M-1]))
elif dist[N-1][M-1][0] != 0:
    print(dist[N-1][M-1][0])
elif dist[N-1][M-1][1] != 0:
    print(dist[N-1][M-1][1])
else:
    print(-1)