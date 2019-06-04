# suffix

N, H = list(map(int, input().split()))

is_stalagmite = True

# 석순
stalagmite = [0 for _ in range(H + 1)]
# 종유석
stalactite = [0 for _ in range(H + 1)]

# 석순 누적
accum_stalagmite = [0 for _ in range(H + 1)]
# 종유석 누적
accum_stalactite = [0 for _ in range(H + 1)]

move_able = [0 for _ in range(H + 1)]

for _ in range(N):
    i = int(input())
    if is_stalagmite:
        stalagmite[i] += 1
    else:
        stalactite[i] += 1
    is_stalagmite = not is_stalagmite

accum_stalagmite[H] = stalagmite[H]
accum_stalactite[H] = stalactite[H]
for i in range(H - 1, 0, -1):
    accum_stalagmite[i] = stalagmite[i] + accum_stalagmite[i + 1]
    accum_stalactite[i] = stalactite[i] + accum_stalactite[i + 1]


print(accum_stalagmite,accum_stalactite)

mn = 20000001
c = 1
for i in range(1, H + 1):
    move_able[i] = accum_stalagmite[i] + accum_stalactite[H - i + 1]

    if move_able[i] < mn:
        mn = move_able[i]
        c = 1
    elif move_able[i] == mn:
        c += 1


print(mn, c)