
for t in range(1,11):
    input()

    ans = 0

    MAP = []
    temp = 0
    for _ in range(100):
        MAP.append(list(map(int,input().split())))
        temp = max(sum(MAP[_]),temp)

    MAP = list(zip(*MAP))

    for _ in range(100):
        temp = max(sum(MAP[_]),temp)

    a=0
    for i in range(100):
        a += MAP[i][i]
    temp = max(a,temp)

    a=0
    for i in range(100):
        a += MAP[i][99-i]
    temp = max(a,temp)

    ans = temp

    print('#',end='')
    print(t,ans)