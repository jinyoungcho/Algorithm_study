
fst = list(map(int, input().split()))

snd = list(map(int, input().split()))

trd = list(map(int, input().split()))

fth = list(map(int, input().split()))

a = [fst,snd,trd,fth]

ans = 0
MAXI = 0
# print(a)
for i in range(4):



    ans -= a[i][0]
    ans += a[i][1]

    MAXI = max(ans,MAXI)

print(MAXI)