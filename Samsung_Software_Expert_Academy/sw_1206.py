
T = 10

for t in range(1,T+1):
    a = input()
    # print(a)
    MAP = list(map(int,input().split()))

    max_len = len(MAP)

    ans = 0

    for i in range(2,max_len-2):

        temp = max(MAP[i-2], MAP[i-1], MAP[i+1], MAP[i+2])

        if MAP[i] > temp:
            ans += MAP[i] - temp
            # print(i, temp)


    print("#",end="")
    print(t,ans)
