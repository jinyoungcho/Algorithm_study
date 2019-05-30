R, C = list(map(int,input().split()))

K = int(input()) #장애물 갯수

obs_li = []

for _ in range(K):
    obs_li.append(list(map(int, input().split())) )

sr, sc = list(map(int, input().split()))

cr, cc = sr, sc

dir_li = list(map(int, input().split()))


check = [[False] * C for _ in range(R)]

for i,j in obs_li:
    check[i][j] = True

check[sr][sc] = True

di = [0,-1,1,0,0]
dj = [0,0,0,-1,1]


d_idx = 0
cnt = 0

while(True):


    nsr, nsc = sr + di[dir_li[d_idx]], sc + dj[dir_li[d_idx]]



    if not (0 <= nsr < R and 0 <= nsc < C) or check[nsr][nsc]:
        cnt += 1
        d_idx = (d_idx + 1) % 4
        if cnt == 4:
            break

        continue

    sr = nsr
    sc = nsc
    check[sr][sc] = True
    cnt = 0
    # print(sr,sc)


print(sr,sc)