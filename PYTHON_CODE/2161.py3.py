a = int(input())

from collections import deque

q = deque(list(range(1,a+1)))

while(q):

    print(q.popleft(),end=" ")

    if q:

        q.append(q.popleft())

