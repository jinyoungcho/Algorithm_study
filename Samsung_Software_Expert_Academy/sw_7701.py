# Sort

from functools import cmp_to_key

T = int(input())

def cmp(x,y):

    if len(x)==len(y):
        return x < y
    else:
        return len(x) < len(y)

for t in range(1,T+1):

    N = int(input())
    name_list = []
    for _ in range(N):
        name_list.append(input())

    name_list.sort(key=lambda x:(len(x),x))
    set_for_check=set()

    print("#",end='')
    print(t)

    for stri in name_list:
        if stri not in set_for_check:
            print(stri)
            set_for_check.add(stri)



