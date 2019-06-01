# 개인적으로 재미있는 시뮬 + connected component 문제~!


R,C = list(map(int,input().split()))

MAP = []

for _ in range(R):
    MAP.append(list(input()))

check = [[False] * C for _ in range(R)]


from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(i,j,num_cn):

    q = deque()
    check[i][j] = True
    q.append((i,j))
    while(q):

        i, j = q.popleft()

        for k in range(4):

            ni = i+di[k]
            nj = j+dj[k]

            if not (0 <= ni < R and 0 <= nj < C):
                continue

            if check[ni][nj]:
                continue

            if MAP[ni][nj] == '#':
                continue

            check[ni][nj] = True
            q.append((ni,nj))

            if MAP[ni][nj] == 'v': #늑대
                if dict.get(num_cn) == None:
                    dict[num_cn] = [[],[(ni,nj)]]
                else:
                    dict[num_cn][1].append((ni,nj))
            elif MAP[ni][nj] == 'o': #양
                if dict.get(num_cn) == None:
                    dict[num_cn] = [[(ni,nj)],[]]
                else:
                    dict[num_cn][0].append((ni, nj))
dict={}
num_cn = 0
for i in range(R):
    for j in range(C):
        if check[i][j]:
            continue
        bfs(i,j,num_cn)
        num_cn+=1


ans_sheep = 0
ans_wolf = 0

for key in dict:
    num_sheep, num_wolf = len(dict[key][0]), len(dict[key][1])

    if num_sheep > num_wolf:
        ans_sheep += num_sheep
    else:
        ans_wolf += num_wolf

print(ans_sheep, ans_wolf)