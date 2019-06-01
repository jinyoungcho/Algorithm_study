N,M = 5,5

MAP = []

for _ in range(N):
    MAP.append(list(input()))

check = [False]*25

ans = 0

from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs(li):

    check = [False] * 25

    i,j = li[0] // 5 , li[0] % 5

    q = deque()

    q.append((i,j))

    check[li[0]] = True

    while(q):
        # print(q)
        i,j = q.popleft()

        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]

            if not (0<= ni < N and 0 <= nj < M):
                continue

            if (ni*5 + nj) not in li:
                continue

            if check[(ni*5 + nj)]:
                continue

            q.append((ni,nj))
            check[(ni*5 + nj)] = True


    for loc in li:
        if check[loc] == False:
            return False

    return True




def backtracking(S,Y,cnt,idx,li):
    global ans
    if Y > 3:
        return

    if cnt == 7:
        # print("~?")
        if bfs(li):
            # print("~?")
            ans += 1

        return

    for _ in range(idx,25):

        if check[_]:
            continue

        check[_] = True

        if MAP[_//5][_%5] == 'Y':

            backtracking(S,Y+1,cnt+1,_,li+[_])

        else:

            backtracking(S+1,Y,cnt+1,_,li+[_])

        check[_] = False


backtracking(0,0,0,0,[])

print(ans)