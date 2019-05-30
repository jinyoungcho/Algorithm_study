a = int(input())

from collections import deque

q = deque(list(range(1,a+1)))

while(q):

    a = q.popleft()

    if q:
        q.append(q.popleft())
    else:
        print(a)