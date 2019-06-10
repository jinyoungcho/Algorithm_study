li = [1,2,3]

T = int(input())

def dfs(now):
    global cnt
    if now == goal:
        cnt += 1

    for num in li:

        if now+num > goal:
            continue

        dfs(now+num)

for t in range(T):

    goal = int(input())
    cnt = 0
    dfs(0)

    print(cnt)