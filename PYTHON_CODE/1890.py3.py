n = int(input())
a = list(list(map(int,input().split())) for i in range(n))
    
d = [[0]*n for _ in range(n)]
d[0][0] = 1
for i in range(n):
    for j in range(n):
        move = a[i][j]
#         print(i,j, a[i][j])
        
        if i == n-1 and j == n-1:
            continue
        
        if d[i][j] != 0:
            if j+move < n:
                d[i][j+move] += d[i][j]
            if i+move < n:
                d[i+move][j] += d[i][j]

#             for k in d:
#                 print(k)
#             print("---")

print(d[n-1][n-1])