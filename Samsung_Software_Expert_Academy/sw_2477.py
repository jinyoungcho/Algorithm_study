from collections import deque
from functools import cmp_to_key

class Customer:
    def __init__(self,idx,new_t):
        self.idx = idx
        self.new_t = new_t
        self.r1_num = -1
        self.r1_wait_time = -1
        self.r2_num = -1
        self.r2_wait_time = -1
        self.r1_finish_time = -1
    def __repr__(self):
        return "c"+str(self.idx) +'~'+ str(self.r1_num+1) +'~'+ str(self.r2_num+1)

def cmp(c, cc):
    if c.r1_finish_time != cc.r1_finish_time:
        return c.r1_finish_time < cc.r1_finish_time
    else:
        return c.r1_num < cc.r1_num

def simulate():

    global ans
    finished = 0
    wait_for_1 = deque()
    wait_for_2 = deque()

    on1 = [False] * N
    on2 = [False] * M

    t = customer[0]
    while( finished != K ):

        # 1.정비소 처리
        for idx in range(M):
            if on2[idx] == False: continue
            else:
                c = on2[idx]

                c.r2_wait_time -= 1
                if c.r2_wait_time != 0:
                    on2[idx] = c
                else:

                    if c.r1_num == A and c.r2_num == B:
                        ans += c.idx

                    finished += 1
                    on2[idx] = False

        # 2.정비소 대기 list
        # wait_for_2 = deque(sorted(wait_for_2,key=cmp_to_key(cmp)))
        for _ in range(len(wait_for_2)):
            c = wait_for_2.popleft()
            find = False

            for idx in range(M):
                if on2[idx] != False: continue
                else:
                    find = True
                    c.r2_num = idx
                    c.r2_wait_time = repair_t[idx]
                    on2[idx] = c
                    break

            if find == False:
                wait_for_2.appendleft(c)
                break

        # 3.접수창구 처리

        for idx in range(N):
            if on1[idx] == False: continue
            else:
                c = on1[idx]
                c.r1_wait_time -= 1
                if c.r1_wait_time != 0:
                    on1[idx] = c
                else: #접수창구 끝났어
                    on1[idx] = False
                    find = False
                    c.r1_finish_time = t
                    for jdx in range(M):
                        if on2[jdx] != False: continue

                        else:
                            find = True
                            c.r2_num = jdx
                            c.r2_wait_time = repair_t[jdx]
                            on2[jdx] = c
                            break

                    if find == False:
                        wait_for_2.append(c)

        # 4.접수창구 대기 list
        # wait_for_1 = deque( sorted(wait_for_1, key = lambda x: x.idx) )
        for _ in range(len(wait_for_1)):
            c = wait_for_1.popleft()
            find = False

            for idx in range(N):
                if on1[idx] != False:
                    continue
                else:
                    find = True
                    c.r1_num = idx
                    c.r1_wait_time = register_t[idx]
                    on1[idx] = c
                    break

            if find == False:
                wait_for_1.appendleft(c)
                break

        # 5. new_cus
        nq = deque()
        if t in cus_dic:
            for a in cus_dic[t]:
                nq.append(a)
            # print(nq)
        for _ in range(len(nq)):
            c = nq.popleft()
            find = False

            for idx in range(N):
                if on1[idx] != False:
                    continue
                else:
                    find = True
                    c.r1_num = idx
                    c.r1_wait_time = register_t[idx]
                    on1[idx] = c
                    break

            if find == False:
                wait_for_1.append(c)


        # print("---t",t,"----")
        # print("wait1", wait_for_1)
        # print("on1", on1)
        # print("wait2",wait_for_2)
        # print("on2",on2)
        # print("finish",finished_customer)
        # print("")

        t+=1




T = int(input())
for tt in range(1,T+1):

    N,M,K,A,B = list(map(int,input().split()))

    A-=1
    B-=1

    ans = 0
    #N = 접수창구 개수
    #M = 정비창구 개수
    #K = 고객 수

    register_t = list(map(int, input().split()))
    repair_t = list(map(int, input().split()))
    customer = list(map(int, input().split()))
    cus_dic = {}
    # print(customer)
    for i,t in enumerate(customer):
        if t in cus_dic:
            cus_dic[t].append(Customer(i+1, t))
        else:
            cus_dic[t] = [Customer(i+1, t)]

    simulate()
    # ans = check(finished_customer)

    if ans == 0:
        ans = -1
    print("#",end="")
    print(tt,ans)