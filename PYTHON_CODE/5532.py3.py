L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# ac
# bd
cnt = 0
for _ in range(L):

    done = True

    if A > 0:
        done = False
        A -= C

    if B > 0:
        done = False
        B -= D

    if done:
        cnt += 1

print(cnt)