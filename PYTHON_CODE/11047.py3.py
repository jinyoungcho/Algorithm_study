N, K = list(map(int,input().split()))

arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

cnt = 0

for i in arr:
    # print("가치",i)
    if i <= K:
        num_coin = K // i
        remain = K % i

        cnt += num_coin
        K = remain

        # print(num_coin, remain, cnt,K)

print(cnt)