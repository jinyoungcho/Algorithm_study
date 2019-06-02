# https://www.acmicpc.net/problem/2980

# 시뮬레이션

N,L = list(map(int,input().split()))

loc = [None]*(L+1)

t = 0

for _ in range(N):
    a,b,c = list(map(int,input().split()))
    loc[a] = [b,c]

def check(now,time):

    signal = loc[now]
    time = time

    state = time % sum(signal)
    # print("-> state", time,sum(signal),state)
    if state < signal[0]:
        return False
    else:
        return True

now = 0
t = 0
while(True):
    # print(now,t)
    if now == L:
        break
    #아무것도 없어유
    if loc[now] is None:
        now += 1
    elif loc[now] is not None:
        if check(now,t):#현재 시간에 건널 수 있다면
            # print("건너")
            now += 1
    t += 1

print(t)