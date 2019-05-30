N = int(input())
K = int(input())

apples = []

for _ in range(K):
    X,Y = list(map(int,input().split()))
    apples.append([X-1,Y-1])

                   
L = int(input())
directions = {}

for _ in range(L):
    kk,vv = list(input().split())
    directions[int(kk)] = vv
    
a = [[0] * N for i in range(N)]
for apple in apples:
    a[apple[0]][apple[1]] = 1
    
l_s = 1

ans = 0
n = 0

d = ''

di=[0,1,0,-1] #동,남,서,북
dj=[1,0,-1,0]
crushed = False
k = 0

head = [[0,0]]
while True:
    
    ans+=1 #한칸 이동

    cur = [head[ans-1][0] + di[k], head[ans-1][1] + dj[k]]

    
    if cur in apples:
        l_s+=1
        apples.remove(cur)
        
    
    
    
    if cur in head[ len(head)-l_s:]:
        crushed = True
    
    head.append(cur)

    
    if cur[0] < 0 or cur[0] >= N or cur[1] <0 or cur[1] >=N or crushed == True:
        break
        
        
        
        
    if ans in directions:
        if directions[ans] =='D': #우회전
            k = (k+1) % 4
        elif directions[ans] =='L': #죄회전
            k = (k+3) % 4
            
print(ans)