
from collections import Counter
from functools import cmp_to_key



def op_r(max_r):
    final_li = []
    max_len = 0
    for r in range(max_r):
        temp_dic = Counter(MAP[r])
        temp_li = [i for i in zip(temp_dic.keys(),temp_dic.values()) if i[0] != 0]
        temp_li = sorted(sorted(temp_li,key= lambda x:x[0]), key= lambda x:x[1])


        sample_li = []
        for li in temp_li:
            for j in range(2):
                sample_li.append(li[j])

        max_len = max(max_len,len(sample_li))
        final_li.append(sample_li)

        # print(temp_li)

    for idx in range(len(final_li)):
        if len(final_li[idx]) < max_len:
            final_li[idx] += [0] * (max_len - len(final_li[idx]))

    return final_li


def op_c(max_c):
    global MAP
    MAP = list(zip(*MAP))

    final_li = []
    max_len = 0
    for r in range(max_c):
        temp_dic = Counter(MAP[r])
        temp_li = [i for i in zip(temp_dic.keys(), temp_dic.values()) if i[0] != 0]
        temp_li = sorted(sorted(temp_li, key=lambda x: x[0]), key=lambda x: x[1])

        sample_li = []
        for li in temp_li:
            for j in range(2):
                sample_li.append(li[j])

        max_len = max(max_len, len(sample_li))
        final_li.append(sample_li)

        # print(temp_li)

    for idx in range(len(final_li)):
        if len(final_li[idx]) < max_len:
            final_li[idx] += [0] * (max_len - len(final_li[idx]))

    return list(zip(*final_li))

def simulate():

    global MAP

    #R연산
    for k in range(101):

        len_r = len(MAP)
        len_c = len(MAP[0])


        try:
            if MAP[R-1][C-1] == K:
                return k
            if k > 100:
                return -1
        except:
            pass

        if len_r >= len_c:
            MAP = op_r(len_r)

        # C연산
        else:
            MAP = op_c(len_c)


    return -1


R,C,K = list(map(int,input().split()))
MAP = []
for _ in range(3):
    MAP.append(list(map(int,input().split())))

ans = simulate()

print(ans)