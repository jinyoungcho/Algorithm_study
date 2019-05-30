T = int(input())
ans = 0
operators = []
numbers = []
MAXI = -100000000
MINI = 100000000








def dfs(temp,op_idx,index):

    global MAXI
    global MINI

    if index == N:

        MAXI = max(temp,MAXI)
        MINI = min(temp,MINI)


    else:
        if operators[op_idx] > 0:

            operators[op_idx]-=1 #연산자 사용

            if op_idx == 0: #'+'
                next_temp = temp + numbers[index]
            elif op_idx == 1: #'-'
                next_temp = temp - numbers[index]
            elif op_idx == 2: #'*'
                next_temp = temp * numbers[index]
            elif op_idx == 3: #'/'
                next_temp = int(temp / numbers[index])

            for op in range(4):
                dfs(next_temp, op, index+1)

            operators[op_idx]+=1

def simulate():

    for op in range(4): # 넷중 아무데서 출발
        dfs(numbers[0],op,1)


for t in range(1,T+1):

    ans = 0
    MAXI = -100000000
    MINI = 100000000

    N = int(input())

    operators = list(map(int,input().split()))
    numbers = list(map(int,input().split()))

    simulate()


    ans = MAXI - MINI
    print("#",end="")
    print(t,ans)