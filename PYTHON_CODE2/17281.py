from itertools import permutations

def run(P):
    i = 0
    score = 0
    for inn in range(n):
        out = 0
        f1, f2, f3 = False, False, False
        while out < 3:
            hit = P[i][inn]
            if hit == '1':
                score+= f3
                f1, f2, f3 = True, f1, f2
            elif hit == '2':
                score+= f2 + f3
                f1, f2, f3 = False, True, f1
            elif hit == '3':
                score+= f1 + f2 + f3
                f1, f2, f3 = False, False, True
            elif hit == '4':
                score+= f1 + f2 + f3 + 1
                f1 = f2 = f3 = False
            else: out+= 1
            i = (i+1) % 9
    return score

n = int(input())
res = [['']*n for i in range(9)]
for i in range(n):
    row = input().replace(' ','')
    for j in range(9): res[j][i] = row[j]
res = [''.join(row) for row in res]
ans = 0
for P in permutations(res[1:], 8):
    Q = P[:3] + (res[0],) + P[3:]
    ans = max(ans, run(Q))
print(ans)