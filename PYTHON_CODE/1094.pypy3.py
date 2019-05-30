X = int(input())

a = [64]

import heapq

temp = 0

while(True):

    if temp == X:
        break


    if sum(a) > X:

        mini_bar = heapq.heappop(a)

        nxt_bar = mini_bar // 2

        if nxt_bar > 0:

            heapq.heappush(a,nxt_bar)

            if sum(a) > X:
                continue
            else:
                heapq.heappush(a, nxt_bar)

    temp = sum(a)

print(len(a))