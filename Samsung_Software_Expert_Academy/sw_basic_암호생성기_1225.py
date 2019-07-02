from collections import deque

for _ in range(10):
    t = int(input())

    q = deque()

    q.extend(list(map(int,input().split())))

    minus = 1

    while( True ):

        num = q.popleft()

        if num-minus > 0:

            q.append(num-minus)

            minus+=1

            if minus == 6:
                minus = 1

        else:
            q.append(0)
            break

    # print(q)

    print("#",end='')
    print(t,end=' ')
    while(q):
        print(q.popleft(), end=' ')
    print()