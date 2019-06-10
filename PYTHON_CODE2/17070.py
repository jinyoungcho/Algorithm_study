N = int(input())

MAP = []

for _ in range(N):
    MAP.append(list(map(int,input().split())))

# state = 0
# 가로 0 -> 0, 2
di = [0, 1]
dj = [1, 1]

# 세로 1 -> 1, 2
di2 = [1, 1]
dj2 = [0, 1]

# 대각선 2 -> 0,1,2
di3 = [0, 1, 1]
dj3 = [1, 0, 1]

cnt = 0

def dfs(i,j,state):
    global cnt
    if i== N-1 and j == N-1:
        cnt += 1
        return

    if state == 0: #가로
        n_state = 0
        ni,nj = i + di[0], j+dj[0]
        if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != 1:
            dfs(ni,nj,n_state)

        n_state = 2
        ni, nj = i + di[1], j+dj[1]

        if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != 1:
            if 0 <= j+1 < N and 0 <= i+1 < N:
                if MAP[i][j+1] == 0 and MAP[i+1][j] == 0:
                    dfs(ni, nj, n_state)

    elif state == 1: #세로
        n_state = 1
        ni,nj = i + di2[0], j+dj2[0]
        if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != 1:
            dfs(ni,nj,n_state)

        n_state = 2
        ni, nj = i + di2[1], j+dj2[1]
        if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != 1:
            if 0<= i+1<N and 0<=j+1<N:
                if MAP[i+1][j] == 0 and MAP[i][j+1] == 0:
                    dfs(ni,nj,n_state)

    elif state == 2: #대각선
        n_state = 0
        ni,nj = i + di3[0], j+dj3[0]
        if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != 1:
            dfs(ni, nj, n_state)

        n_state = 1
        ni,nj = i + di3[1], j+dj3[1]
        if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != 1:
            dfs(ni, nj, n_state)

        n_state = 2
        ni, nj = i + di3[2], j+dj3[2]
        if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != 1:
            if 0<= i+1<N and 0<=j+1<N:
                if MAP[i+1][j] == 0 and MAP[i][j+1] == 0:
                    dfs(ni, nj, n_state)

dfs(0,1,0)

print(cnt)