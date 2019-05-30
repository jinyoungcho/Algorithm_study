T = int(input())
N = 0
M = 0
MAP = []

di = [0,0,1,-1]
dj = [1,-1,0,0]

from collections import deque


def get_op_cost(k):
    return (k*k) + ((k-1) * (k-1))

def bfs(i,j,k):
    check = [[False] * N for _ in range(N)]
    q = deque()

    q.append((i,j,k)) # i,j,k
    num_house = MAP[i][j]
    check[i][j] = True

    while(q):

        i,j,k = q.popleft()
        # print(i,j,k)
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 > ni or 0 > nj or N <= ni or N <= nj or k <= 1:
                continue

            if check[ni][nj] == False:
                # print(ni, nj, k)
                check[ni][nj] = True
                q.append((ni, nj, k-1))
                num_house+=MAP[ni][nj]

    return num_house





def search(k,op_cost):


    num_house = 0

    for i in range(N):

        for j in range(N):

            cur_n = bfs(i, j, k)

            if (cur_n*M) - op_cost >= 0: # 손해가 아니면
                num_house = max(num_house, cur_n)

    return num_house

def simulate():

    temp_ans = 0

    for k in range(1, N+3):
        op_cost = get_op_cost(k)
        # print("k운영비용", k,op_cost)
        temp_ans = max(search(k,op_cost),temp_ans)

    return temp_ans


for t in range(1, T+1):
    N, M = list(map(int, input().split()))

    MAP = [list(map(int, input().split())) for _ in range(N)]

    ans = simulate()

    print("#",end="")
    print(t,ans)