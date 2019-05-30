T = int(input())




def dfs(month,price_idx,total):
    global MINI

    if month >= 12:
        MINI = min(total,MINI)
        # print(MINI)
    else:
        # print(month,price_idx,total)
        # 1일치
        if plan_list[month] != 0:
            price_idx = 0
            cost = plan_list[month] * price_list[price_idx]
            dfs(month+1,price_idx,total+cost)

            # 1달치
            price_idx = 1
            cost = price_list[price_idx]
            dfs(month+1,price_idx,total+cost)
        else:
            dfs(month + 1, 0, total)

        if sum(plan_list[month:month+3]) != 0:
            price_idx = 2
            cost = price_list[price_idx]
            dfs(month+3,price_idx,total+cost)



def simulate():
    global price_list

     # 1년짜리 이용권
    dfs(0,0,0) # 1월, 1일권, 0원부터 시작~!

    return MINI

for t in range(1,T+1):
    ans=0

    price_list = list(map(int,input().split()))

    plan_list = list(map(int,input().split()))

    MINI = price_list[-1]

    ans = simulate()



    print("#",end="")
    print(t,ans)