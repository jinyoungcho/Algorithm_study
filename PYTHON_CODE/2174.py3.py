C,R = list(map(int,input().split()))
N,M = list(map(int,input().split()))

robot=[]

di=[-1,0,1,0]
dj=[0,1,0,-1]
# 남동북서

MAP = [[-1] * C for _ in range(R)]

rdx = 0
for _ in range(N):

    j,i,k_str = list(input().split())

    k = 0
    if k_str == 'N':
        k=2
    elif k_str == 'W':
        k=3
    elif k_str == 'E':
        k=1
    elif k_str == 'S':
        k=0

    robot.append([int(i)-1,int(j)-1,k])
    MAP[int(i)-1][int(j)-1] = rdx
    rdx+=1

cmd_li = []

for _ in range(M):
    idx, cmd, freq = list(input().split())
    cmd_li.append((int(idx)-1,cmd,int(freq)))


# for _ in range(R):
#     print(MAP[_])


def simulate():

    # print(idf)
    # for _ in range(R):
    #     print(MAP[_])

    for idf in cmd_li:

        idx,cmd,freq = idf

        now_robot = robot[idx]

        if cmd == 'F':
            sample_i,sample_j = now_robot[0], now_robot[1]
            for f in range(freq):
                now_robot[0] += di[now_robot[2]]
                now_robot[1] += dj[now_robot[2]]

                # print(now_robot[0],now_robot[1])
                if not(0<= now_robot[0] < R and 0 <= now_robot[1] < C):
                    print("Robot", idx+1, "crashes into the wall")
                    return


                if MAP[ now_robot[0] ][ now_robot[1] ] != -1:
                    print("Robot", idx+1, "crashes into robot", MAP[ now_robot[0] ][ now_robot[1] ] + 1)
                    return


            MAP[sample_i][sample_j] = -1
            MAP[now_robot[0]][now_robot[1]] = idx

        elif cmd == 'L':

            now_robot[2] += freq
            now_robot[2] %= 4

        elif cmd == 'R':
            # print('before',now_robot[2])
            # now_robot[2] = abs(now_robot[2]-freq) % 4
            # print(freq % 4)
            now_robot[2] -= freq % 4
            # print(now_robot[2])
            if now_robot[2] <0:

                now_robot[2] = 4-abs(now_robot[2])

            # print('after',now_robot[2])
        # print("~~")
        # print(idf)
        # for _ in range(R):
        #     print(MAP[_])

    print("OK")
simulate()