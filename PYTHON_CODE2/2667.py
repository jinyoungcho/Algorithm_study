#Connected Component/

N = int(input())

MAP = []

for _ in range(N):
    MAP.append(list(map(
        int,list(input())
    )))

# print(MAP)

dict={}

check = [[0]*N for _ in range(N)]
cnt = 1



from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs(i,j,c):

    q = deque()
    q.append((i, j))
    check[i][j] = c

    count_ = 0

    while(q):
        i,j = q.popleft()
        count_+=1

        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]

            if not (0 <= ni < N and 0 <= nj < N):
                continue

            if check[ni][nj] != 0:
                continue

            if MAP[ni][nj] == 0 :
                continue

            check[ni][nj] = c
            q.append((ni,nj))

    return count_

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1 and check[i][j] == 0:
            house_cnt = bfs(i,j,cnt)
            dict[cnt] = house_cnt
            # print(cnt, house_cnt)
            cnt +=1

# print(dict)

# for _ in range(N):
#     print(check[_])


print(cnt-1)
a = list(dict.values())
a.sort()
for i in a:
    print(i)