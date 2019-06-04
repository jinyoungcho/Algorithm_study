# Binary Search with BFS or Dikstra

N, M = list(map(int, input().split()))

# MAP_dic = [[0] * N for _ in range(N)]

adj_list = {}
for _ in range(N):
    adj_list[_] = {}

for _ in range(M):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1

    if adj_list[a].get(b) == None:
        adj_list[a][b] = c
    else:
        adj_list[a][b] = max(adj_list[a][b], c)

    if adj_list[b].get(a) == None:
        adj_list[b][a] = c
        adj_list[b][a] = max(adj_list[b][a], c)
    # adj_list[a].append([b, c])
    # adj_list[b].append([b, c])

    # MAP_dic[a-1][b-1] = max(MAP_dic[a-1][b-1], c)
    # MAP_dic[b-1][a-1] = max(MAP_dic[b-1][a-1], c)

# print(adj_list)

goal_i, goal_j = list(map(int, input().split()))
goal_i -= 1
goal_j -= 1

from collections import deque

def bfs(weight):

    check = [False] * N

    q = deque()
    q.append(goal_i)
    check[goal_i] = True

    while(q):

        st = q.popleft()

        for next_node in adj_list[st]:

            if check[next_node]:
                continue

            if adj_list[st][next_node] == 0:
                continue

            if adj_list[st][next_node] < weight:
                continue

            if next_node == goal_j:
                return True

            q.append(next_node)
            check[next_node] = True

    return False

def binary_search():

    st = 1
    ed = 1000000000
    ans = 0

    while(st<=ed):
        # print(st, ed)
        md = (st+ed) // 2

        if bfs(md): #이 중량으로 보낼수 있다면
            #더 올려서 보내보자
            st = md+1
            ans = md

        else: #이 중량으로 보낼수 없다면
            ed = md-1 #올려서 보내보자

    return ans

print(binary_search())