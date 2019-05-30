N,M = list(map(int,input().split()))

MAP = [[0] * M for _ in range(N)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

i=0;j=0;k=0;cnt = 0

while(True):
    # print(i,j)
    if MAP[i][j] != 0:
        break

    MAP[i][j] = 1

    ni = i + di[k]
    nj = j + dj[k]
    # print(ni,nj)
    if not(0 <= ni < N and 0 <= nj < M) or MAP[ni][nj] != 0:
        k += 1
        k %= 4
        # print(i,j,k)
        cnt += 1

        ni = i+di[k]
        nj = j+dj[k]

    i = ni
    j = nj

print(cnt-1)