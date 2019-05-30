N, M = list(map(int, input().split()))

check = {}

dict = {}

friend = set()

for _ in range(M):

    i, j = list(map(int, input().split()))

    friend.add(i)
    friend.add(j)

    check[i] = False
    check[j] = False

    if i in dict:
        dict[i].append(j)
    else:
        dict[i]=[j]

    if j in dict:
        dict[j].append(i)
    else:
        dict[j]=[i]


def dfs(idx,cnt):
    global find

    if find == True:
        return

    if cnt == 5:
        find = True
        return
    else:

        for _ in dict[idx]:

            if check[_] == False:
                check[_] = True

                dfs(_, cnt+1)

                check[_] = False
find = False
for k in friend:
    if find:
        break
    check[k] = True
    dfs(k, 1)
    check[k] = False

print(1 if find else 0)