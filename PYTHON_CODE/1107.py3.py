now = 100

N = int(input())

M = int(input())

if M > 0:
    a = list(map(int,input().split(" ")))
else:
    a = []
    
    
def possible(c):
    li_str = list(str(c))
    
    for x in li_str:
#         print(x)
        if int(x) in a:
            return False
    
    return True

ans = abs(N - 100)
for c in range(0,1000001):

    check = possible(c)
#     print(check)
    
    if check == True:
        l = len(list(str(c)))
        press = abs(N - c)
        if ans > l + press:
            ans = l + press
            
print(ans)