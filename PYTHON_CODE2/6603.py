# https://www.acmicpc.net/problem/6603

# 완전탐색 -> 순열,조합

from itertools import combinations

while(True):

    ip = list(map(int,input().split()))

    if ip[0] == 0:
        break

    for comb in combinations(ip[1:], r=6):

        for num in comb:
            print(num, end=' ')
        print('')
    print('')