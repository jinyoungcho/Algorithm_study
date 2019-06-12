N = int(input())

DP = [0 for _ in range(N+1)]

MAP = []


MAP.append(0)
for _ in range(N):
    MAP.append(int(input()))


DP[0] = MAP[0]
DP[1] = MAP[0]+MAP[1]
DP[2] = max(MAP[0]+MAP[2], MAP[1]+MAP[2])

for i in range(3,N+1):
    DP[i] = max(DP[i-2]+MAP[i], MAP[i-1]+MAP[i] + DP[i-3])
                # i-1계단을 안밟음 vs i-2계단을 안밟음
print(DP[-1])