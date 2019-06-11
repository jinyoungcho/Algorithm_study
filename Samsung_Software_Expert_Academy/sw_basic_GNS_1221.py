code = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
testcase = int(input())
for tc in range(1, testcase+1):
    n = input()
    s = input()
    ans = ''
    for i in range(len(code)):
        ans += (code[i] + ' ')*s.count(code[i])
    print("#%d\n%s" %(tc,ans))