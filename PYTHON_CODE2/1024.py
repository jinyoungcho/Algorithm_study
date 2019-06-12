N,L = list(map(int,input().split()))

# arr = [1,2,3,4,5,6,7,8,9]

from itertools import combinations
x = -1
iter = -1
for _ in range(L,101):
    t = (_-1)*_ // 2

    if (N-t) % _ == 0 and (N-t)// _ >= 0:
        x = (N-t) // _
        iter = _
        break

# print(iter)

if x == -1:
    print(x)
else:
    for _ in range(iter):
        print(x+_,end=' ')