N, M, x, y, K = list(map(int, input().split()))

MAP = [list(map(int, input().split())) for _ in range(N)]

command = list(map(int, input().split()))

dice = [0,0,0,0,0,0]


ni, nj = x, y
di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

for cmd in command:

    ni += di[cmd]
    nj += dj[cmd]

    if not (0 <= ni < N and 0 <= nj < M):
        ni -= di[cmd]
        nj -= dj[cmd]
        continue



    if cmd == 1:
        dice = [dice[2],dice[0],dice[5],dice[3],dice[4],dice[1]]
    elif cmd == 2:
        dice = [dice[1],dice[5],dice[0],dice[3],dice[4],dice[2]]
    elif cmd == 3:
        dice = [dice[4],dice[1],dice[2],dice[0],dice[5],dice[3]]
    elif cmd == 4:
        dice = [dice[3],dice[1],dice[2],dice[5],dice[0],dice[4]]

    bottom = dice[5] # 주사위의 바닥면 숫자
    top = dice[0] #주사위의 윗면 숫자

    print(top)
    if MAP[ni][nj] == 0:
        MAP[ni][nj] = bottom
    else:
        dice[5] = MAP[ni][nj]
        MAP[ni][nj] = 0