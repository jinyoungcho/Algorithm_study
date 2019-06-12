



def solution(n):

    DP = [0] * (n+1+3)

    DP[0] = 0
    DP[1] = 1
    DP[2] = 2


    for _ in range(3,n+1):
        DP[_] = DP[_-1] + DP[_-2]

    # print(DP)
    answer = DP[n]



    return answer % 10007

print(solution(int(input())))
