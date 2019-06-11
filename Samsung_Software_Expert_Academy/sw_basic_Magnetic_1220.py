import copy
from collections import deque



for t in range(1,11):

    input()
    MAP = []
    N = 100
    for _ in range(N):
        MAP.append(list(map(int, input().split())))

    MAP = list(zip(*MAP))
    ans = 0

    def find_component(copy_MAP):

        temp = 0

        st = 0
        second = 0
        for _ in range(N):
            if st == 0 and copy_MAP[_] == 1:
                st = 1

            elif st == 0 and copy_MAP[_] == 2:
                st = 2

            elif st == 1 and second == 0:
                if copy_MAP[_] == 2:
                    second = 2

            elif st == 2 and second == 0:
                if copy_MAP[_] == 1:
                    second = 1

            elif st != 0 and second !=0:
                if copy_MAP[_] != second or copy_MAP[_] == st:
                    temp += 1
                    second = 0

        if st != 0 and second !=0:
            temp += 1

        return temp




    def check_move(copy_MAP,j,dir):
        if dir == 1: # + 1

            nj = j + 1

            if nj >= N: #범위 넘어가
                check[j] = False
                return check[j]
            elif copy_MAP[nj] == 1: #같은방향 친구
                check[j] = check_move(copy_MAP,nj,1)
                return check[j]
            elif copy_MAP[nj] == 2: #다른방향 친구
                check[j] = True         ##둘다 못움직이죠~
                return check[j]

            else:
                return False


        elif dir == 2:

            nj = j-1
            if nj < 0: #범위 넘어가
                check[j] = False
                return check[j]

            elif copy_MAP[nj] == 2:
                check[j] = check_move(copy_MAP,nj,2)
                return check[j]
            elif copy_MAP[nj] == 1:
                check[j] = True
                return check[j]
            else:
                return False

    for _ in range(N):
        copy_MAP = list(MAP[_])
        check = [False] * N

        q1 = deque()
        q2 = deque()

        for j in range(N):
            if copy_MAP[j] == 1:
                q1.append((j,copy_MAP[j]))
            elif copy_MAP[j] == 2:
                q2.append((j,copy_MAP[j]))

        # print('before')
        # print(q1)
        # print(q2)

        while(q1):
            j,dir = q1.popleft()
            check_move(copy_MAP,j,dir)



        while(q2):
            j,dir = q2.popleft()
            check_move(copy_MAP,j,dir)
        # print("~")
        # print(check)
        # print(copy_MAP)
        # print(check[67])
        for j in range(N):
            if copy_MAP[j] == 1 and check[j] == False:
                q1.append((j,copy_MAP[j]))
            elif copy_MAP[j] == 2 and check[j] == False:
                q2.append((j,copy_MAP[j]))


        # print(q1,q2)
        # print(check)
        # print(q1)
        while(q1):
            j,dir = q1.pop()

            nj = j+1

            if nj >= N:
                copy_MAP[j] = 0
                continue

            elif check[nj] == True or copy_MAP[nj]==2:
                check[j] = True
                continue

            elif check[nj] == False and copy_MAP[nj] == 0:
                copy_MAP[j] = 0
                copy_MAP[nj] = 1
                q1.append((nj,dir))
        # print(q2)
        while(q2):
            j,dir = q2.popleft()

            nj = j-1

            if nj < 0:
                copy_MAP[j] = 0
                continue

            elif check[nj] == True or copy_MAP[nj]==1:
                check[j] = True
                continue

            elif check[nj] == False and copy_MAP[nj] == 0:
                copy_MAP[j] = 0
                copy_MAP[nj] = 2
                q2.appendleft((nj,dir))


        # print(copy_MAP)
        # print(check)


        if any(check):
            asdf = find_component(copy_MAP)
            # print(asdf)
            ans += asdf

    # check = [False] * 7

    print("#",end='')
    print(t,ans)
# 1 0 2 0 1 0 1
# 0 2 0 0 0 0 0
# 0 0 1 0 0 1 0
# 0 0 0 0 1 2 2
# 0 0 0 0 0 1 0
# 0 0 2 1 0 2 1
# 0 0 1 2 2 0 2