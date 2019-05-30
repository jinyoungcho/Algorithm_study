kloc, sloc, N = list(input().split())

N = int(N)
Kloc = [int(kloc[1])-1, ord(kloc[0]) - ord('A')]
Sloc = [int(sloc[1])-1, ord(sloc[0]) - ord('A')]

class object:
    def __init__(self,ij,name):
        self.i = ij[0]
        self.j = ij[1]
        self.name = name

king = object(Kloc,'king')
stone = object(Sloc,'stone')

move_dic = {
    'R'  : [ 0,  1],
    'L'  : [ 0, -1],
    'B'  : [-1,  0],
    'T'  : [ 1,  0],
    'RT' : [ 1,  1],
    'LT' : [ 1, -1],
    'RB' : [-1,  1],
    'LB' : [-1, -1]
}

for _ in range(N):

    cmd = input()

    di, dj = move_dic[cmd]

    #킹 움직여보기
    king.i += di
    king.j += dj

    if not (0 <= king.i < 8 and 0 <= king.j < 8):
        king.i -= di
        king.j -= dj

    #돌이 있다면 돌도 움직여보기
    if king.i == stone.i and king.j == stone.j:

        stone.i += di
        stone.j += dj

        # 돌이 밖으로 나간다면
        if not(0<= stone.i <8 and 0 <= stone.j <8):
            king.i -= di
            king.j -= dj

            stone.i -= di
            stone.j -= dj

print(chr(king.j+65)+str(king.i+1))
print(chr(stone.j+65)+str(stone.i+1))

