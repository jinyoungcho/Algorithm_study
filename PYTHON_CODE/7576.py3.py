M, N = map(int, input().split())

a = []
for _ in range(N):
    a.append(list(map(int, input().split())))
    
c = [[False for i in range(M)] for j in range(N)]

from collections import deque
q = deque()

finished=[]
for i in range(N):
    for j in range(M):
        if a[i][j]==1:
            finished.append((i,j))
            
def bfs(li):
    i_li = [i[0] for i in li]
    j_li = [j[1] for j in li]
    
    for i in li:
        c[i[0]][i[1]] = True 
        q.append((i[0],i[1]))
    
    di = [-1,1,0,0]
    dj = [0,0,1,-1]
    
    while q:
        ii,jj = q.popleft()
        
        for k in range(4):
            iii = ii + di[k]
            jjj = jj + dj[k]
            
            if 0 <= iii < N and 0<= jjj < M:
                if a[iii][jjj] == 0 and c[iii][jjj] == False:
                    c[iii][jjj] = True
                    a[iii][jjj] = a[ii][jj] + 1
                    
                    q.append((iii,jjj))
    return a

bfs(finished)

ccc = True
for li in a:
    if 0 in li:
        print(-1)
        ccc= False
        break
        
if ccc == True:
    print(max(max(i) for i in a ) -1)
