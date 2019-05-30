N,S,M = map(int,input().split())
V = list(map(int,input().split()))
D = [[0]*(M+1) for i in range(N+1)]
D[0][S] = 1
for i in range(N):
    for j in range(M+1):
        if D[i][j] == 1:
            if j-V[i] >= 0:
                D[i+1][j - V[i]] = 1
            if j+V[i] <= M:
                D[i+1][j + V[i]] = 1
ans = -1
for i in range(M+1):
    if D[N][i]:
        ans = i
print(ans)