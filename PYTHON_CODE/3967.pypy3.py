MAP = []

for _ in range(5):
    MAP.append(list(input()))

# print(MAP)

MAP2 = []

ij_li = []

num = 0

check=[]

visited = []

for i in range(5):
    for j in range(9):
        if MAP[i][j] == '.':
            MAP[i][j] = 0
        elif ord('A') <= ord(MAP[i][j]) <= ord('L'):
            visited.append(ord(MAP[i][j]) - ord('A') + 1)
            MAP[i][j] = ord(MAP[i][j])-ord('A') + 1


        else:
            MAP[i][j] = 0
            num += 1
            ij_li.append((i,j))
            check.append(False)

# for _ in range(5):
#     print(MAP[_])

def check_all():
    global flag
    if MAP[1][1]+MAP[1][3]+MAP[1][5]+MAP[1][7] != 26:
        return False
    if MAP[1][7]+MAP[2][6]+MAP[3][5]+MAP[4][4] != 26:
        return False
    if MAP[1][1]+MAP[2][2]+MAP[3][3]+MAP[4][4] != 26:
        return False
    if MAP[0][4]+MAP[1][3]+MAP[2][2]+MAP[3][1] != 26:
        return False
    if MAP[0][4]+MAP[1][5]+MAP[2][6]+MAP[3][7] != 26:
        return False
    if MAP[3][1]+MAP[3][3]+MAP[3][5]+MAP[3][7] != 26:
        return False

    flag = 1
    return True

flag = 0


def dfs(cnt,pos,visited):

    if cnt == num:

        if check_all():

            return

    for i in range(1,13):

        if i in visited:
            continue

        MAP[ij_li[pos][0]][ij_li[pos][1]] = i

        dfs(cnt+1,pos+1,visited + [i])

        if flag:
            return

        MAP[ij_li[pos][0]][ij_li[pos][1]] = -1

dfs(0,0,visited)
# print("-")

for i in range(5):
    for j in range(9):
        if MAP[i][j] == 0:
            print('.',end='')
        else:
            print(chr(MAP[i][j]+65-1), end='')
    print('')
# for _ in range(5):
#     print(MAP[_])

# print(ord('A'))