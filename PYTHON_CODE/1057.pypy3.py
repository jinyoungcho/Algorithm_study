N,S,G = list(map(int,input().split()))


arr = list(range(N))
# print(arr)
cnt = 0
done = False
while(S != G):
    S = S // 2 + S % 2
    G = G // 2 + G % 2
    cnt += 1

print(cnt)