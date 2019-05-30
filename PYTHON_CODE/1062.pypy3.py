from itertools import combinations

N, K = list(map(int, input().split()))
word = [input() for _ in range(N)]
for i in range(N):
    word[i] = set(word[i][4:-4])
"""
anta tica
a c i n t  --> 5
"""
if K < 5:
    print('0')

else:
    default = set(['a', 'c', 'i', 'n', 't'])
    alphabet = 'bdefghjklmopqrsuvwxyz'
    alphabet = list(alphabet)
    com_alphabet = combinations(alphabet, K-5)

    maxi = 0
    for can in com_alphabet:
        # print("before",can)

        can = set(can).union(default)

        # print("after",can)

        cnt = 0
        for w in word:
            if w & can == w:
               cnt += 1
        maxi = max(maxi, cnt)

    print(maxi)