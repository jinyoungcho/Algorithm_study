ip = input()

from itertools import combinations

sample = ip

li = []

for comb in combinations((range(1,len(ip))),2):
    # print(comb)
    _0 = 0
    _1,_2 = comb

    a = ip[_0:_1]
    b = ip[_1:_2]
    c = ip[_2:]
    # print(a,b,c)
    a = a[::-1]
    b = b[::-1]
    c = c[::-1]

    # print(a,b,c)

    li.append(a+b+c)

li.sort()

print(li[0])