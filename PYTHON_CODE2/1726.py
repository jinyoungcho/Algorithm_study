# 명령 1. Go k
#   - k는 1, 2 또는 3일 수 있다. 현재 향하고 있는 방향으로 k칸 만큼 움직인다.
#
# 명령 2. Turn dir
#   - dir은 left 또는 right 이며, 각각 왼쪽 또는 오른쪽으로 90° 회전한다.

#동 서 남 북 1,2,3,4

#3차원 BFS, 방향조절에 신경 잘 써야 실수하지 않는 문제입니다~!

N, M = list(map(int, input().split()))
MAP = []
for _ in range(N):
    MAP.append((list(map(int, input().split()))))

si, sj, dir = list(map(int, input().split()))

gi, gj, gir = list(map(int, input().split()))

di = [0,1,0,-1] #동남서북
dj = [1,0,-1,0]

si-=1
sj-=1
gi-=1
gj-=1

if dir == 1:
    dir = 0
elif dir == 2:
    dir = 2
elif dir == 3:
    dir = 1
elif dir == 4:
    dir = 3

if gir == 1:
    gir = 0
elif gir == 2:
    gir = 2
elif gir == 3:
    gir = 1
elif gir == 4:
    gir = 3





from collections import deque

def bfs(si, sj, dir):

    check = [[[-1] * 4 for __ in range(M)] for _ in range(N)]


    # for _ in range(N):
    #     print(check[_])
    # print(check)

    check[si][sj][dir] = 0

    q = deque()

    q.append((si, sj, dir))

    while(q):

        i,j,dir = q.popleft()

        if i == gi and j == gj and dir == gir:
            return check[i][j][dir]

        # 좌 우 방향
        for k in [1, 3]:

            nir = (dir+k) % 4

            if check[i][j][nir] != -1:
                continue

            check[i][j][nir] = check[i][j][dir] + 1
            q.append((i, j, nir))

        for f in [1, 2, 3]: #앞으로 이동

            ni = i + (di[dir]*f)
            nj = j + (dj[dir]*f)

            if not (0 <= ni < N and 0 <= nj < M):
                break

            if check[ni][nj][dir] != -1:
                continue

            if MAP[ni][nj] == 1:
                break

            check[ni][nj][dir] = check[i][j][dir] + 1
            q.append((ni, nj, dir))

    return check[gi][gj][dir]

print(bfs(si, sj, dir))