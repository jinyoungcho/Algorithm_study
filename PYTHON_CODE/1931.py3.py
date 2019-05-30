full2 = []
full = []
temp = []

itr = int(input())

cf2 = 0
for i in range(0, itr):
    full2.append([*map(int, input().split()[::-1])])

full2.sort()


full.append(full2[0])


cf2 = 1

topf = 0

while (True):
    if cf2 == itr: break
    if int(full[topf][0]) <= int(full2[cf2][1]):
        full.append(full2[cf2])
        topf += 1
    cf2 += 1

print(len(full))