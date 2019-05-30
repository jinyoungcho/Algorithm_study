import copy
from collections import deque

n = int(input())
a = []
for _ in range(n):
    a.append(
    list(map(int,input().split(" ")))
    )
def dfs(_a,idy):
    
    if idy == 5: #5번까지 돌았으면
        ans = 0
        for i in range(n):
            ans = max(ans,max(_a[i]))
        return ans
    
    ans = 0
    
    #남
    b = copy.deepcopy(_a) #현재 map복사
    q = deque()
    for j in range(n):
        for i in range(n-1,-1,-1):
            if b[i][j] != 0:
                q.append(b[i][j])
                b[i][j]=0
        idx=n-1
        while q:
            now = q.popleft()
            if b[idx][j] == 0:
                b[idx][j] = now
            elif b[idx][j] == now:
                b[idx][j] *= 2
                idx -= 1
            else:
                idx -= 1
                b[idx][j] = now

    ans=max(ans,dfs(b,idy+1))
    
    #북
    b = copy.deepcopy(_a) #현재 map복사
    q = deque()
    for j in range(n):
        for i in range(n):
            if b[i][j] != 0:
                q.append(b[i][j])
                b[i][j]=0        
        idx=0
       
        while q:
            now = q.popleft()
            if b[idx][j] == 0:
                b[idx][j] = now
            elif b[idx][j] == now:
                b[idx][j] *= 2
                idx += 1
            else:
                idx += 1
                b[idx][j] = now
    ans=max(ans,dfs(b,idy+1))
    
    #서
    b = copy.deepcopy(_a) #현재 map복사
    q=deque()
    for i in range(n):
        for j in range(n):
            if b[i][j] != 0:
                 q.append(b[i][j])
            b[i][j] = 0 
        idx = 0
        while q:
            now = q.popleft()
            if b[i][idx] == 0:
                b[i][idx] = now
               
            elif b[i][idx] == now:
                b[i][idx] *= 2
                idx+=1
            else: #0도 아니고 다른 숫자면
                idx+=1
                b[i][idx] = now
    ans=max(ans,dfs(b,idy+1))
    
    #동
    b = copy.deepcopy(_a) #현재 map복사
    q=deque()
    for i in range(n):
        for j in range(n-1,-1,-1):
            if b[i][j] != 0:
                q.append(b[i][j])
                b[i][j] = 0
        idx = n-1
        while q:
            now = q.popleft()
            if b[i][idx] == 0:
                b[i][idx] = now
               
            elif b[i][idx] == now:
                b[i][idx] *= 2
                idx-=1
            else: #0도 아니고 다른 숫자면
                idx-=1
                b[i][idx] = now
    ans=max(ans,dfs(b,idy+1))
    return ans

print(dfs(a,0))