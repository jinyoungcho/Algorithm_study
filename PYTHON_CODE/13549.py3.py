N, M = map(int, input().split())
c = [0 for i in range(100001)]
c[N] = 1

from collections import deque


def bfs(s):
    
    q = deque()
    q.append(N)
    next_q = deque()
    
    while q:
        s = q.popleft()
    
        if s*2 < 100001 and c[s*2] == 0:
            q.append(s*2)
            c[s*2] = c[s] 
        if s-1 >= 0 and c[s-1] == 0:
            next_q.append(s-1)
            c[s-1] = c[s]+1
        if s+1 < 100001 and c[s+1] == 0:
            next_q.append(s+1)
            c[s+1] = c[s]+1

        if not q:
            q = next_q
            
        
    return c[M]

print(bfs(N)-1)