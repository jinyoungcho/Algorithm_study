N = int(input())

li = list(map(int, input().split()))

MAXI = 0

def dfs(n,lli,ans):
    global MAXI

    if n == 2:
        MAXI = max(MAXI, ans)
        return


    # print(list(range(1,n-1)))

    for _ in range(1,n-1):
        # print(_)
        #제거

        po_idx = _
        po_val = lli[_]

        temp = lli[_-1] * lli[_+1]

        lli.pop(po_idx)
        dfs(n-1,lli,ans+temp)
        lli.insert(po_idx,po_val)

        #복구

dfs(N,li,0)

print(MAXI)