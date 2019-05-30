from collections import*

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(q):
    while q:
        x,y,f=q.popleft()
        for i in range(4):
            nx, ny = x+dx[i] , y+dy[i]
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 :
                if f==1:
                    return visit[x][y]+1
                else:
                    continue
            if visit[nx][ny]!=-1 or arr[nx][ny]!='.':continue
            visit[nx][ny]=visit[x][y]+1
            q.append((nx,ny,f))
    return 'IMPOSSIBLE'  
for testCase in range(int(input())):
    m,n=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(input())
    q=deque()
    visit=[[-1]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j]=='*':
                q.append((i,j,0))
                visit[i][j]=0
            elif arr[i][j]=='@':
                s=(i,j,1)
                visit[i][j]=0
    q.append(s)
    print(bfs(q))