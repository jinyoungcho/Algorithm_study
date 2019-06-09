from collections import deque

def bfs():
    st = 0

    visited = set()
    visited.add(st)

    q = deque()
    q.append(st)
    # print(dict)
    while(q):
        st = q.popleft()

        if st == 99:
            return True

        for ed in dict[st]:

            if ed in visited:
                continue

            q.append(ed)
            visited.add(ed)

    # print(visited)

    return False

for t in range(1,11):

    test_case, num_arc = list(map(int,input().split()))

    ip_arc_li = list(map(int,input().split()))

    dict={}
    for _ in range(100):
        dict[_] = []

    for idx in range(num_arc):
        st = ip_arc_li[idx*2]
        ed = ip_arc_li[(idx*2) + 1]
        dict[st].append(ed)


    ans = 1 if bfs() else 0


    print("#",end='')
    print(t,ans)