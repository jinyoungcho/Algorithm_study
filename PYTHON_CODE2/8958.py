# EASY

T = int(input())

for _ in range(T):

    string = ['X']+ list(input())

    temp = 0
    score = 0

    tem=1
    for str_ in string:
        if str_ == 'X':
            temp = 1
        else:
            score += temp
            temp += 1

    print(score)
