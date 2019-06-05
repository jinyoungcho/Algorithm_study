N = int(input()) # <= 100

num_arc = int(input())

arc_dict = {}

visited = set()

for _ in range(num_arc):
    node_A, node_B = list(map(int, input().split()))

    if arc_dict.get(node_A) == None:
        arc_dict[node_A] = [node_B]
    else:
        arc_dict[node_A].append(node_B)

    if arc_dict.get(node_B) == None:
        arc_dict[node_B] = [node_A]
    else:
        arc_dict[node_B].append(node_A)

from collections import deque

def bfs():

    visited.add(1)
    q = deque()
    q.append(1)
    cnt = 0
    while(q):
        node = q.popleft()
        cnt += 1
        for nxt_node in arc_dict[node]:

            if nxt_node in visited:
                continue

            q.append(nxt_node)
            visited.add(nxt_node)

    print(cnt-1)

bfs()