N1, N2 = list(map(int,input().split()))

g1 = list(input())
g1.reverse()
g2 = list(input())

T = int(input())

Ant_list = []


class Ant:

    def __init__(self, name, loc, dir):
        self.name = name
        self.loc = loc
        self.dir = dir

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
loc = 0
for ant in g1:
    Ant_list.append(Ant(ant,loc,1))
    loc += 1

for ant in g2:
    Ant_list.append(Ant(ant,loc,-1))
    loc += 1

# print(Ant_list)

while(T):

    swap_li=[]
    adx = 0
    while(adx < N1+N2-1):
        # print(adx)

        if not (0<= adx+Ant_list[adx].dir <= N1+N2-1):
            adx+=1
            continue

        if Ant_list[adx].dir != Ant_list[adx+Ant_list[adx].dir].dir:
            swap_li.append((adx,adx+Ant_list[adx].dir))
            adx+=1

        adx+=1

    # print(swap_li)

    for i,j in swap_li:
        Ant_list[i],Ant_list[j] = Ant_list[j],Ant_list[i]


    # print(Ant_list)
    T-=1

for _ in Ant_list:
    print(_.name,end='')