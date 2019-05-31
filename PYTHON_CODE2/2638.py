# BFS 응용문제, 공기부터 bfs를 시작하여
# 치즈부분이 공기와 2면 이상 다아 있으면
# 해당 부분을 삭제시키고 다시 bfs를 진행
# 모든 치즈가 사라지면 break!

N, M = list(map(int, input().split()))
MAP = []

for _ in range(N):
    MAP.append(list(map(int, input().split())))


from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs():

    check = [[False]*M for _ in range(N)]

    check[0][0] = True

    q = deque()

    q.append((0,0))
    check2 = [[0]*M for _ in range(N)]
    li_ = []
    while(q):

        i,j = q.popleft()

        for k in range(4):

            ni,nj = i+di[k], j + dj[k]

            if not( 0<= ni < N and 0 <= nj < M):
                continue

            if MAP[ni][nj] == 1:

                check2[ni][nj] += 1

                if check2[ni][nj] >= 2:

                    li_.append((ni,nj))

                continue

            if check[ni][nj]:
                continue

            q.append((ni,nj))
            check[ni][nj] = True

    return list(set(li_))


def is_clear():

    # clear = True

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 1:
                return False
    return True

cnt = 0
while(True):

    if is_clear():
        break

    dele_li = bfs()

    for i,j in dele_li:
        MAP[i][j] = 0

    cnt += 1

print(cnt)