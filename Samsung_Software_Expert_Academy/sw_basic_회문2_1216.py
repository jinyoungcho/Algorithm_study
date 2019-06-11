def check(li,len_hui_men):
    if len_hui_men % 2 == 0:
        if li[:len_hui_men//2] == li[::-1][:len_hui_men//2]:
            return True
    else:
        if li[(len_hui_men//2)-1] != li[len_hui_men//2] and li[len_hui_men // 2] != li[(len_hui_men//2)+1]:
            if li[:len_hui_men//2] == li[::-1][:len_hui_men//2]:
                return True
        else:
            if li[(len_hui_men//2)-1] == li[len_hui_men//2] == li[(len_hui_men//2)+1]:
                if li[:len_hui_men // 2] == li[::-1][:len_hui_men // 2]:
                    return True
    return False

for t in range(1,11):
    input()

    MAXI = 1

    MAP = []
    for _ in range(100):
        MAP.append(list(input()))

    # MAP = [['a','b','b','a']]

    for k in range(2,101):
        for i in range(100):
            for j in range(100-k+1):
                if check(MAP[i][j:j+k],k):
                    MAXI = max(MAXI,k)

    MAP = list(zip(*MAP))

    for k in range(2,101):
        for i in range(100):
            for j in range(100-k+1):
                if check(MAP[i][j:j+k],k):
                    MAXI = max(MAXI,k)
    print('#',end='')
    print(t,MAXI)