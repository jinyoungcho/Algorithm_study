N,M = list(map(int,input().split()))


cmd_li = [0] * N
dice_li = [0] * M

for _ in range(N):
    cmd_li[_] = int(input())

for _ in range(M):
    dice_li[_] = int(input())

# print(cmd_li)

now_loc = 0
t = 0

for dice in dice_li:

    t += 1

    now_loc += dice

    if now_loc >= N-1:
        print(t)
        break

    now_loc += cmd_li[now_loc]

    if now_loc >= N-1:
        print(t)
        break