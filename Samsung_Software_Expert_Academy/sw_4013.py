T = int(input())
K = 0
ans = 0
magnet_list = []
move_list=[]

check = []

from collections import deque

d_idx = [-1,1]

def get_ans():
    temp = 0
    if magnet_list[0][0] == 1:
        temp += 1
    if magnet_list[1][0] == 1:
        temp += 2
    if magnet_list[2][0] == 1:
        temp += 4
    if magnet_list[3][0] == 1:
        temp += 8
    return temp



def move_magnet(idx,k):

    q = deque()
    q.append((idx,k))
    check[idx] = True


    while(q):
        cur_idx,cur_k = q.popleft()
        cur_right = magnet_list[cur_idx][2]
        cur_left = magnet_list[cur_idx][6]

        # print(cur_idx, cur_k, cur_right, cur_left)

        for i in range(2):

            n_idx = cur_idx + d_idx[i]


            if 0 > n_idx or n_idx >= 4 or check[n_idx] == True:
                continue

            if n_idx > cur_idx:  # right magget

                if cur_right == magnet_list[n_idx][6]:
                    check[n_idx] = True
                    # q.append((n_idx, cur_k))
                elif cur_right != magnet_list[n_idx][6]:
                    check[n_idx] = True
                    q.append((n_idx, -cur_k))

            elif n_idx < cur_idx:  # left magnet

                if cur_left == magnet_list[n_idx][2]:
                    check[n_idx] = True
                    # q.append((n_idx, cur_k))
                elif cur_left != magnet_list[n_idx][2]:
                    check[n_idx] = True
                    q.append((n_idx, -cur_k))

        if cur_k == 1:
            magnet_list[cur_idx] = [magnet_list[cur_idx][-1]] + magnet_list[cur_idx][:-1]
        elif cur_k == -1:
            magnet_list[cur_idx] = magnet_list[cur_idx][1:] + [magnet_list[cur_idx][0]]

        # print(magnet_list[cur_idx])



def simulate():
    # print(magnet_list)
    global ans
    for idx,dir in move_list:
        # print("before", magnet_list)
        global check
        # print("-")
        check = [False] * 4
        move_magnet(idx-1,dir)
        # print(magnet_list)


    ans = get_ans()

for t in range(1,T+1):

    K = int(input())

    ans = 0

    magnet_list = [list(map(int,input().split())) for _ in range(4)]

    move_list = [list(map(int,input().split())) for _ in range(K)]

    check = [False] * 4
    simulate()

    print("#",end="")
    print(t,ans)
