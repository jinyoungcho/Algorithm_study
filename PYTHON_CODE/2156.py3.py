n = int(input())
a = [0]    

for i in range(n):
    a.append( int(input()) )
    
d = [[0] * 3 for i in range(n+1)]

for i in range(1,n+1):
    d[i][0] = max(d[i-1][0],d[i-1][1],d[i-1][2])   # i번째 마시지 않은 것
    d[i][1] = d[i-1][0] + a[i]   # i번째 1번째로 마신것
    d[i][2] = d[i-1][1] + a[i]   # i번째 2번째로 마신것
    
print(max(d[n]))