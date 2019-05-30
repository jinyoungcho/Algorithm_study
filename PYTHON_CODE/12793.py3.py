# M,N 공간의 게임판
# M 이 Y
#y = 0 ->

N, M, K = list(map(str, input().split()))
MAP = []




M = (int(M)*2) + 1
N = (int(N)*2) + 1
K = int(2 * float(K))

# print("k~!",K)

for i in range(M):
    MAP.append(list(input()))

from collections import deque

di1 = [1,-1]
dj1 = [0,0]

di2 = [0,0]
dj2 = [1,-1]

di3 = [1,-1,0,0]
dj3 = [0,0,1,-1]

def bfs(i, j):

    q = deque()
    q.append((i, j))

    find = False
    while(q):

        i,j = q.popleft()

        if MAP[i][j] == '-': # 상 하
            for k in range(2):
                ni,nj = i + di1[k], j + dj1[k]

                if not (0 <= ni < M and 0 <= nj < N):
                    continue

                if MAP[ni][nj] not in ['B','.']:
                    continue

                q.append((ni,nj))

        elif MAP[i][j] == '|': # 좌 우
            for k in range(2):
                ni,nj = i + di2[k], j + dj2[k]

                if not (0 <= ni < M and 0 <= nj < N):
                    continue

                if MAP[ni][nj] not in ['B','.']:
                    continue

                q.append((ni, nj))


        elif MAP[i][j] in ['B','.']: # B , .
            find = True


            MAP[i][j] = '~'
            for k in range(4):

                ni, nj = i + di3[k], j + dj3[k]



                if not (0 <= ni < M and 0 <= nj < N):
                    continue

                if MAP[ni][nj] not in ['B','.']:
                    continue



                q.append((ni, nj))

    return find


def simulate():
    start_i = M - 1
    start_j = K



    di = -1
    dj = -1

    ans = 0

    done = False

    #방향 설정
    clock = 0
    dir = 0

    while(not done):



        start_i += di
        start_j += dj

        if start_i == 0:
            di = -di
        if start_j == 0 or start_j == N - 1:
            dj = -dj

        if start_i == M - 1: #다시 바닥으로 돌아오면 끝
            done = True
            break


        if MAP[start_i][start_j] != '+' or 'O':
            if bfs(start_i, start_j):
                ans += 1

        # print(start_i, start_j)
        # for i in range(M):
        #     for j in range(N):
        #         if i == start_i and j == start_j:
        #             print("*",end="")
        #         else:
        #             print(MAP[i][j],end="")
        #     print("")

    return ans
print(simulate())
