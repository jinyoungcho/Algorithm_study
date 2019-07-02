T = 10

for testcase in range(1,T+1):

    ans = ''

    N = int(input())
    password = list(input().split())

    num_cmd = int(input())
    cmd = input()

    # print(cmd.split('I')[1].split(' ')[3:-1])
    # print(password)
    s=[]
    for c in list(cmd.split('I'))[1:]:
        a = c.split(" ")[1:-1]

        x,y = int(a[0]),int(a[1])
        s = a[2:]

        for _ in range(y-1,-1,-1):
            password.insert(x,s[_])

        # password.insert(x,s[:y])

        # print(s)

    # print(password[:10])

    print("#",end='')

    for _ in range(10):
        ans += password[_] + ' '

    print(testcase,ans)
