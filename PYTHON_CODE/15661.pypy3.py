N = int(input())
a = [
     list(map(int,input().split())) for _ in range(N)
]

#N = 6
#a = [
#    [0,1,2,3,4,5],
#    [1,0,2,3,4,5],
#    [1,2,0,3,4,5],
#    [1,2,3,0,4,5],
#    [1,2,3,4,0,5],
#    [1,2,3,4,5,0]
#]

def go(team, team2):
    tp1 = 0
    tp2 = 0
    if len(team) > 1:
        for i in team:
            for j in team:
                tp1 += a[i][j]
    
    if len(team2) > 1:
        for i in team2:
            for j in team2:
                tp2 += a[i][j]
    
    return abs(tp1-tp2)

from itertools import combinations

all_team = {i for i in range(N)}
ans = 999999999
for i in range(1,N//2+1):
    for j in combinations(all_team,r=i):
        team = set(j)
        team2 = all_team-set(j)
        temp = go(team, team2)
        
        ans = min(ans,temp)

print(ans)