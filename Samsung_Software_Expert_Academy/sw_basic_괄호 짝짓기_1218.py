


from collections import deque

def simulate(li_str):

    stack1 = 0  # '()'
    stack2 = 0  # '[]'
    stack3 = 0  # '{}'
    stack4 = 0  # '<>'

    for stri in li_str:

        # print(stack1,stack2,stack3,stack4)

        if stri == '(' or stri == ')':
            stack1 = stack1 + (1 if stri == '(' else -1)
            if stack1 == -1:
                return False

        elif stri == '[' or stri == ']':
            stack2 = stack2 + (1 if stri == '[' else -1)
            if stack2 == -1:
                return False


        elif stri == '{' or stri == '}':
            stack3 = stack3 + (1 if stri == '{' else -1)
            if stack3 == -1:
                return False
        else:
            stack4 = stack4 + (1 if stri == '<' else -1)
            if stack4 == -1:
                return False

    if stack1 != 0 or stack2 != 0 or stack3 != 0 or stack4 != 0:
        return False
    else:
        return True

for testcase in range(10):

    N = int(input())
    ans = 0

    li_str = list(input())

    # '()', '[]', '{}', '<>'

    ans = 1 if simulate(li_str) else 0

    print("#",end='')
    print(testcase+1,ans)