# https://www.acmicpc.net/problem/15683

# input

# 4 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 0 6 0
# 0 0 0 0 0 0

# output

# 20

#CCTV의 방향을 적절히 정해서, 사각지대의 최소크기 구하는 문제
# -> Brute Force(dfs)
# 생각보다 간단한 문제였지만, 함수화 할 수 있는 부분
# (cctv 종류에 따른 감시구역 check 부분에서 함수화를 이용했다면..)
# 더 짧은 코드로 구현 가능했을 것 같다...!
# 파이썬에 switch 문이 없다는게 너무나 아쉽군!

# 문제풀이 1시간!

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = list(map(int, input().split()))

MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

check = [[False] * M for _ in range(N)]
cctv = []
cctv5 = []
wall = []
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 6:
            wall.append((i,j))
        elif 0 < MAP[i][j] < 5:
            cctv.append((i,j))
        elif MAP[i][j] == 5:
            cctv5.append((i,j))

for i,j in wall:
    check[i][j] = True

for i,j in cctv5:
    check[i][j] = True

    #동 북 서 남

    for k in range(4):

        ni = i
        nj = j

        while(True):

            ni += di[k]
            nj += dj[k]

            if not (0 <= ni < N and 0 <= nj < M): #범위를 벗어났다면
                break

            if MAP[ni][nj] == 6: #벽이라면
                break

            check[ni][nj] = True


def find_blind_spot():
    temp = 0
    for i in range(N):
        for j in range(M):
            if check[i][j] == False:
                temp += 1

    return temp




def draw_map(cctv_i, cctv_j ,kind, dir):

    #cctv의 종류와, 방향을 입력받아유
    list_for_return_map = []

    check[cctv_i][cctv_j] = True

    if kind == 1:
        ni = cctv_i
        nj = cctv_j
        while(True):
            ni += di[dir]
            nj += dj[dir]
            if not (0 <= ni < N and 0 <= nj < M): #범위를 벗어났다면
                break
            if MAP[ni][nj] == 6: #벽이라면
                break
            if check[ni][nj] == False:
                list_for_return_map.append((ni,nj))
                check[ni][nj] = True

    elif kind == 2:
        ni = cctv_i
        nj = cctv_j
        while(True):
            ni += di[dir]
            nj += dj[dir]
            if not (0 <= ni < N and 0 <= nj < M): #범위를 벗어났다면
                break
            if MAP[ni][nj] == 6: #벽이라면
                break
            if check[ni][nj] == False:
                list_for_return_map.append((ni,nj))
                check[ni][nj] = True

        ni = cctv_i
        nj = cctv_j
        while(True):
            ni += di[(dir+2)%4]
            nj += dj[(dir+2)%4]
            if not (0 <= ni < N and 0 <= nj < M): #범위를 벗어났다면
                break
            if MAP[ni][nj] == 6: #벽이라면
                break
            if check[ni][nj] == False:
                list_for_return_map.append((ni,nj))
                check[ni][nj] = True


    elif kind == 3:

        ni = cctv_i
        nj = cctv_j
        while(True):
            ni += di[dir]
            nj += dj[dir]
            if not (0 <= ni < N and 0 <= nj < M): #범위를 벗어났다면
                break
            if MAP[ni][nj] == 6: #벽이라면
                break
            if check[ni][nj] == False:
                list_for_return_map.append((ni,nj))
                check[ni][nj] = True

        ni = cctv_i
        nj = cctv_j
        while(True):
            ni += di[(dir+1)%4]
            nj += dj[(dir+1)%4]
            if not (0 <= ni < N and 0 <= nj < M): #범위를 벗어났다면
                break
            if MAP[ni][nj] == 6: #벽이라면
                break
            if check[ni][nj] == False:
                list_for_return_map.append((ni,nj))
                check[ni][nj] = True


    elif kind == 4:

        ni = cctv_i
        nj = cctv_j
        while(True):
            ni += di[dir]
            nj += dj[dir]
            if not (0 <= ni < N and 0 <= nj < M): #범위를 벗어났다면
                break
            if MAP[ni][nj] == 6: #벽이라면
                break
            if check[ni][nj] == False:
                list_for_return_map.append((ni,nj))
                check[ni][nj] = True

        ni = cctv_i
        nj = cctv_j
        while(True):
            ni += di[(dir+2)%4]
            nj += dj[(dir+2)%4]
            if not (0 <= ni < N and 0 <= nj < M): #범위를 벗어났다면
                break
            if MAP[ni][nj] == 6: #벽이라면
                break
            if check[ni][nj] == False:
                list_for_return_map.append((ni,nj))
                check[ni][nj] = True

        ni = cctv_i
        nj = cctv_j
        while(True):
            ni += di[(dir+1)%4]
            nj += dj[(dir+1)%4]
            if not (0 <= ni < N and 0 <= nj < M): #범위를 벗어났다면
                break
            if MAP[ni][nj] == 6: #벽이라면
                break
            if check[ni][nj] == False:
                list_for_return_map.append((ni,nj))
                check[ni][nj] = True



    return list_for_return_map

def return_MAP(li_f_re):
    for i,j in li_f_re:
        check[i][j] = False

MINI = 100
len_cctv = len(cctv)
def dfs(cnt,idx):

    global MINI

    if cnt == len_cctv:
        #사각지대 갯수 확인
        # print("~")
        # for _ in range(N):
        #     print(check[_])

        num_bs = find_blind_spot()
        MINI = min(MINI, num_bs)
        return

    else:
        for k in range(4):
            # draw MAP
            cctv_i, cctv_j = cctv[idx]
            cctv_kind = MAP[cctv_i][cctv_j]
            list_for_return = draw_map(cctv_i,cctv_j,cctv_kind,k)

            dfs(cnt+1,idx+1)

            return_MAP(list_for_return)

dfs(0,0)

print(MINI)