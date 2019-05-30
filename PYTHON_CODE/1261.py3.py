from collections import deque

M, N = map(int, input().split())

a = [list(map(int,list(input()))) for _ in range(N)]
# for _ in range(N):
#     a.append(list(map(int, input().split())))
    
q = deque()
c = [
    [False for j in range(M)] for i in range(N)
]



q.append((0,0))
c[0][0] = True


while q:
    i,j = q.popleft()
    di = [-1,1,0,0]
    dj = [0,0,1,-1]

    for k in range(4):
        ii = i+di[k]
        jj = j+dj[k]
        
        
        
        if 0 <= ii < N and 0 <= jj < M:

            if c[ii][jj] == False and a[ii][jj] == 0:
                c[ii][jj] = True
                q.appendleft((ii,jj))

                a[ii][jj] = a[i][j]

            if c[ii][jj] == False and a[ii][jj] == 1:
                c[ii][jj] = True
                q.append((ii,jj))
                a[ii][jj] = a[i][j]+1

print(a[N-1][M-1])