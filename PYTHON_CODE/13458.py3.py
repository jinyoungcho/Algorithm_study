N = int(input())
Arr = list(map(int,input().split()))
# Arr = [1000000] * 1000000
B,C = list(map(int,input().split()))

Brr = []

for A in Arr:
    num_director = 0

    A -= B
    num_director += 1
    if A <= 0:
        Brr.append(num_director)
        continue

    if A > 0:
        num_director += A // C
        A = A % C

    if A > 0:
        num_director += 1

    Brr.append(num_director)
    # print(num_director)
# print(Brr)
print(int(sum(Brr)))