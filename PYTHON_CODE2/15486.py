# https://www.acmicpc.net/problem/15486

# 퇴사 2

N = int(input())

time=[]
price=[]

for _ in range(N):

    t,p = list(map(int,input().split()))

    time.append(t)
    price.append(p)

MAXI = 0

DP = [0] * (N+1)

temp = 0
for now in range(N):

    # now = 일하는 날

    end = now + time[now]

    temp = max(temp, DP[now]) #현재시점 까지 받은 최대 돈

    # end = 돈 받는 날

    if end > N: #퇴사날에 다다른다면 #해당 일을 할 수 없다
        continue

    DP[end] = max(temp + price[now], # 현재시점까지 받은 돈 +
                                     # 해당 일을 함으로써 받을 돈
                  DP[end])    # vs     돈받는 날까지 받을 돈

    # print(DP[end])

print(max(DP))

# print(temp)
#
# print(DP[-1])

