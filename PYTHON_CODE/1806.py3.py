n,s = map(int,input().split())
a = list(map(int,input().split()))

left = 0
right = 0

total_sum = a[0]
ans = n+1



while(right <n):
    
    if total_sum < s:
        right += 1
        if right < n:
            total_sum+= a[right]
    
    elif total_sum >= s:
        ans = min(right-left+1,ans)
        total_sum -= a[left]
        left+=1
        
if ans >n:
    ans = 0
    
print(ans)