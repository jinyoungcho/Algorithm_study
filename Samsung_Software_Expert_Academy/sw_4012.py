T = int(input())

from itertools import permutations

for t in range(1,T+1):

    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]

    food = [0 for _ in range(N)]


    def cal():

        sumA=0
        sumB=0

        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                else:
                    if food[i] == 1 and food[j] == 1:
                        sumA += MAP[i][j]
                    elif food[i] == 2 and food[j] == 2:
                        sumB += MAP[i][j]

        return abs(sumA-sumB)

    mini =100000

    def dp(idx,acnt,bcnt):
        global mini

        if acnt > (N//2) or bcnt > (N // 2):
            return

        elif idx == N and acnt == N//2 and bcnt == N//2:
            temp = cal()
            mini = min(mini, temp)
        else:

            food[idx] = 1
            dp(idx+1,acnt+1,bcnt)
            food[idx] = 2
            dp(idx+1,acnt,bcnt+1)

    dp(0,0,0)
    print("#",end="")
    print(t,mini)