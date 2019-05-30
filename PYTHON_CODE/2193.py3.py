n = int(input())


d = [0 for i in range(91)]
d[0] = 0
d[1] = 1
d[2] = 1
for i in range(3,len(d)):
    for j in range(1, i-1):
        d[i] += d[j]
    d[i] += 1
    
print(d[n])