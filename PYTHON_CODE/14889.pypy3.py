N = int(input())
MAP = [list(map(int,input().split())) for _ in range(N)]

check = [False] * N



MINI = 1000000000

def get_ans():
    # print(check)
    global MINI
    temp1 = 0
    temp2 = 0
    for ni in range(N):
        for nj in range(N):

            if ni == nj:
                continue

            if check[ni] and check[nj]:
                temp1 += MAP[ni][nj]
            elif check[ni]==False and check[nj]==False:
                temp2 += MAP[ni][nj]

    temp3 = abs(temp1-temp2)

    MINI = min(temp3,MINI)


for i in range(1<<N):
    check = [False] * N
    for j in range(N):

        if i & 1<<j:
            check[j] = True

    if check.count(True) == N//2:
        get_ans()

print(MINI)