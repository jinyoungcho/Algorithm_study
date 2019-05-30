from collections import deque
MAX = 100000
n,k = list(map(int,input().split()))

check = [-1] * (MAX+1)
ans = [-1] * (MAX+1)

q = deque()
q.append(n)
check[n] = 0
ans[n] = 1
while q:
    s = q.popleft()
    
    s_li = [s+1, s-1, s*2]
    
    for ss in s_li:
        if 0 <= ss <= MAX:
            if check[ss] == -1: #한번도 들른적이 없다!
                q.append(ss)
                check[ss] = check[s]+1
                ans[ss] = ans[s]
            elif check[ss] == check[s]+1:
                ans[ss] += ans[s]
                
print(check[k])
print(ans[k])