n = int(input())
li = [list(map(int,(input().split(" ")))) for i in range(n)]

a,b,c,d = zip(*li)

from collections import defaultdict
ab_dic = defaultdict(lambda : 0)
cd_dic = defaultdict(lambda : 0)

for i in range(n):
    for j in range(n):
        ab_dic[a[i]+b[j]] +=1
        
for i in range(n):
    for j in range(n):
        cd_dic[c[i]+d[j]] +=1
        
ans = 0
for i in ab_dic.keys():
    ans += cd_dic[-i] * ab_dic[i]

print(ans)