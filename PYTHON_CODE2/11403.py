# 플로이드 와샬 알고리즘 공부합시다..!

# dfs를 이용해서 첫 시작 노드부터 마지막 방문할수 있느 노드까지 체크해주기

N = int(input())

MAP = []

for _ in range(N):
    MAP.append(list(map(int,input().split())))

dict = {}

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:

            if dict.get(i) == None:
                dict[i] = [j]
            else:
                dict[i].append(j)

# print(dict)

from sys import setrecursionlimit

setrecursionlimit(1000000)

def dfs(pr,start):

    for node in dict[start]:
        # print(pr,st,node, check[start][node])

        if check[start][node] == 0:
            check[start][node] = 1
            # print("~?")
            if dict.get(node) != None:
                dfs(pr,node)
        check[pr][node] = 1

ans = [[0] * N for _ in range(N)]

for st in dict.keys():
    check = [[0] * N for _ in range(N)]
    dfs(st,st)

    for i in range(N):
        for j in range(N):
            if check[i][j]==1:

                ans[i][j] = 1

for i in range(N):
    for j in range(N):
        print(ans[i][j],end=' ')
    print()
