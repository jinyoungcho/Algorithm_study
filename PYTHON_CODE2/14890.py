N,L = list(map(int, input().split()))

MAP = []

for _ in range(N):
    MAP.append(list(map(int, input().split())))



def simulate(li):

    li = li
    check = [False] * N

    st = li[0]
    for i in range(1,N):

        if st == li[i]: #같다면 그냥 넘어가유
            st = li[i]
            continue

        elif st > li[i]: #앞선 쪽이 더 낮다면? #앞으로 내리막길 만들어줘

            if st - li[i] > 1:
                return False

            for j in range(i,i+L):
                if j >= N:
                    return False
                if check[j] == True:
                    return False
                if li[j] != li[i]:
                    return False
                check[j] = True

            st = li[i]
            continue

        elif st < li[i]: #앞쪽이 높다면 현재위치 i부터 뒤로 오르막길 만들어줘

            if li[i] - st > 1:
                return False

            for j in range(i-1,i-L-1,-1):
                if j < 0:
                    return False
                if check[j] == True:
                    return False
                if li[j] != st:
                    return False
                check[j] = True

            st = li[i]
            continue



    return True

cnt = 0

for _ in range(N):
    if simulate(MAP[_]):
        # print(_)
        # print(MAP[_])
        cnt += 1


MAP = list(zip(*MAP))

for _ in range(N):
    if simulate(MAP[_]):
        # print(_)
        # print(MAP[_])
        cnt += 1

print(cnt)