
di = [1,1,-1,-1]
dj = [1,-1,-1,1]


def dfs(i,j,k):
    global ans,si,sj,N

    for z in range(2): #z == 0 -> 원래방향 // z == 1 -> 우회전
        if k + z == 4:
            return
        ni = i+di[k+z]
        nj = j+dj[k+z]

        if not(0<=ni<N and 0<=nj<N): # 범위가 벗어났다면..!
            continue

        if ni == si and nj == sj: # 시작점으로 다시왔어요!
            # print("???")
            ans = max(ans, sum(visited))
            return
        if ni <= si and nj <= sj: #왼쪽 위로 벗어났다면 더이상 탐색할 필요가 없죠 뒤에서 했으니
            continue
        if visited[MAP[ni][nj]]==1: #먹어봤던 디져트 라면 탐색할 필요가 없어요!
            continue

        #모든 조건을 넘어왔다면
        visited[MAP[ni][nj]] = 1
        dfs(ni,nj,k+z)
        visited[MAP[ni][nj]] = 0

T = int(input())
for t in range(1,T+1):
    ans = -1
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * 101
    for i in range(N-2):
        for j in range(1, N-1):
            si = i
            sj = j
            visited[MAP[i][j]] = 1
            dfs(i,j,0)
            visited[MAP[i][j]] = 0

    print("#",end="")
    print(t,ans)