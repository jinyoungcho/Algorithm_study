#시간초과 실패한 문제 나중에 실력 키워서 다시 풀어봅시다..!

# https://www.acmicpc.net/problem/3025

# 단순 시뮬레이션 문제

# N값이 worst case일 경우 시간이 엄청 오래걸립니다..!

# 파이썬문제인지 코드문제인지 나중에 확인

N,M = list(map(int,input().split()))

MAP = []

for _ in range(N):
    MAP.append(list(input()))

N_stone = int(input())

def is_bottom_or_wall_or_stone(i,j):

    if i==N or MAP[i][j] == 'X':
        return 1
    elif MAP[i][j] == 'O':
        return 2
    elif MAP[i][j] == '.':
        return 0



def drop_ball(j):
    print("~",j)
    i=0
    while(True):

        if i == N-1:
            MAP[i][j] = 'O'
            break

        temp = is_bottom_or_wall_or_stone(i+1,j)
        # print(temp)
        #중력
        if temp == 0:
            i += 1
            continue
        #멈춰윰
        elif temp == 1:
            MAP[i][j] = 'O'
            break
        #밑이 돌이면..!
        elif temp == 2:

            if (0 <= j-1) and MAP[i][j-1] == '.' and MAP[i+1][j-1] =='.':
                j -= 1
                i += 1
                continue

            if (j+1 < M) and MAP[i][j+1] == '.' and MAP[i+1][j+1] == '.':
                j += 1
                i += 1
                continue

            MAP[i][j] = 'O'
            break

    # print("~")
    # for _ in range(N):
    #     print(MAP[_])








for _ in range(N_stone):

    drop_j = int(input()) - 1



    drop_ball(drop_j)


for i in range(N):
    for j in range(M):
        print(MAP[i][j],end='')
    print("")