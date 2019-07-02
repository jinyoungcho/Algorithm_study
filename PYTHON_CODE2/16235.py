di=[-1,-1,-1,0,0,1,1,1]
dj=[-1,0,1,-1,1,-1,0,1]

N,M,K = list(map(int,input().split()))

Arr = []
A = []
MAP = []
for _ in range(N):
    A.append(list(map(int,input().split())))
    Arr.append([5] * N)
    MAP.append([[] for _ in range(N)])

for _ in range(M):
    x,y,z = list(map(int,input().split()))
    MAP[x-1][y-1].append(z)


# for _ in range(N):
#     print(MAP[_])

while(K):

    dead_tree = []
    # print("봄 전 양분")
    # for _ in range(N):
    #     print(Arr[_])

    # print("현재 나무 상태")
    # for _ in range(N):
    #     print(MAP[_])
    #봄
    for i in range(N):
        for j in range(N):
            for tdx in range(len(MAP[i][j])):

                age_of_tree = MAP[i][j].pop(-1)

                if Arr[i][j] - age_of_tree >= 0:
                    Arr[i][j] -= age_of_tree
                    age_of_tree += 1
                    MAP[i][j].insert(0,age_of_tree)
                else:

                    dead_tree.append((i,j,age_of_tree//2))

    # print("봄 이후 여름 전 양분")
    # for _ in range(N):
    #     print(Arr[_])


    #여름
    for i,j,a in dead_tree:
        Arr[i][j] += a

    # print("죽은 나무로 충전")
    # for _ in range(N):
    #     print(Arr[_])



    # print("~")
    #가을
    for i in range(N):
        for j in range(N):
            for tdx in range(len(MAP[i][j])):

                if MAP[i][j][tdx] % 5 == 0:

                    for k in range(8):

                        ni = i+di[k]
                        nj = j+dj[k]

                        if not (0<= ni <N and 0 <= nj < N):
                            continue

                        MAP[ni][nj].append(1)

    #겨울
    for i in range(N):
        for j in range(N):
            Arr[i][j] += A[i][j]

    K-=1

ans = 0

for i in range(N):
    for j in range(N):
        ans += len(MAP[i][j])

print(ans)