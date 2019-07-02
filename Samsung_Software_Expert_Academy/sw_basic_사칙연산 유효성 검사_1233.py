for tc in range(10):
    case = int(input())
    datas = []
    for number in range(case):
        datas.append(list(input().split()))

    result = 1
    for i in range(case):
        if len(datas[i]) == 2:
            if datas[i][1] in ['+', '-', '*', '/']:
                # print(datas[i])
                result = 0
                break

    print('#{} {}'.format(tc + 1, result))