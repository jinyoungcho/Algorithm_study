T = int(input())

N = 6
X = 2

MAP = []

ans = 0
setup_check = []
# 9 4
# 4 4 3 3 3 3 2 2 2
# 4 4 3 3 1 1 2 2 3
# 3 3 2 2 1 1 1 1 2
# 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1
# 2 2 1 1 1 1 1 1 1
# 2 2 1 1 1 1 1 1 1
# 2 2 2 2 2 2 1 1 1
# 3 3 3 3 2 2 2 2 1

def setup_forward(i,j,next_height):
    global X
    global setup_check

    j=j
    check = True

    for x in range(X):

        if j+x < N and MAP[i][j+x] == next_height and setup_check[j+x] == False:
            setup_check[j+x] = True
            continue
        else:
            check = False

    return check

def setup_backward(i,j,cur_height):
    global X
    global setup_check
    j=j
    check = True

    for x in range(X):

        if 0 <= j-x and MAP[i][j-x] == cur_height and setup_check[j-x] == False:
            setup_check[j - x] = True
            continue

        else:
            check = False
            break

    return check

def simulate():
    global ans
    global X
    global MAP
    global setup_check
    #가로방향
    c = 0
    for i in range(N):
        # print(MAP[i])
        setup_check = [False] * N
        cur_hight = MAP[i][0]
        j=1
        while(True):
            if j == N:
                # print("통과~")
                c+=1
                break
            next_hight = MAP[i][j]
            if abs(cur_hight-next_hight) > 1:
                break


            elif abs(cur_hight-next_hight) == 0:
                j += 1
            elif abs(cur_hight-next_hight) == 1: # 높이차이 1~


                if cur_hight < next_hight:

                    # 뒤로 오르막길 설치
                    if setup_backward(i, j-1, cur_hight):
                        cur_hight = next_hight
                        j += 1
                    else:
                        break

                elif cur_hight > next_hight:
                    # 앞으로 내리막길 설치
                    if setup_forward(i, j, next_hight):
                        cur_hight = next_hight
                        j += 1
                    else:
                        break

    MAP = list(zip(*MAP))

    for i in range(N):
        # print(MAP[i])
        setup_check = [False] * N
        cur_hight = MAP[i][0]
        j=1
        while(True):
            if j == N:
                # print("통과~")
                c+=1
                break
            next_hight = MAP[i][j]
            if abs(cur_hight-next_hight) > 1:
                break


            elif abs(cur_hight-next_hight) == 0:
                j += 1
            elif abs(cur_hight-next_hight) == 1: # 높이차이 1~


                if cur_hight < next_hight:

                    # 뒤로 오르막길 설치
                    if setup_backward(i, j-1, cur_hight):
                        cur_hight = next_hight
                        j += 1
                    else:
                        break

                elif cur_hight > next_hight:
                    # 앞으로 내리막길 설치
                    if setup_forward(i, j, next_hight):
                        cur_hight = next_hight
                        j += 1
                    else:
                        break

    ans = c



for t in range(1,T+1):

    N,X = list(map(int,input().split()))

    MAP = [list(map(int,input().split())) for _ in range(N)]
    setup_check = [False] * N
    ans = 0

    simulate()

    print("#",end="")
    print(t,ans)