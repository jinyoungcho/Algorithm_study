A,B,C = list(map(int,input().split()))

table = [0] * 101

for _ in range(3):
    f,t = list(map(int,input().split()))

    for __ in range(f,t):

        table[__] += 1

# print(table[:10])

ans = 0

for _ in table:

    if _ == 0:
        continue
    elif _ == 1:
        ans += A
    elif _ == 2:
        ans += (B*2)
    elif _ == 3:
        ans += (C*3)

print(ans)