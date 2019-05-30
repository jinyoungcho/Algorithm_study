w,h = map(int,input().split())

arr = [input() for _ in range(h)]

c = [[False] * w for i in range(h)]
dist = [[-1] * w for i in range(h)]
di = [1,-1,0,0]
dj = [0,0,1,-1]

from collections import deque

q = deque()

start_end=[]
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'C':
            start_end.append((i,j))

start = start_end[0]
end = start_end[1]

c[start[0]][start[1]] = True
dist[start[0]][start[1]] = 0

q.append(start)
while q:
    i,j = q.popleft()
    
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        while 0 <= ni < h and 0 <= nj < w:
            if arr[ni][nj] == '*':
                break
            
            if dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni,nj))
            ni += di[k]
            nj += dj[k]
            
            
print(dist[end[0]][end[1]]-1)