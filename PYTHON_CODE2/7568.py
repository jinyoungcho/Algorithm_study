N = int(input())

li = []

for _ in range(N):
    weight, height = list(map(int,input().split()))

    li.append((weight,height))

# print(li)

for idx, (n_weight, n_height) in enumerate(li):
    cnt = 1

    for idx2, (n_weight2, n_height2) in enumerate(li):

        if idx == idx2:
            continue

        if n_weight2 > n_weight and n_height2 > n_height:
            cnt += 1

    print(cnt, end=' ')