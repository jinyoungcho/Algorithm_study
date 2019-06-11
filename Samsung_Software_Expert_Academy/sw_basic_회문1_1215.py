def check(li):

    # if num_hui_men % 2 == 0:

    if li[:num_hui_men//2] == li[::-1][:num_hui_men//2]:

        return True

    return False
    # else:
    #
    #     if li[:num_hui_men//2] ==

for t in range(1,10+1):

    num_hui_men = int(input())

    N,M = 8,8

    MAP = []

    for _ in range(N):
        MAP.append(list(input()))


    cnt = 0

    for i in range(N):
        for j in range(0,N-num_hui_men+1):
            if check(MAP[i][j:j+num_hui_men]):
                # print(MAP[i][j:j+num_hui_men])
                cnt += 1

    MAP = list(zip(*MAP))
    for i in range(N):
        for j in range(0,N-num_hui_men+1):
            if check(MAP[i][j:j+num_hui_men]):
                # print(MAP[i][j:j+num_hui_men])
                cnt += 1
    print("#",end='')
    print(cnt)