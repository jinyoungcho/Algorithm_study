from collections import deque

n = int(input())

dist = [[-1]*(n+1) for _ in range(n+1)]

q = deque()

q.append((1,0))

dist[1][0] = 0

#key = (screen , clip_borad)
#value = (step)

while q:
    s,c = q.popleft()
    
    if dist[s][s] == -1: #화면에 있는 복사해서 클립보드에 붙여 넣기
        dist[s][s] = dist[s][c] + 1
        
        q.append((s,s))
    
    
    if s+c <= n and dist[s+c][c] == -1: # 클립보드를 화면에 표시하기
        dist[s+c][c] = dist[s][c] + 1
        
        q.append((s+c,c))
        
    if s-1 >= 0 and dist[s-1][c] == -1 :
        dist[s-1][c] = dist[s][c] + 1
        
        q.append((s-1,c))
        
print(min(dist[n][1:]))