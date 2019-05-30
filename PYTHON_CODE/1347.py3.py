T = int(input())

string = input()

MAP = {}


di = [1,0,-1,0]
dj = [0,1,0,-1]

move = [(0,0)]
i = 0
j = 0
k = 0
for st in string:



     #남으로 시작
    # print(k)
    # print(i,j)
    if st == 'R':
        if k == 0:
            k = 3
        elif k == 1:
            k = 0
        elif k == 2:
            k = 1
        elif k == 3:
            k = 2

    elif st == 'L':
        if k == 0:
            k = 1
        elif k == 1:
            k = 2
        elif k == 2:
            k = 3
        elif k == 3:
            k = 0

    elif st == 'F':

        i += di[k]
        j += dj[k]

        move.append((i,j))

# print(move)


min_i = 1000
max_i = -1000

min_j = 1000
max_j = -1000


dic = {}
for i,j in move:

    dic[(i,j)] = '.'

    min_i = min(min_i, i)
    max_i = max(max_i, i)

    min_j = min(min_j,j)
    max_j = max(max_j,j)

# print(min_i, max_i)
# print(min_j, max_j)

# print(dic)

for i in range(min_i, max_i+1):
    for j in range(min_j, max_j+1):


        if (i,j) in dic:
            print(dic[(i,j)], end='')
        else:
            print("#",end='')
    print("")