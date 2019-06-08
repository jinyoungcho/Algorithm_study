# 3
# 4 10
# 1 2 3 4
# 5 7
# 14 15 12 17 17
# 5 1
# 10 10 10 10 10


# Binary_Search

T = int(input())

def check(md,N,M):
    so_far_tree = 0
    for tree in li:
        if tree > md:
            so_far_tree += tree-md

        if so_far_tree > M:
            return 0

    if so_far_tree == M:
        return 1
    else:
        return -1

def binary_search(li,N,M):

    st = 0
    ed = li[0]
    aaa = 0
    while(st<=ed):
        md = (st+ed) // 2
        # print(md)
        c = check(md,N,M)

        if c == -1:
            ed = md-1
        elif c == 0:
            st = md+1
            aaa = max(aaa,md)
            # print('too many',aaa)
        else:
            return md

    return aaa

for t in range(1,T+1):
    ans = 0

    N, M = list(map(int, input().split()))

    li = list(map(int, input().split()))

    li.sort(reverse=True)

    # print(li)

    ans = binary_search(li,N,M)


    print("#",end='')
    print(t,ans)