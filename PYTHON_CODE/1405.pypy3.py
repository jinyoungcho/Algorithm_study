di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N_prob = list(map(int,input().split()))

N = N_prob[0]

def fuc(x):
    return x/100


prob = list(map(fuc, N_prob[1:]))

res = 0

def dfs(i,j,cnt,visited,pb):
    global res
    if cnt == N:
        # print(pb)
        res += pb
        return

    else:

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]

            if (ni,nj) in visited:
                continue

            visited.add((ni,nj))
            dfs(ni,nj,cnt+1,visited,pb * prob[k])
            visited.remove((ni,nj))

visited = set()
visited.add((0,0))
dfs(0,0,0,visited,1)

print(res)