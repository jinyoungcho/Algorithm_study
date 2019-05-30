N, M = list(map(int, input().split()))

sadari = {}

bam = {}

for _ in range(N):
    a,b = list(map(int, input().split()))
    sadari[a]=b

for _ in range(M):
    a,b = list(map(int, input().split()))
    bam[a] = b

MINI = 1000000

# import sys
# sys.setrecursionlimit(100000)

visited = []

def dfs(st,cnt):
    global MINI, visited

    if st >= 100:
        MINI = min(MINI,cnt)
        return
    elif (st,cnt) in visited:
        return
    elif cnt > MINI:
        return
    elif cnt > 100:
        return
    else:
        # print(st,cnt)
        visited.append((st,cnt))

        if st in sadari:
            st = sadari[st]

        elif st in bam:
            st = bam[st]

        for k in range(1,7):
            dfs(st+k, cnt+1)


dfs(1,0)

print(MINI)