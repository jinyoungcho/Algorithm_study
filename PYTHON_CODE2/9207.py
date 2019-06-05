import copy
#back tarcking!

def dfs(cnt, MAP1):
    global o, res
    c = False

    for i in range(5):
        for j in range(9):
            # print(i,j)
            if MAP1[i][j] == 'o':
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    ni2, nj2 = i + (2*di[k]), j + (2*dj[k])
                    if not (0 <= ni < 5 and 0 <= nj < 9) or not(0 <= ni2 < 5 and 0 <= nj2 < 9):
                        # print("?")
                        continue
                    if not(MAP1[ni][nj] == 'o') or not(MAP1[ni2][nj2] == '.'):
                        continue

                    c = True
                    MAP2 = copy.deepcopy(MAP1)
                    MAP2[i][j] = '.'
                    MAP2[ni][nj] = '.'
                    MAP2[ni2][nj2] = 'o'

                    dfs(cnt + 1, MAP2)
    if c == False:

        num_o = 0
        for i in range(N):
            for j in range(M):
                if MAP1[i][j] == 'o':
                    num_o += 1
        if num_o < o:
            o = num_o
            res = cnt
        elif num_o == o and cnt < res:
            res = cnt
    return

T = int(input())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for t in range(T):

    MAP = []
    N,M = 5,9
    for _ in range(N):
        MAP.append(list(input()))

    o,res = 100000,100000

    dfs(0,MAP)

    print(o,res)
    if t != T-1:
        input()