T = int(input())


def check_pass(cur_MAP):
    for j in range(W):  # j
        temp_cell = cur_MAP[0][j]
        cnt = 1
        for i in range(1, D):  # i
            if temp_cell == cur_MAP[i][j]:
                cnt += 1
            else:
                cnt = 1
                temp_cell = cur_MAP[i][j]
            if cnt == K:
                break
            if i == D - 1:  ###########################
                return False
    return True


def dfs(cnt, idx):
    global MINI
    global MAP

    if idx == D:
        if check_pass(MAP):
            MINI = min(cnt, MINI)
    elif cnt > MINI:  ###########################
        return
    else:
        MAP_j = MAP[idx][:]
        MAP[idx] = fiil0or1[0]
        dfs(cnt + 1, idx + 1)
        MAP[idx] = fiil0or1[1]
        dfs(cnt + 1, idx + 1)
        MAP[idx] = MAP_j
        dfs(cnt, idx + 1)


for t in range(1, T + 1):
    D, W, K = list(map(int, input().split()))
    MAP = [list(map(int, input().split())) for _ in range(D)]
    MINI = D
    fiil0or1 = ([0] * W, [1] * W)
    # print(MAP)

    dfs(0, 0)

    ans = MINI
    print("#", end="")
    print(t, ans)