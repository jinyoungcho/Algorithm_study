A,B,C,X,Y = list(map(int,input().split()))

# A 양념
# B 후라이드
# C 반반

# 양념 X
# 후라이드 Y

total_cost = 0



if A+B < C*2:
    total_cost += A * X
    total_cost += B * Y

elif B > C*2 or A > C*2:

    if A > C*2 and B > C*2: #둘다 반반 사는게 더 쌈
        if X > Y:
            total_cost += (X-Y) * C * 2
            total_cost += Y * C * 2
        elif Y > X:
            total_cost += (Y-X) * C * 2
            total_cost += X * C * 2
        else:
            total_cost += (X+Y) * C*2

    elif A > C*2 and B < C*2: #양념만 반반사는게 더 싸
        if X >= Y: #근데 양념이 더 많아
            total_cost += X * C*2

        elif X < Y:
            total_cost += X * C * 2
            total_cost += (Y-X) * B

    elif B > C*2 and A < C*2: #후라이드만 반반사는게 더 싸

        if Y >= X:  # 근데 후라이드가 더 많아
            total_cost += Y * C * 2

        elif Y < X:
            total_cost += Y * C * 2
            total_cost += (X - Y) * A


else:
    if X > Y:
        total_cost += (Y * C*2)
        total_cost += ((X-Y) * A)
    elif X < Y:
        total_cost += (X * C*2)
        total_cost += ((Y-X) * B)
    else:
        total_cost += (X * C*2)

print(total_cost)