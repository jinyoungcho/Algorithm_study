topni = []

for _ in range(4):
    topni.append(list(map(int, list(input()))))

N = int(input())


def move(n, dir):
    top = topni[n]
    if dir == 1: #시계방향
        top.insert(0, top.pop(7))
    elif dir == -1: #반시계방향
        top.insert(7, top.pop(0))

dk = [-1,1] # 좌, 우
from collections import deque
def bfs(n_,dir):
    q = deque()
    q.append((n_,dir))
    check[n_] = True

    move_list = []

    while(q):
        n_,dir = q.popleft()
        # print(n_,dir)
        # print(check)
        move_list.append((n_,dir))
        for k in range(2):
            n_n = n_+dk[k]

            if not (0 <= n_n < 4):
                continue

            if check[n_n] == True:
                continue

            if k == 0: #좌
                # print("check", topni[n_][6], topni[n_n][2])
                if topni[n_][6] != topni[n_n][2]:
                    q.append((n_n,-dir))
                    check[n_n] = True
            elif k == 1: #우
                if topni[n_][2] != topni[n_n][6]:
                    q.append((n_n,-dir))
                    check[n_n] = True

    return move_list



for _ in range(N):
    n, dir = list(map(int, input().split()))

    n -= 1
    check = [False] * 4
    move_list = bfs(n,dir)

    # print(move_list)



    for nnnn, dddd in move_list:

        move(nnnn,dddd)

    # print(topni)



ans = 0
for tdx, top in enumerate(topni):
    # print(top)
    if top[0] == 1: #N극이면
        # print(1 << tdx)
        ans += 1<<tdx

# print(topni)

print(ans)