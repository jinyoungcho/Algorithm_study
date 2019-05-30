#Bitmask + BFS + Connected Component 문제!

from collections import deque
C, R = list(map(int, input().split()))

MAP = []
for _ in range(R):
    MAP.append(list(map(int, input().split())))


check = [[0]*C for _ in range(R)]

di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]
#서 북 동 남

count_dic = {}

def bfs(i, j,ccp):
    cnt = 0
    q = deque()
    q.append((i, j))
    check[i][j] = ccp

    while(q):
        i, j = q.popleft()
        cnt += 1
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if not( ~MAP[i][j] & (1 << k)):
                continue
            if not ( 0 <= ni < R and 0 <= nj < C):
                continue
            if check[ni][nj] != 0:
                continue
            check[ni][nj] = ccp
            q.append((ni, nj))

    count_dic[ccp] = cnt

    return cnt

def bfs2():
    i, j = 0, 0


    connected_li=[]

    q=deque()
    check2 = [[False]*C for _ in range(R)]
    q.append((i, j))
    check2[i][j] = True

    while(q):
        i, j = q.popleft()

        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]

            if not (0 <= ni < R and 0 <= nj < C):
                continue

            if check2[ni][nj] == True:
                continue

            if check[i][j] != check[ni][nj]:
                connected_li.append((check[i][j],check[ni][nj]))

            check2[ni][nj] = True
            q.append((ni, nj))

    return connected_li



MAXI = 0
ccp = 1
for i in range(R):
    for j in range(C):
        if check[i][j] != 0:
            continue
        MAXI = max(bfs(i,j,ccp),MAXI)
        ccp += 1

cli = bfs2()
temp=0
for i,j in cli:
    temp = max(temp,count_dic[i]+count_dic[j])


# for _ in range(R):
#     print(check[_])

print(ccp-1)
print(MAXI)
print(temp)