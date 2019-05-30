N, M = list(map(int,input().split()))

MAP = []
for _ in range(N):
    MAP.append(list(map(int,input().split())))


DP=[[0]*M for _ in range(N)]

temp = 0

for i in range(N):
    if MAP[i][0] == 0:
        DP[i][0] = 1
        temp = 1
    else:
        DP[i][0] = 0

for j in range(M):
    if MAP[0][j] == 0:
        DP[0][j] = 1
        temp = 1
    else:
        DP[0][j] = 0

for i in range(1,N):
    for j in range(1,M):

        if MAP[i][j] == 0:

            DP[i][j] = min(DP[i-1][j-1],DP[i-1][j],DP[i][j-1])+1

            temp = max(temp, DP[i][j])

print(temp)