A, B = list(input().split())

min_len = len(A)
max_len = len(B)

A=int(A)
B=int(B)
ans = 0
def dfs(string,cnt):
    global ans
    if cnt > max_len:
        return

    if string !='':
        if A<= int(string) <=B:
            ans += 1

    dfs(string+'4',cnt+1)
    dfs(string+'7',cnt+1)

dfs('',0)

print(ans)