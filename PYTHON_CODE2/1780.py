#분할정복 문제

#https://www.acmicpc.net/problem/1780

# 재귀함수를 이용해서 조건에 맞지 않는다면 분할해서 정복하기!

def d_q(i,j,size,MAP,dict):

    if size == 1:
        dict[MAP[i][j]] += 1
        return

    same = True
    first = MAP[i][j]

    for i_2 in range(i,i+size):
        if not same:
            break

        for j_2 in range(j,j+size):
            if first != MAP[i_2][j_2]:
                same = False
                break

    if same:
        dict[first] += 1
        return

    new_size = size // 3

    for i_3 in range(3):
        for j_3 in range(3):
            d_q(i+(i_3 * new_size), j+(j_3 * new_size), new_size,MAP,dict)


def main():
    N = int(input())
    MAP = []
    for _ in range(N):
        MAP.append(list(map(int, input().split())))

    dict = {}

    dict[-1] = 0
    dict[0] = 0
    dict[1] = 0

    d_q(0,0,N,MAP,dict)

    # print(dict)

    for key in [-1,0,1]:
        print(dict[key])
main()