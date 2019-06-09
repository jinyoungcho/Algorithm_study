
for t in range(1,11):
    input()
    ans = 0

    goal_str = input()

    paper = input()

    # print(paper.find(goal_str))

    st=0
    ed=len(paper)
    cnt=0
    while(True):
        # print(paper[st:ed])
        idx = paper[st:ed].find(goal_str)
        # print(idx)
        if idx == -1:
            break

        cnt += 1

        st = st+idx+len(goal_str)
        # print(st)
    # print(cnt)


    ans = cnt

    print('#',end='')
    print(t,ans)