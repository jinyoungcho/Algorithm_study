T = int(input())

from collections import deque

for t in range(1,T+1):

    num_paper, goal = list(map(int,input().split()))

    papers = list(map(int,input().split()))

    q = deque()

    for i in range(num_paper):
        q.append((i, papers[i]))

    # print(q)
    tt = 0
    while(True):
        # print(q)
        idx,paper = q.popleft()

        check = False

        for jdx, japer in list(q):
            if japer > paper:
                check = True
                break

        if check:
            q.append((idx,paper))
        else:
            tt += 1
            if idx == goal:
                print(tt)
                break