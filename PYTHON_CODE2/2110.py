# https://www.acmicpc.net/problem/2110

# 이분탐색

Num_House,Num_Gadget = list(map(int,input().split()))

house = []
for _ in range(Num_House):
    temp = int(input())
    house.append(temp)
house.sort()


def binary_search():
    # 간격!
    st = 1
    ed = house[-1] - house[0]
    ans = 0

    while st <= ed:

        md = (st+ed)//2 # 거리 기준
        house_installed = house[0]
        num_gadget_installed = 1

        for i in range(1, Num_House):
            dist = house[i] - house_installed  # 두 집 사이의 거리

            if md <= dist:  # 만약 두 집 사이의 거리가 기준보다 크다면
                num_gadget_installed += 1
                house_installed = house[i]  # 설치되었습니다

        if num_gadget_installed >= Num_Gadget:  # 설치되어야 할 공유기보다 많이 설치됐다면
            # print('over')
            # print(st,ed,md)
            st = md + 1
            ans = md

        elif num_gadget_installed < Num_Gadget:  # 설치되어야 할 공유기보다 적게 설치됐다면
            # print('under')
            # print(st, ed, md)
            ed = md - 1
            # st = ed

    # print(num_gadget_installed, Num_Gadget)

    return ans

print(binary_search())
