N = int(input())

n = N
cnt = 0
while n > 0:
    l = len(str(n))
    if n == N:
        cnt+= (N - 10**(len(str(n))-1) +1) * l
    else:
        cnt+= (10**len(str(n)) - 10**(len(str(n))-1)) * l
    n = n // 10
print(cnt)