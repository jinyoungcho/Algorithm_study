T = int(input())

import sys
from collections import deque
for _ in range(T):

    string = input()

    res = []
    idx = 0
    cur = 0

    st1 = deque()
    st2 = deque()

    while(idx != len(string)):

        ip = string[idx]
        # print(ip)
        if ip == "<":
            if st1:
                st2.appendleft(st1.pop())
        elif ip == '>':
            if st2:
                st1.append(st2.popleft())
        elif ip == '-':
            if st1:
                st1.pop()
        else:
            st1.append(ip)

        idx += 1

    print(''.join(st1+st2))