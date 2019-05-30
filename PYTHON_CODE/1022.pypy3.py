r1, c1, r2, c2 = list(map(int,input().split()))

# 가장 왼쪽 위
# 가장 오른쪽 아래


MAP = {}

from collections import deque

q = deque()

q.append((0,0,1,1)) #y,x,num,direction,cnt

MAP[(0,0)] = 1

#반시계방향
#우 상 좌 하

di = [0,-1,0,1]
dj = [1,0,-1,0]


MAXI = max(abs(r1),abs(r2),abs(c1),abs(c2))

MAXI_len = 0
while(q):

    i,j,num,cnt = q.popleft()
    # print(i,j,num,cnt)
    # print(cnt)
    a = 0

    if cnt == 1+(2*MAXI):
        # print(cnt, 1+(2*MAXI))
        break

    #우 #한칸만

    ni = i+di[0]
    nj = j+dj[0]
    n_num = num + 1

    if r1 <= ni <= r2 and c1 <= nj <= c2:
        MAP[(ni, nj)] = n_num
        MAXI_len = max(MAXI_len, len(str(n_num)))
    while(a != cnt):
        #상 #
        ni += di[1]
        nj += dj[1]
        n_num += 1

        if r1 <= ni <= r2 and c1 <= nj <= c2:
            MAP[(ni, nj)] = n_num
            MAXI_len = max(MAXI_len, len(str(n_num)))
        a += 1

    a = 0

    while(a!= cnt+1):
        ni += di[2]
        nj += dj[2]
        n_num += 1
        if r1 <= ni <= r2 and c1 <= nj <= c2:
            MAP[(ni,nj)] = n_num
            MAXI_len = max(MAXI_len, len(str(n_num)))
        a += 1

    a = 0
    while(a!= cnt+1):
        ni += di[3]
        nj += dj[3]
        n_num += 1
        if r1 <= ni <= r2 and c1 <= nj <= c2:
            MAP[(ni,nj)] = n_num
            MAXI_len = max(MAXI_len, len(str(n_num)))
        a += 1

    a = 0
    while(a!= cnt+1):
        ni += di[0]
        nj += dj[0]
        n_num += 1
        if r1 <= ni <= r2 and c1 <= nj <= c2:
            MAP[(ni,nj)] = n_num

            MAXI_len = max(MAXI_len,len(str(n_num)))

        a += 1

    q.append((ni,nj,n_num,cnt+2))


# print(MAP)

# print(MAXI_len)

for i in range(r1,r2+1):
    for j in range(c1,c2+1):

        if MAXI_len > len(str(MAP[(i,j)])):
            for _ in range(MAXI_len - len(str(MAP[(i,j)]))):
                print(" ", end="")

        if j == c2:
            print(MAP[(i,j)],end="")
        else:
            print(MAP[(i, j)], end=" ")

    if i != r2:
        print("")
