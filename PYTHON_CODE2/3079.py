# Binary Search

N, M = list(map(int, input().split()))

T = []

for _ in range(N):
    T.append(int(input()))


def check(time):

    temp = 0
    # print(time)
    for t in T:
        temp += time // t

    return temp >= M

def binary_search():

    st = 0
    ed = 1000000000000000000
    ans = 1000000000000000000
    while(st<=ed):

        md = (st+ed)//2

        if check(md):
            ed = md -1
            ans = min(ans,md)
        else:
            st = md + 1


    return ans

print(binary_search())