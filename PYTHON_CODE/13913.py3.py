import sys
sys.setrecursionlimit(200000)

n,k = map(int,input().split())

c = [-1] * 200000
sequence = []

via = [-1] * 200000

from collections import deque, defaultdict

q = deque()

q.append(n)
c[n] = 0

sequence = defaultdict(lambda : [n])

while q:
    
    x = q.popleft()
    
    xi = x+1
    xy = x-1
    xk = x*2
    
    if xi < len(c) and c[xi] == -1:
        c[xi]=c[x]+1
        q.append(xi)
        sequence[xi].append(xi)
        via[xi] = x
    
    if xy >= 0 and c[xy] == -1:
        c[xy]=c[x]+1
        q.append(xy)
        sequence[xy].append(xy)
        via[xy] = x
        
    if 0 <= xk and xk <len(c) and c[xk] == -1:
        c[xk]=c[x]+1
        q.append(xk)
        sequence[xk].append(xk)
        via[xk] = x
        
def get_route(kk):
    if via[kk] == -1:
        return
    else:
        route.append(via[kk])
        get_route(via[kk])
        
route = [k]
get_route(k)
route.reverse()

print(c[k])
for i in route:
    print(i, end=' ')