T = 10

for testcase in range(1,T+1):

    ans = ''

    N = int(input())
    password = list(input().split())

    num_cmd = int(input())
    cmd = input()

    cmd = cmd.split()

    idx = 0

    now = ''
    x, y = 0, 0
    li = []
    while idx<len(cmd):
        # print(idx)


        # print(idx, cmd[idx], now, x, y, li)

        if cmd[idx]=='I' or cmd[idx]=='D':
            # print(now, x, y, li)
            if now == 'I':
                for _ in range(y-1,-1,-1):
                    password.insert(x,li[_])
            elif now == 'D':
                # print(now,x,y)
                # print(password[x:])
                for _ in range(y):
                    password.pop(x)
                # print(password[x:])
            elif now == 'A':
                for _ in li:
                    password.append(_)


            if cmd[idx] == 'I':
                now = 'I'
                x=int(cmd[idx+1])
                y=int(cmd[idx+2])
                li=[]
                idx += 3
            elif cmd[idx] == 'D':
                now = 'D'
                x=int(cmd[idx+1])
                y=int(cmd[idx+2])
                idx += 3
            elif cmd[idx] == 'A':
                now = 'A'
                y=int(cmd[idx+1])
                idx+=2
                li=[]

        else:
            li.append(cmd[idx])
            idx+=1

    if now == 'I':
        for _ in range(y - 1, -1, -1):
            password.insert(x, li[_])
    elif now == 'D':
        for _ in range(y):
            password.pop(x)
    elif now == 'A':
        for _ in li:
            password.append(_)

    # print("?")
    # print(password[:10])

    # print(cmd.split('I')[1].split(' ')[3:-1])
    # print(password)
    # s=[]
    # for c in list(cmd.split('I'))[1:]:
    #     a = c.split(" ")[1:-1]
    #
    #     x,y = int(a[0]),int(a[1])
    #     s = a[2:]
    #
    #     for _ in range(y-1,-1,-1):
    #         password.insert(x,s[_])
    #
    #     # password.insert(x,s[:y])
    #
    #     # print(s)
    #
    # # print(password[:10])
    #
    print("#",end='')
    #
    for _ in range(10):
        ans += password[_] + ' '
    #
    print(testcase,ans)
