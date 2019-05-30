n = int(input()) #수열의 크기

s = list(map(int,input().split()))

d = [False for i in range(sum(s)+1)]

d[0] = True

from itertools import combinations

for i in range(1,len(s)+1):
    for j in combinations(s,r=i):
        d[sum(j)] = True
        
if all(d):
    print(len(d))
else:
    for idx,i in enumerate(d):
        if i == False:
            print(idx)
            break