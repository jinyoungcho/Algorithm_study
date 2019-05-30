from collections import deque

N,M = list(map(int,input().split()))

dq = deque(list(range(1,N+1)))

g_li = list(map(int,input().split()))


idx = 0
cnt = 0

while(idx < M):

    g = g_li[idx]

    gdx = dq.index(g)

    if gdx == 0:
        dq.popleft()
        idx += 1

    else:

        if gdx > (len(dq)//2):
            dq.appendleft(dq.pop())

        else:
            dq.append(dq.popleft())

        cnt += 1
print(cnt)