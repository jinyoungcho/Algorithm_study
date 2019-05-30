
from collections import deque


N, M = map(int, input().split())

c2 =[0 for i in range(100001)]
c2[N] = 1

def bfs(s):
    cnt = 0
    q = deque()
    q.append(s)
    
    while q:
        s = q.popleft()
        s1 = s-1
        s2 = s+1
        s3 = 2*s

        if 0 <= s1 <100001 and c2[s1] == 0:
            c2[s1] = c2[s] + 1
            q.append(s1)

        if 0 <= s2 <100001 and c2[s2] == 0:
            c2[s2] = c2[s] + 1
            q.append(s2)

        if 0 <= s3 <100001  and c2[s3] == 0:
            c2[s3] = c2[s] + 1
            q.append(s3)
        
        if c2[M] != 0:
            return c2[M]
    
    return c2[M]
   
print(bfs(N)-1)

    