N,M = list(map(int, input().split()))

MAP = [[0]*M for _ in range(N)]

queen_list = list(map(int, input().split()))

knight_list = list(map(int,input().split()))

pawn_list = list(map(int,input().split()))

num_queen = queen_list[0]
queen_ = []
sam_li = []
if len(queen_list) != 1:
    for ij in queen_list[1:]:
        if len(sam_li) == 2:
            sam_li = []
        if len(sam_li) == 0:
            sam_li.append(ij-1)
        elif len(sam_li) == 1:
            sam_li.append(ij-1)
            queen_.append(sam_li)

# print(queen_)


num_knight = knight_list[0]
knight_ = []

sam_li = []
if len(knight_list) != 1:
    for ij in knight_list[1:]:
        if len(sam_li) == 2:
            sam_li = []
        if len(sam_li) == 0:
            sam_li.append(ij-1)
        elif len(sam_li) == 1:
            sam_li.append(ij-1)
            knight_.append(sam_li)

num_pawn = pawn_list[0]
pawn_ = []

sam_li = []
if len(pawn_list) != 1:
    for ij in pawn_list[1:]:
        if len(sam_li) == 2:
            sam_li = []
        if len(sam_li) == 0:
            sam_li.append(ij-1)
        elif len(sam_li) == 1:
            sam_li.append(ij-1)
            pawn_.append(sam_li)


check = [[-1]* M for _ in range(N)]

#queen
for i,j in queen_:
    check[i][j] = 0
for i,j in knight_:
    check[i][j] = 0
for i,j in pawn_:
    check[i][j] = 0

# print("setting")
# for _ in range(N):
#     print(check[_])


q_di = [-1,-1,-1,0,1,1,1,0]
q_dj = [-1,0,1,1,1,0,-1,-1]

for i,j in queen_:

    for k in range(8):
        ni = i
        nj = j
        while(True):

            ni += q_di[k]
            nj += q_dj[k]

            if not (0<= ni < N and 0 <= nj < M):
                break

            if check[ni][nj] == 0: #뭐가 가로박고있다면
                break

            check[ni][nj] = 10

# print("queen")
# for _ in range(N):
#     print(check[_])


k_di = [-1,-2,-2,-1,1,2,2,1]
k_dj = [-2,-1,1,2,2,1,-1,-2]

for i,j in knight_:

    for k in range(8):

        ni = i + k_di[k]
        nj = j + k_dj[k]

        if not (0 <= ni < N and 0 <= nj < M):
            continue


        check[ni][nj] = 10

# print("night")
# for _ in range(N):
#     print(check[_])

cnt = 0

for i in range(N):
    for j in range(M):

        if check[i][j] ==-1:

            cnt+=1

# print(queen_)
# print(knight_)
# print(pawn_)

print(cnt)
