check = [0] * 100001

from collections import deque

A,B,N,M = list(map(int,input().split()))

q = deque()

q.append(N)

check[N] = 1


while(q):

    now = q.popleft()

    if now == M:
        break

    next_loc = now - 1
    next_loc2 = now + 1
    next_loc3 = now + A
    next_loc4 = now - A
    next_loc5 = now * A
    next_loc6 = now + B
    next_loc7 = now - B
    next_loc8 = now * B

    next_li = [next_loc,next_loc2,next_loc3,
               next_loc4, next_loc5, next_loc6, next_loc7, next_loc8]

    for k in range(8):

        next_now = next_li[k]

        if not ( 0 <= next_now < 100001 ):
            continue

        if check[next_now] != 0:
            continue

        check[next_now] = check[now] + 1
        q.append(next_now)

print(check[M]-1)