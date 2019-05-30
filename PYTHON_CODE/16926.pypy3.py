N,M,R = list(map(int,input().split()))

MAP = [list(map(int,input().split())) for _ in range(N)]

# print(MAP)

# print("--",(N-1)//2, (M-1)//2)

from collections import deque

def dfs(sn, sm, n, m):
    global N
    #가장 바깥
    # print(sn, sm)
    if sn > ((N-1)//2) or sm > ((M-1)//2):
        return

    else:
        q = deque()

        q.append(MAP[sn][sm])

        for _ in range(sn+1,n):
            q.append(MAP[_][sm])
            MAP[_][sm] = q.popleft()

        for _ in range(sm,m+1):
            q.append(MAP[n][_])
            MAP[n][_] = q.popleft()

        # print(q)
        for _ in range(n-1,sn-1,-1):
            q.append(MAP[_][m])
            MAP[_][m] = q.popleft()

        for _ in range(m-1,sm-1,-1):
            q.append(MAP[sn][_])
            MAP[sn][_] = q.popleft()

        # print(q)

        dfs(sn+1,sm+1,n-1,m-1)

for _ in range(R):
    dfs(0,0,N-1,M-1)


for i in range(N):
    for j in range(M):
        print(MAP[i][j],end=" ")
    print()

