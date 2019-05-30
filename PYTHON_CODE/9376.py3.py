from collections import deque

di = [1,-1,0,0]
dj = [0,0,1,-1]

def bfs(MAP,x,y):    
    c = [[0] * len(MAP[0]) for i in range(len(MAP))]
    c2 = [[False] * len(MAP[0]) for i in range(len(MAP))]
    
    q = deque()
    q.append((x,y))
    c2[x][y] = True

    while q:
        i,j = q.popleft()
        
        for k in range(4):
            next_i = i + di[k]
            next_j = j + dj[k]
            
            if 0 <= next_i < len(MAP) and 0 <= next_j < len(MAP[0]):
                if c2[next_i][next_j] == False:
                    c2[next_i][next_j] = True
                    if MAP[next_i][next_j] == "." or MAP[next_i][next_j] == "$":
                        q.appendleft((next_i,next_j))
                        c[next_i][next_j] = c[i][j]
                    elif MAP[next_i][next_j] == "#":
                        q.append((next_i,next_j))
                        c[next_i][next_j] = c[i][j]+1
                    elif MAP[next_i][next_j] == "*":
                        pass
    return c
    
TEST_CASE = int(input())

for KKKK in range(TEST_CASE):

    h,w = list(map(int, input().split()))

    a = ['.'+input()+'.' for _ in range(h)]
    h+=2
    w+=2
    a = ['.'*w] + a + ['.'*w]

    loc_criminal=[]
    for idx, i in enumerate(a):
        for jdx, j in enumerate(i):
            if j == "$":
                loc_criminal.append((idx,jdx))

    d = []
    for i in loc_criminal:
        d.append(bfs(a,i[0],i[1]))
    d.append(bfs(a,0,0))

    ans = 999999999
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == "*":
                continue
            cur = d[0][i][j] + d[1][i][j] + d[2][i][j]

            if a[i][j] == "#":
                cur -= 2

            ans = min(ans,cur)

    print(ans)