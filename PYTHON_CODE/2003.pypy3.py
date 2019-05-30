N,M = list(map(int,input().split()))

li = list(map(int,input().split()))

cnt = 0

i=0
while(True):

    if i == N:
        break

    temp = li[i]


    if temp == M:
        cnt +=1
        i += 1
        continue

    j=i+1

    while(True):
        # print(i,j)
        if j == N:
            i+=1
            break

        temp += li[j]

        if temp == M:
            cnt += 1
            i+=1
            break
        elif temp > M:
            i+=1
            break
        else:
            j+=1

print(cnt)