# https://www.acmicpc.net/problem/11048

# dynamic programming!

# 처음엔 dfs로 시도했지만 시간초과,,

# 간단하게 dp로 접근할수 있으면 dp로 풀어봅시다

N,M = list(map(int,input().split()))

MAP = []

for _ in range(N):
    MAP.append(list(map(int,input().split())))



DP = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):

        if 0 <= i-1 and 0 <= j-1:
            A,B,C = DP[i-1][j],DP[i][j-1],DP[i-1][j-1]
        elif 0 == i and j > 0:
            A,B,C = 0,DP[i][j-1],0
        elif j == 0 and i > 0:
            A,B,C = DP[i-1][j],0,0
        elif i == 0 and j == 0:
            A,B,C = 0,0,0
        # else:
            # print("~?",i,j)
        # print(i,j, A,B,C)
        # print(i,j)
        # print(A,B,C)
        DP[i][j] = MAP[i][j] + max(A,B,C)

        # print(DP[i][j])

# for _ in range(N):
#     print(DP[_])

print(DP[N-1][M-1])