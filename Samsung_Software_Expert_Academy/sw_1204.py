# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

T = int(input())

for t in range(1,T+1):
    input()
    MAP = [0 for _ in range(101)]
    for score in list(map(int,input().split())):
        MAP[score] += 1

    MAXI = max(MAP)

    # print(MAXI)
    ans = 0
    for i in range(100,-1,-1):
        if MAP[i] == MAXI:
            ans = i
            break
    print("#",end='')
    print(t,ans)