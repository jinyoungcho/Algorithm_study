from copy import deepcopy
from itertools import permutations

from collections import deque

T = int(input())


class person:
    def __init__(self, idx, i, j, state):
        self.idx = idx
        self.i = i
        self.j = j
        self.distance = 0
        self.state = state
        self.wating = 0

    def __repr__(self):
        return "index:" + str(self.idx) + ",  상태:" + str(self.state)


def get_Time(p_li, s_info):
    si = s_info[0]
    sj = s_info[1]
    s_waiting = s_info[2]

    p_queue = deque()
    stair_queue = deque()
    end_queue = deque()

    for p in p_li:
        p.distance = abs(p.i - si) + abs(p.j - sj)
        p.wating = s_waiting
        p_queue.append(p)

    t = 0
    while (len(end_queue) != len(p_li)):

        # print(t, p_queue, stair_queue, end_queue)

        p_len = len(p_queue)
        stair_len = len(stair_queue)

        for _ in range(stair_len):
            p = stair_queue.popleft()
            p.wating -= 1

            if p.wating == 0:
                end_queue.append(p)
            else:
                stair_queue.append(p)

        # person에서 뽑아와유
        for _ in range(p_len):
            p = p_queue.popleft()

            if p.state == 0:

                p.distance -= 1
                if p.distance == 0:
                    p.state = 1
                    if len(stair_queue) < 3:
                        stair_queue.append(p)
                    else:
                        p_queue.append(p)

                else:
                    p_queue.append(p)

            elif p.state == 1:

                if len(stair_queue) < 3:
                    stair_queue.append(p)
                else:
                    p_queue.append(p)

        t += 1

    return t


def simulate(num_p):
    a_list = []
    for i in range(1 << num_p):
        f_li = []
        s_li = []
        for j in range(num_p):

            # 계단 1
            if i & (1 << j):
                f_li.append(deepcopy(p_list[j]))
            # 계단 2
            else:
                s_li.append(deepcopy(p_list[j]))

        f_time = get_Time(f_li, stair_list[0])
        s_time = get_Time(s_li, stair_list[1])
        temp = max(f_time, s_time)

        a_list.append(temp)

    # print(a_list)

    return min(a_list)


for t in range(1, T + 1):
    ans = 0
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    p_list = []
    stair_list = []

    idx = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1:
                p_list.append(person(idx, i, j, 0))
                idx += 1
            elif MAP[i][j] > 1:
                stair_list.append((i, j, MAP[i][j]))

    ans = simulate(idx)

    print("#", end="")
    print(t, ans + 1)