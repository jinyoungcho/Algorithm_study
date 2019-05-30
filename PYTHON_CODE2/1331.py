# https://www.acmicpc.net/problem/1331

# 간단한 시뮬레이션 문제

# 나이트의 이동을 확인하고

#   if 방문했던 칸이거나 /
#      벽을 나가서거나 /
#      마지막에 시작점으로 돌아올수 없다면!

        #print("Invalid")
    # else
        #print("Valid")

MAX = 36
move_li = []

# 8방향

di = [1,2,2,1,-1,-2,-2,-1]
dj = [-2,-1,1,2,2,1,-1,-2]

for _ in range(MAX):
    ip = input()

    j = ord(ip[0]) - ord('A')
    i = int(ip[1])-1

    move_li.append((i,j))

si,sj = move_li[0]
find = True

check = [[False]*6 for _ in range(6)]
check[si][sj] = True

for move in move_li[1:]:

    sample_next_li = []
    # print(sample_next_li)
    for k in range(8):
        ni = si+di[k]
        nj = sj+dj[k]

        sample_next_li.append((ni,nj))

    if check[move[0]][move[1]] == True:
        find = False
        break

    if move in sample_next_li:
        si,sj = move
        check[move[0]][move[1]] = True
    else:
        find = False
        break


sample_next_li = []
li,lj = move_li[-1]
for k in range(8):
    ni = si + di[k]
    nj = sj + dj[k]
    sample_next_li.append((ni, nj))

if move_li[0] not in sample_next_li:
    find = False



print("Valid" if find else "Invalid")