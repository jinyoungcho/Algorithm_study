t = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

def make_li(li):
    new_li = []
    for i in range(len(li)):
        new_li.append(li[i])
        s = li[i]
        for j in range(i+1,len(li)):
            s += li[j]
            new_li.append(s)
    
    return new_li

a = sorted(make_li(a))
b = sorted(make_li(b),key=lambda x : -x)

len_a = len(a)
len_b = len(b)
i,j = 0,0
ans = 0
while i < len_a and j < len_b:
    if a[i] + b[j] == t:
        
        c1=1
        c2=1
        
        i+=1
        j+=1
        
        while i < len_a and a[i] == a[i-1]:
            c1 += 1
            i += 1
        
        while j < len_b and b[j] == b[j-1]:
            c2 += 1
            j += 1
        
        ans += c1*c2
        
    elif a[i] + b[j] < t :
        i+=1
    else:
        j+=1

print(ans)