# (()[[]])([])
ip = list(input())
stack = []

pair = {
    ')' : '(',
    ']' : '['
}

def check(ip):
    for char in ip:
        if char in ['[', '(']:
            stack.append(char)
        elif char in [')',']']:
            if not stack:
                return False
            else:
                value = stack.pop(-1)
                if value != pair[char]:
                    return False
    if stack:
        return False
    else:
        return True

if not check(ip):
    print(0)
    exit(0)

for idx,char in enumerate(ip):
    # print(stack)
    if char in ['(','[']:
        stack.append(char)

    else:

        #닫는괄호 처리부분!!! 잘생각하자

        temp = 0
        # print(idx)
        # print(stack)
        value = stack.pop(-1)
        flag = False
        while(value != '[' and value != '('):
                #너는 닫는괄호가 아니야
            flag = True
            temp += value
            value = stack.pop(-1)

        temp = 1 if not flag else temp

        #드디어 닫는괄호가 나왔어유 or 넌 이미 닫는괄호야
        temp *= 2 if value =='(' else 3

        stack.append(temp)

print(sum(stack))

#1. (()[[]])([])
    #(
#2. (2[[]])([])
    #(2
#3. (2[3])([])
    #(2[3
#4. (2 9 )([])
    #(29
#5. 22([])
    # 22
#6. 22 (3)
    # 22 (
#7. 22 6
    # 22 6

# sum(stack)