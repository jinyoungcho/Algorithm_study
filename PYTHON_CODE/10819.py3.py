N = int(input())
li = list(map(int,input().split()))

from itertools import permutations

MAXI = 0

for perm in permutations(li):
    # print(perm)
    temp = 0
    for i in range(N-1):
        # print(i,i+1)
        temp += abs(perm[i] - perm[i+1])

    # print(temp)
    MAXI=max(temp,MAXI)

print(MAXI)