T = int(input())

di = [1,-1,0,0]
dj = [0,0,-1,1]
atom_dic = {}
atom_list = []

def move():
    global atom_list, atom_dic
    atom_dic = {}

    for atom in atom_list:

        y,x,dir,k = atom

        ny,nx = y + di[dir], x + dj[dir]

        if (ny,nx) not in atom_dic:
            atom_dic[(ny,nx)] = [(dir,k)]
        else:
            atom_dic[(ny,nx)].append((dir,k))


def delete_and_get_score():
    global atom_list, atom_dic
    atom_list = []

    sc = 0

    for key in atom_dic.keys():


        if len(atom_dic[key]) >= 2:

            for atom in atom_dic[key]:

                sc += atom[1]

        else:
            atom_list.append((key[0],key[1],atom_dic[key][0][0],atom_dic[key][0][1]))

    return sc

def simulate():
    global atom_list
    temp = 0

    for _ in range(4000):

        move()

        temp += delete_and_get_score()

        if len(atom_list) == 0:
            break

    return temp

for t in range(1,T+1):
    N = int(input())
    atom_dic = {}
    atom_list = []
    for i in range(N):
        x, y, dir, k = list(map(int,input().split()))
        x *= 2
        y *= 2
        atom_list.append((y, x, dir, k))

    ans = simulate()

    print("#",end="")
    print(t, ans)