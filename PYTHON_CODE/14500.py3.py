N,M = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        # ㅡ
        if j+3 < M:
            temp = a[i][j] + a[i][j+1] +a[i][j+2] + a[i][j+3]
            ans = max(temp,ans)
        
        # |
        if i+3 < N:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j]
            ans = max(temp,ans)
            
#             print(temp)
        
        # L
        if j+1 < M and i+2<N:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j+1]
            ans = max(temp,ans)
        
        # ㅢ
        if j+2 < M and i > 0: 
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i-1][j+2]
            ans = max(temp,ans)
        
        # ㄴ
        if i < N-1 and j+2 < M:
            temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2]
            ans = max(temp,ans)
#             print(temp)
    
        # _l
        
        if i-1 > 0 and j+1 <M:
            temp = a[i][j] + a[i][j+1] + a[i-1][j+1] + a[i-2][j+1]
            ans = max(temp,ans)
#             print(temp)
#     print("--")
        
        # r
        if i < N-1 and j+2 < M:
            temp = a[i][j] + a[i+1][j] + a[i][j+1] + a[i][j+2]
            ans = max(temp,ans)
#             print(temp)
        #ㅡ|
        if i < N-1 and j+2 < M:
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j]
            ans = max(temp,ans)
#             print(temp)
        
        # ㄱ
        if i < N-1 and j+2 < M:
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+2]
            ans = max(temp,ans)
#             print(temp)
            
        # 
        if i+2 < N and j+1 < M:
            temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+2][j+1]
            ans = max(temp,ans)
#             print(temp)
        
        if i > 0 and j+2 < M:
            temp = a[i][j] + a[i][j+1] + a[i-1][j+1] + a[i-1][j+2]
            ans = max(temp,ans)
#             print(temp)
            
        if i < N-1 and j+2 < M:
            temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j+2]
            ans = max(temp,ans)
#             print(temp)
            
        if j>0 and i < N-2:
            temp = a[i][j] + a[i+1][j] + a[i+1][j-1] + a[i+2][j-1]
            ans = max(temp,ans)
#             print(temp)
            
        if j+2 < M and i+1 < N:
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1]
            ans = max(temp,ans)
#             print(temp)
            
        if i>0 and j+2 < M:
            temp  = a[i][j] + a[i][j+1] + a[i][j+2] + a[i-1][j+1]
            ans = max(temp,ans)
#             print(temp)
            
        if i>0 and j+1 < M and i+1 <N:
            temp = a[i][j] + a[i][j+1] + a[i-1][j+1] + a[i+1][j+1]
            ans = max(temp,ans)
#             print(temp)
        
        if i>0 and i+1 < N and j+1 <M:
            temp = a[i][j] + a[i][j+1] + a[i-1][j] + a[i+1][j]
            ans = max(temp,ans)
#             print(temp)
        
        if i+1<N and j+1<M:
            temp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1]
            ans = max(temp,ans)
#             print(temp)
        if i+2 < N  and j+1 <M :
            temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1]
            ans = max(temp,ans)
#             print(temp)
            
        if i+2 < N  and j+1 <M :
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i][j+1]
            ans = max(temp,ans)
#             print(temp)
#     print("--")
print(ans)

