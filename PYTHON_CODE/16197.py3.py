di = [0,0,1,-1]
dj = [1,-1,0,0]

# n, m = 5,3

# a = [
#     ["#","#","#"],
#     [".","o","."],
#     ["#",".","#"],
#     [".","o","."],
#     ["#","#","#"]
# ]

n,m = list(map(int,input().split()))

a = [list(input()) for _ in range(n)]

loc_coins=[]
for idx,i in enumerate(a):
    for jdx,j in enumerate(i):
        if j == 'o':
            loc_coins.append([idx,jdx])
            
            
def go(count, loc_coins):
#     print(count, loc_coins)
    
    if count == 11:
        return -1
    if len(loc_coins) == 0: #둘 다 떨어지는 경우
        return -1
    if len(loc_coins) == 1: #둘 중 하나만 떨어지는 경우
        return count
    
    ans = -1
    
    for k in range(4):
        temps = []
        
        for coin in loc_coins:
            ni = coin[0] + di[k]
            nj = coin[1] + dj[k]
            
            if 0 <= ni <n and 0 <= nj < m: #나가지 않은 경우
                if a[ni][nj] == "#": #벽
                    temps.append([coin[0],coin[1]])
                else: #빈칸
                    temps.append([ni,nj])
        
        asdf = go(count+1,temps)
        
        if asdf == -1:
            continue
        
        if ans == -1 or ans > asdf:
            ans = asdf
    return ans

print(go(0, loc_coins))