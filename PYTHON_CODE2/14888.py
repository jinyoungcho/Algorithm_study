#dfs 이용한 완전탐색 문제 // 마이너스 나눗샘 조심할것

N = int(input()) # 2 <= N <= 11

Arr = list(map(int, input().split()))

op_Arr = list(map(int, input().split()))


MAXI = -1000000000
MINI = 1000000000

def cal(visited):

    global MAXI, MINI

    temp = Arr[0]

    # if visited == [1, 3, 0, 0, 2]:

    for i in range(N - 1):

        op = visited[i]

        if op == 0:  # +
            temp = temp + Arr[i + 1]
        elif op == 1:  # -
            temp = temp - Arr[i + 1]
        elif op == 2:  # x
            temp = temp * Arr[i + 1]
        elif op == 3:  # /

            if temp > 0:

                temp = temp // Arr[i + 1]

            else:

                temp = -temp // Arr[i + 1]
                temp = -temp

        # print(temp)

    MAXI = max(MAXI,temp)
    MINI = min(MINI,temp)

def dfs(cnt,visited):

    if cnt == N-1:
        # print(visited)
        cal(visited)

        return

    for op_idx in range(4):

        if not op_Arr[op_idx] > 0:
            continue

        op_Arr[op_idx] -= 1
        dfs(cnt+1, visited + [op_idx])
        op_Arr[op_idx] += 1

dfs(0,[])

print(MAXI)
print(MINI)