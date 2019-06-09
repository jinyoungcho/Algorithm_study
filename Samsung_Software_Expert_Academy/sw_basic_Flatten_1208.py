import heapq

for t in range(1,11):
    ans = 0

    num_dump = int(input())
    li = list(map(int, input().split()))
    heapq.heapify(li)


    while num_dump:
        heapq._heapify_max(li)
        maxi = heapq._heappop_max(li)
        maxi -= 1
        maxi = heapq.heappush(li,maxi)
        heapq.heapify(li)
        mini = heapq.heappop(li)
        mini += 1
        heapq.heappush(li,mini)
        num_dump-=1

    ans = max(li)-min(li)


    print('#',end='')
    print(t,ans)