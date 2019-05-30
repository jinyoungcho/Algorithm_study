M = int(input())

li = [1] + [0]*2

for _ in range(M):

    s, g = list(map(int,input().split()))

    s -= 1
    g -= 1

    li[s],li[g] = li[g],li[s]

print(li.index(1)+1)

