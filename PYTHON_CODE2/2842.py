#Two pointer + bfs

N = int(input())

MAP = []

for _ in range(N):
    MAP.append(list(input()))

office = []
house_li = []

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 'P':
            office.append(i)
            office.append(j)
        elif MAP[i][j] == 'K':
            house_li.append([i, j])
MAP2 = []
for _ in range(N):
    MAP2.append(list(map(int, input().split())))

height_li = []
for i in range(N):
    for j in range(N):
        height_li.append(MAP2[i][j])

from collections import deque

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(lower_bound, upper_bound):

    i, j = office
    now_height = MAP2[i][j]

    if not lower_bound <= now_height <= upper_bound:
        return False

    check = [[False] * N for _ in range(N)]
    q = deque()
    q.append((i,j))
    check[i][j] = True
    while(q):
        i, j = q.popleft()
        for k in range(8):
            ni, nj = i+di[k], j+dj[k]
            if not (0<= ni <N and 0 <= nj <N):
                continue
            if check[ni][nj]:
                continue
            if not lower_bound <= MAP2[ni][nj] <= upper_bound:
                continue
            check[ni][nj] = True
            q.append((ni,nj))
    ccc = 0
    for i,j in house_li:
        if check[i][j] == True:
            ccc+=1
    if ccc == len(house_li):
        return True

    return False

def binary_search(height_li):

    height_li = sorted(list(set(height_li)))

    # print(height_li)

    mini = height_li[0]
    maxi = height_li[-1]

    ans = 10000000000
    j=0
    for i in range(len(height_li)):
        # print(i,j)

        while(True):
            # print(i,j,height_li[j],height_li[i])

            if bfs(height_li[j],height_li[i]) == False:
                # print('nope')
                break
            # print('yes')
            ans = min(ans, height_li[i]-height_li[j])
            j+=1
            if j >= len(height_li):
                break
    return ans

print(binary_search(height_li))

# print(bfs(0))