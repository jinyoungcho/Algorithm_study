from collections import deque
from itertools import product



A,B,C = list(map(int,input().split()))

s = C

check = [[False]*(C+1) for i in range(C+1)]

ans = [False] *(C+1)

cap = [A,B,C]
moves = []
for i in product([0,1,2],repeat=2):
    if i[0] != i[1]:
        moves.append(i)
        
q = deque()
q.append((0,0))
check[0][0] = True
ans[C] = True

while q:
    x,y = q.popleft()
    z = s - x - y
    
    cur = [x,y,z]
    
    for fr,to in moves:
        ncur = cur[:] #deep copy
        
        ncur[to] += ncur[fr]
        ncur[fr] = 0
        
        if ncur[to] >= cap[to]:
            ncur[fr] = ncur[to] - cap[to]
            ncur[to] = cap[to]
        
        if check[ncur[0]][ncur[1]] == False:
            check[ncur[0]][ncur[1]] = True
            q.append((ncur[0],ncur[1]))
            
            if ncur[0] == 0:
                ans[ncur[2]] = True
        
        
for idx,i in enumerate(ans):
    if i == True:
        print(idx, end=" ")
