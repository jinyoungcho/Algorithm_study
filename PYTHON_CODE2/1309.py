N = int(input())

# DP = [0] * (N+1)
DP = [0]*100002

DP[0]=1
DP[1]=3
DP[2]=7

for i in range(3,N+1):


    DP[i] = (DP[i-1]*2 + DP[i-2]) % 9901

# print(ans2)
print(DP[N])
# print(DP)