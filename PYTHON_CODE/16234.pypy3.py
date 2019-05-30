import copy

N, L, R = list(map(int, input().split()))
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

dict_for_nation = {}




from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(si,sj,conected_component):

    q = deque()
    check[si][sj] = conected_component
    q.append((si, sj))

    nation_li = [(si, sj)]

    while(q):

        i, j = q.popleft()

        for k in range(4):

            ni = i+di[k]
            nj = j+dj[k]

            if not (0 <= ni < N and 0 <= nj < N):
                continue

            if check[ni][nj] != -1:
                continue

            if not(L <= abs(MAP[i][j] - MAP[ni][nj]) <= R):
                # print((i, j), (ni, nj), MAP[i][j], MAP[ni][nj], abs(MAP[i][j] - MAP[ni][nj]))
                continue

            check[ni][nj] = conected_component
            q.append((ni, nj))
            nation_li.append((ni,nj))

    # print(nation_li)

    dict_for_nation[conected_component] = nation_li

    return dict_for_nation

ans = 0
while(True):
    check = [[-1] * N for _ in range(N)]

    dict_for_nation = {}

    cp = 0
    for i in range(N):
        for j in range(N):
            if check[i][j] == -1:
                dict_for_nation = bfs(i, j, cp)
                cp += 1

    # print(dict_for_nation)
    if len(dict_for_nation) == N*N:
        break

    for cp_num in dict_for_nation:

        population_cp = 0

        for nni, nnj in dict_for_nation[cp_num]:
            population_cp += MAP[nni][nnj]

        for nni, nnj in dict_for_nation[cp_num]:
            MAP[nni][nnj] = population_cp // len(dict_for_nation[cp_num])

    # for _ in range(N):
    #     print(MAP[_])

    ans += 1

print(ans)