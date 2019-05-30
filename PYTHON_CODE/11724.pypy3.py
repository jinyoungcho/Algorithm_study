N, M = list(map(int, input().split()))

dict = {}
check_dic={}
for _ in range(M):

    i, j = list(map(int, input().split()))

    check_dic[i] = False
    check_dic[j] = False

    if i in dict:
        dict[i].append(j)
    else:
        dict[i] = [j]

    if j in dict:
        dict[j].append(i)
    else:
        dict[j] = [i]

from collections import deque

def bfs(node):

    q = deque()

    q.append(node)
    check_dic[node] = True

    while(q):

        node = q.popleft()

        for nxt_node in dict[node]:

            if check_dic[nxt_node]:
                continue

            else:

                check_dic[nxt_node] = True
                q.append(nxt_node)
cnt = 0
for key in range(1,N+1):

    if key not in check_dic:
        cnt += 1

    elif check_dic[key] == False:
        cnt += 1
        bfs(key)

print(cnt)