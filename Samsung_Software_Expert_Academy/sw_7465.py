from collections import deque


def bfs(st):

    q = deque()

    q.append(st)

    visited.add(st)

    while q:

        st = q.popleft()

        for nxt_node in dict[st]:

            if nxt_node in visited:
                continue

            q.append(nxt_node)
            visited.add(nxt_node)

    # assert dict


T = int(input())
for t in range(1,T+1):
    ans = 0
    N, M = list(map(int, input().split()))
    dict = {}

    for _ in range(1,N+1):
        dict[_] = []

    for _ in range(M):

        node_i, node_j = list(map(int, input().split()))

        if dict.get(node_i) == None:
            dict[node_i] = [node_j]
        else:
            dict[node_i].append(node_j)

        if dict.get(node_j) == None:
            dict[node_j] = [node_i]
        else:
            dict[node_j].append(node_i)


    # print(dict)

    visited = set()
    cnt = 1
    # if M != 0:
    for n in range(1,N+1):
        # print(n)
        if n in visited:
            continue
        bfs(n)
        cnt += 1

    ans = cnt-1

    print('#',end='')
    print(t,ans)