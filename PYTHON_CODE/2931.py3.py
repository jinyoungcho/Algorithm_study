R, C = list(map(int, input().split()))

MAP = [list(input()) for _ in range(R)]


# bitmask for direction
dict = {          # n,s,w,e
        '|': 12,  # 1,1,0,0
        '-': 3,   # 0,0,1,1
        '1': 5,   # 0,1,0,1
        '2': 9,   # 1,0,0,1
        '3': 10,  # 1,0,1,0
        '4': 6,   # 0,1,1,0
        '+': 15,  # 1,1,1,1
        'M': 15,  # 1,1,1,1
        'Z': 15,  # 1,1,1,1
        '.': 0,   # 0,0,0,0
        }

dict2 = {
    12:'|',
    3:'-',
    5:'1',
    9:'2',
    10:'3',
    6:'4',
    15:"+"
}

Mi, Mj = 0, 0
Gi, Gj = 0, 0

for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'M':
            Mi = i
            Mj = j
        elif MAP[i][j] == 'Z':
            Gi = i
            Gj = j

M = (Mi,Mj)
G = (Gi,Gj)


from collections import deque

di = [0,0,1,-1] #동 서 남 북
dj = [1,-1,0,0]

MAP2 = [[dict[MAP[i][j]] for j in range(C)] for i in range(R)]



def bfs(si,sj):

    q = deque()
    q.append((si,sj))
    while(q):
        i, j = q.popleft()

        bit = MAP2[i][j]

        for k in range(4):

            if MAP2[i][j] == 0:
                break

            ni, nj = i+di[k], j+dj[k]

            if not(0 <= ni < R and 0 <= nj < C):
                continue

            if MAP[ni][nj] == '.':
                continue

            nbit=dict[MAP[ni][nj]]

            if k == 0:#동
                if bit & 1 and nbit & 2:
                    MAP2[i][j] -= 1
                    MAP2[ni][nj] -= 2
            elif k == 1:#서
                if bit & 2 and nbit & 1:
                    MAP2[i][j] -= 2
                    MAP2[ni][nj] -= 1
            elif k == 2:#남
                if bit & 4 and nbit & 8:
                    MAP2[i][j] -= 4
                    MAP2[ni][nj] -= 8
            elif k == 3:#북
                if bit & 8 and nbit & 4:
                    MAP2[i][j] -= 8
                    MAP2[ni][nj] -= 4

            if (i,j) == M or (i,j) == G:
                MAP2[i][j] = 0

            if MAP2[ni][nj] != 0:
                q.append((ni,nj))
bfs(Mi,Mj)
bfs(Gi,Gj)

# MAP2[Mi][Mj] = 0
# MAP2[Gi][Gj] = 0


asdf = []
for i in range(R):
    for j in range(C):
        if MAP2[i][j] != 0:
            asdf.append((i,j,MAP2[i][j]))


# for _ in range(R):
#     print(MAP2[_])


fi,fj,fk = 0,0,0
for i,j,k in asdf:
    # print(i,j,k)
    if k == 1:
        fi = i
        fj = j+1
        fk += 2
    elif k == 2:
        fi = i
        fj = j-1
        fk += 1
    elif k == 4:
        fi = i+1
        fj = j
        fk += 8
    elif k == 8:
        fi = i-1
        fj = j
        fk += 4

    # fk += k

print(fi+1,fj+1,dict2[fk])