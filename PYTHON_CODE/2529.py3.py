n = int(input())

a = list(map(str,input().split()))

n_li = [0,1,2,3,4,5,6,7,8,9]


from itertools import permutations, product

mini = 9999999999999
maxi = 0

mini_str = ''
maxi_str = ''

for i in permutations(n_li,n+1):
    li = i
    c = False
    for jdx,j in enumerate(a):
        
        if j == "<" and li[jdx] < li[jdx+1]:
            c = True
        
        elif j == ">" and li[jdx] > li[jdx+1]:
            c = True
        else:
            c = False
            break
    
    if c == True:
        temp = int(''.join(list(map(str,li))))

        if temp < mini:
            mini = temp
            mini_str = ''.join(list(map(str,li)))
        
        if temp > maxi:
            maxi = temp
            maxi_str = ''.join(list(map(str,li)))
#         mini = min(temp,mini)
#         maxi = max(temp,maxi)
        
        
        
print(maxi_str)
print(mini_str)