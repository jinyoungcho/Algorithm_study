L,C = list(map(int,input().split()))

li = list(input().split())

c_li = [False]* 26

for ch in li:
    c_li[ord(ch)-ord('a')] = True

# print(c_li)

#최소 하나의 모음, 최소 두개의 자음

def make_chr(num_li):
    string = ''
    for num in num_li:
        string += chr(num + ord('a'))

    return string

def dfs(num_za, num_mo, cnt, chosen):

    if cnt == L:

        if num_za >=2 and num_mo >= 1:
            s = make_chr(chosen)
            print(s)

    if chosen == []:
        for _ in range(26):
            if c_li[_] == True:

                c_li[_] = False

                if chr(_ + ord('a')) in ['a', 'e', 'i', 'o', 'u']:

                    dfs(num_za, num_mo + 1, cnt + 1, chosen + [_])
                else:
                    dfs(num_za + 1, num_mo, cnt + 1, chosen + [_])

                c_li[_] = True
    else:
        for _ in range(chosen[-1], 26):
            if c_li[_] ==  True:

                c_li[_] = False

                if chr( _ + ord('a') ) in ['a','e','i','o','u']:

                    dfs(num_za, num_mo + 1, cnt+1, chosen + [_])
                else:
                    dfs(num_za + 1, num_mo, cnt+1, chosen + [_])

                c_li[_] = True

dfs(0,0,0,[])