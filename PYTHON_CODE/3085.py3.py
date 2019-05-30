N = int(input())

MAP = [list(input()) for _ in range(N)]

di = [0,0,1,-1]
dj = [1,-1,0,0]


MAXI = 0
def check(si,sj,sni,snj):
    global MAXI

    st = MAP[si][0]
    cnt = 1
    for j in range(1,N):
        if st == MAP[si][j]:
            cnt += 1
        else:
            st = MAP[si][j]
            cnt = 1
        MAXI = max(MAXI, cnt)

    st = MAP[sni][0]
    cnt = 1
    for j in range(1,N):
        if st == MAP[si][j]:
            cnt += 1
        else:
            st = MAP[si][j]
            cnt = 1
        MAXI = max(MAXI, cnt)

    st = MAP[0][sj]
    cnt = 1
    for i in range(1,N):
        if st == MAP[i][sj]:
            cnt += 1
        else:
            st = MAP[i][sj]
            cnt = 1
        MAXI = max(MAXI, cnt)

    st = MAP[0][snj]
    cnt = 1
    for i in range(1,N):
        if st == MAP[i][snj]:
            cnt += 1
        else:
            st = MAP[i][snj]
            cnt = 1
        MAXI = max(MAXI, cnt)

    # for i in range(N):
    #     cnt = 1
    #     st = MAP[i][0]
    #     for j in range(1,N):
    #         # print(st)
    #         if st == MAP[i][j]:
    #             cnt += 1
    #
    #         else:
    #             st = MAP[i][j]
    #             cnt = 1
    #         MAXI = max(MAXI,cnt)
    #
    # for j in range(N):
    #     cnt = 1
    #     st = MAP[0][j]
    #     for i in range(1,N):
    #         if st == MAP[i][j]:
    #
    #             if st == MAP[i][j]:
    #                 cnt += 1
    #             else:
    #                 st = MAP[i][j]
    #                 cnt = 1
    #         MAXI = max(MAXI,cnt)

def simulate(i,j):

    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]

        if not (0 <= ni < N and 0 <= nj < N):
            continue

        if MAP[i][j] == MAP[ni][nj]:
            continue

        MAP[i][j], MAP[ni][nj] = MAP[ni][nj], MAP[i][j]
        check(i,j,ni,nj)
        MAP[i][j], MAP[ni][nj] = MAP[ni][nj], MAP[i][j]

for i in range(N):
    for j in range(N):

        simulate(i,j)

print(MAXI)