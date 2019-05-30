N = int(input())

Arr = list(map(int, input().split()))
Brr = list(map(int, input().split()))


Arr=sorted(Arr,reverse=True)
Brr=sorted(Brr)

ans = 0

for _ in range(N):
    ans += Arr[_]*Brr[_]

print(ans)