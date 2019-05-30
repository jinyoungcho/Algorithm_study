N, M = list(map(int,input().split()))

r, c, k = list(map(int,input().split()))

MAP = [list(map(int,input().split())) for _ in range(N)]
check = [[False]*M for _ in range(N)]

ni,nj = r,c
di = [-1, 0, 1, 0] # 북 동 남 서
dj = [0, 1, 0, -1]


for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            check[i][j] = True

#현재위치 청소
cnt = 0
done = False
while(True):
    if done:
        break
    # 1. 현재위치 청소
    if check[ni][nj] == False:
        cnt += 1
    # print(cnt,":",ni,nj)
    check[ni][nj] = True

    # 2. 왼쪽 방향부터 탐색 시작


    c = [False, False, False, False]

    while(True):


        # print("--")
        # for _ in range(N):
        #     print(check[_])

        # a
        if not all(c):

            left = k-1 if k-1 != -1 else 3
            # print("~",ni,nj,k,left)
            if 0 <= ni+di[left] < N and 0 <= nj + dj[left] < M:

                if check[ni+di[left]][nj+dj[left]] == False:
                    k = left
                    ni += di[left]
                    nj += dj[left]

                    break

                else:
                    k = left
                    c[k] = True
                    # print(c)

                    # print("--")
                    # for _ in range(N):
                    #     print(check[_])

                    if all(c) == True:
                        pass
                    else:
                        continue

        else:
        # c
            if 0 <= ni-di[k] < N and 0 <= nj-dj[k] < M and MAP[ni-di[k]][nj-dj[k]] != 1:

                ni -= di[k]
                nj -= dj[k]
                # print("빠꾸", ni, nj,k)
                break
            else:
                # print("~~")
                done = True
                break

print(cnt)