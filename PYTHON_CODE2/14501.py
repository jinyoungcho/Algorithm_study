# dp or dfs

#조금 까다로웠다..!

N = int(input())

time_map = []
price_map = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    time_map.append(a)
    price_map.append(b)

check = [False] * N
MAXI = 0
def dfs(idx, score, visited, price_visited):
    global MAXI
    # print(visited)
    # print(idx)
    if idx >= N:
        # MAXI = max(MAXI, score)
        if score > MAXI:
            # print(visited)
            # print(price_visited)
            MAXI = score
        return

    for _ in range(idx,N):

        if check[_] == True:
            continue

        if _ + time_map[_] > N:
            MAXI = max(score,MAXI)
            continue

        #선택했쯍
        check[_] = True
        dfs(_+time_map[_], score + price_map[_], visited + [_], price_visited + [price_map[_]])
        check[_] = False

dfs(0,0,[],[])

print(MAXI)