class BUS:
    def __init__(self,t,p,num):
        self.T = t
        self.P = p
        self.loc = -1
        self.num = num

    def __repr__(self):
        return "T:"+str(self.T)+", P:"+str(self.P)+", loc:"+str(self.loc)+", num:"+str(self.num)


N, M = list(map(int, input().split()))

from collections import deque

bus_queue = deque()

arrived_queue = deque()

waiting_queue = deque()

for num in range(1, M+1):

    t, p = list(map(int, input().split()))

    bus_queue.append(BUS(t, p, num))

t=1
find = False
ans = 0
while(True):

    # if t == 30:
    #     break

    for _ in range(len(waiting_queue)):

        waiting_bus = waiting_queue.popleft()

        if waiting_bus.num == M:
            find = True
            ans = waiting_bus.loc
            break

        waiting_bus.P -= 1

        if waiting_bus.P <= 0:

            #can out
            can_out = True
            for _ in range(len(waiting_queue)):
                if waiting_bus.num != waiting_queue[_].num:
                    if waiting_bus.loc > waiting_queue[_].loc:
                        can_out = False
                        break

            if can_out == False:
                waiting_queue.append(waiting_bus)


        else:
            waiting_queue.append(waiting_bus)

    if find == True:
        break

    for _ in range(len(arrived_queue)):

        arrived_bus = arrived_queue.popleft()

        if len(waiting_queue) == 0:
            arrived_bus.loc = 1
            waiting_queue.append(arrived_bus)

        elif len(waiting_queue) < N:
            last_waiting_bus_loc = waiting_queue[-1].loc

            if last_waiting_bus_loc == N:
                arrived_queue.append(arrived_bus)
            else:
                arrived_bus.loc = last_waiting_bus_loc+1
                waiting_queue.append(arrived_bus)

        else:
            arrived_queue.append(arrived_bus)


    while(bus_queue):

        bus = bus_queue.popleft()

        if bus.T == t:

            if len(waiting_queue) == 0:

                bus.loc = 1
                waiting_queue.append(bus)

            elif len(waiting_queue) < N:
                last_waiting_bus_loc = waiting_queue[-1].loc

                if last_waiting_bus_loc == N:
                    arrived_queue.append(bus)
                else:
                    bus.loc = last_waiting_bus_loc + 1
                    waiting_queue.append(bus)


            else:
                arrived_queue.append(bus)


        else:
            bus_queue.appendleft(bus)
            break


    # print(t, arrived_queue, waiting_queue)

    t+=1

print(ans)