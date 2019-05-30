from collections import deque


# 프로그램영역 // 입력영역

finish = False
while(True):

    mode = 'program'

    input_program=[]

    if mode == 'program':
        while(True):

            ip = input()

            if ip == "END":
                mode = 'input'
                break
            elif ip == 'QUIT':
                finish = True
                break

            else:
                input_program.append(ip)



    input_num = []

    if finish:
        break

    if mode == 'input':

        N = int(input())

        for _ in range(N):
            input_num.append(int(input()))

        input()
        mode = 'program'

    # print(input_program, input_num)


    for ip_num in input_num:

        error = False

        stack = deque()
        stack.append(ip_num)
        ans = 0
        for cmd in input_program:
            # print(stack)
            if cmd[:3] == 'NUM':
                number = int(cmd[4:])
                stack.append(number)

            elif cmd == 'POP':
                try:
                    stack.pop()
                except:
                    ans = "ERROR"
                    break

            elif cmd == 'INV':
                try:

                    number = -stack.pop()
                    stack.append(number)
                except:
                    ans = "ERROR"
                    break

            elif cmd == 'DUP':
                try:
                    dup = stack.pop()
                    stack.append(dup)
                    stack.append(dup)
                except:
                    ans = "ERROR"
                    break

            elif cmd == 'SWP':
                try:
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(first)
                    stack.append(second)
                except:
                    ans = "ERROR"
                    break
            elif cmd == 'ADD':
                try:
                    first = stack.pop()
                    second = stack.pop()
                    ans = first+second

                    if ans > pow(10,9):
                        ans = "ERROR"
                        break

                    stack.append(ans)
                except:
                    ans = "ERROR"
                    break

            elif cmd == 'SUB':
                try:
                    # print(stack)
                    first = stack.pop()
                    second = stack.pop()
                    ans = second - first

                    if abs(ans) > pow(10,9):
                        ans = "ERROR"
                        break

                    stack.append(ans)
                except:
                    ans = "ERROR"
                    break

            elif cmd == 'MUL':
                try:
                    first = stack.pop()
                    second = stack.pop()
                    ans = first * second

                    if ans > pow(10,9):
                        ans = "ERROR"
                        break

                    stack.append(ans)

                except:
                    ans = "ERROR"
                    break

            elif cmd == 'DIV' or 'MOD':

                try:

                    first = stack.pop()
                    second = stack.pop()
                    # print(first, second)
                    f_p = True
                    s_p = True

                    if first == 0:
                        ans = 'ERROR'
                        break

                    f_p = False if first < 0 else True
                    s_p = False if second < 0 else True

                    div = abs(second) // abs(first)
                    mod = abs(second) % abs(first)

                    if cmd == 'DIV':
                        if (f_p == True and s_p == False) or (f_p == False and s_p == True):
                            stack.append(-div)
                        else:
                            stack.append(div)

                    elif cmd == 'MOD':
                        if s_p == True:
                            stack.append(mod)
                        else:
                            mod = -mod
                            stack.append(mod)
                except:
                    ans = "ERROR"
                    break

        if ans == 'ERROR':
            print(ans)
        else:
            if len(stack) != 1:
                print("ERROR")
            else:
                print(stack.pop())



    print("")