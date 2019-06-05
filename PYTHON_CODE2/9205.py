#folyd washall

T = int(input())

from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for t in range(1, T+1):

    N = int(input())  # 0 <= n <= 100
    loc_dict = {}
    loc_li = []
    for _ in range(N+2):
        x, y = list(map(int, input().split()))
        loc_li.append((x, y))

    for x, y in loc_li:
        for x2, y2 in loc_li:
            if x == x2 and y == y2:
                continue
            if loc_dict.get((x,y)) == None:
                loc_dict[(x, y)] = [(x2, y2)]
            else:
                loc_dict[(x, y)].append((x2, y2))

    q = deque()

    q.append((loc_li[0][0], loc_li[0][1], 1000))

    visited = {loc_li[0]}

    while(q):
        i, j, bear = q.popleft()
        # print(i,j,bear)
        for next_loc in loc_dict[(i, j)]:
            # print(next_loc)
            ni = next_loc[0]
            nj = next_loc[1]
            if (ni, nj) in visited:
                continue

            if abs(i-ni) + abs(j-nj) > bear:
                continue

            n_bear = bear - (abs(i-ni) + abs(j-nj))
            #남은맥주
            if (ni,nj) in loc_li[1:-1]:
                n_bear = 1000
                # remain = n_bear % 50
                #
                # if remain == 0:
                #     n_bear = 1000
                # else:
                #     n_bear = 1000 - 50 + remain

            q.append((ni,nj,n_bear))
            visited.add((ni,nj))

    # print(visited)

    print('happy' if loc_li[-1] in visited else 'sad')