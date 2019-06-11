for t in range(1,11):

    input()

    N, M = list(map(int, input().split()))


    ans = pow(N,M)


    print("#",end='')
    print(t,ans)