from copy import deepcopy

N, M, D = list(map(int,input().split()))

monster_MAP = [list(map(int,input().split())) for _ in range(N)]
from itertools import combinations

class Monster:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.dead = False

mon_li = []
for i in range(N):
    for j in range(M):
        if monster_MAP[i][j] == 1:
            mon_li.append(Monster(i,j))


def simulate(ht):

    t = N

    hunter_list = []

    for num in ht:
        ht_i = N
        ht_j = num
        hunter_list.append((ht_i,ht_j))


    monster_list = deepcopy(mon_li)

    score = 0
    # print("------------")
    while(t):

        can_catch_mdx = [[],[],[]]

        for hdx,hunter in enumerate(hunter_list):
            for mdx,monster in enumerate(monster_list):
                if monster.dead:
                    continue
                else:
                    h_i, h_j = hunter
                    distance = abs(h_i - monster.i) + abs(h_j - monster.j)
                    if D >= distance:
                        can_catch_mdx[hdx].append((mdx,distance))

        #kill
        # print("")
        for can_li in can_catch_mdx:
            if can_li == []:
                continue
            asdf = sorted(can_li, key=lambda x: (x[1], monster_list[x[0]].j))

            mon_dx = asdf[0][0]

            if monster_list[mon_dx].dead == False:
                # print(mon_dx)
                score += 1

            monster_list[mon_dx].dead = True




        #move
        for monster in monster_list:
            if monster.dead == False:
                monster.i += 1
                if monster.i == N:
                    monster.dead=True

        # for _ in range(len(monster_list)):
        #     if monster_list[_].dead == False:
        #         print(_,end="")

        t-=1

    return score

MAXI = 0

# print(simulate([21,22,23]))

def dfs(li,idx,cnt):
    global MAXI
    if idx >= M:
        return
    if cnt == 3:
        MAXI = max(MAXI,simulate(li))
        return
    else:
        dfs(li+[idx+1], idx+1, cnt+1)
        dfs(li, idx+1, cnt)

dfs([],-1,0)


print(MAXI)