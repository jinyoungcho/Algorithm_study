n,m = list(map(int,input().split(" ")))

a = []
for _ in range(n):
    a.append(list(input()))

_ri,_rj = 0,0
_bi,_bj = 0,0
_gi,_gj = 0,0
for i in range(n):
    for j in range(m):
        if a[i][j] == 'R':
            _ri,_rj = i,j
            a[i][j] = '.'
        elif a[i][j] == 'B':
            _bi,_bj = i,j
            a[i][j] = '.'
        elif a[i][j] == 'O':
            _gi,_gj = i,j
            
di = [1,-1,0,0]
dj = [0,0,1,-1]

check = [[ [ [False] * m for i in range(n)] for j in range(m)] for k in range(n)]
check[_ri][_rj][_bi][_bj] = True #현재 상태 TRUE

from collections import deque
q = deque()
q.append((_ri,_rj,_bi,_bj,0))

def move(_i,_j,_di,_dj,_c):
    while a[_i+_di][_j+_dj] != '#':
        _i += _di
        _j += _dj
        _c += 1
        if a[_i][_j] == 'O':
            break
            
    return _i,_j,_c


def bfs():
    while q:
        ri,rj,bi,bj,cnt = q.popleft()
        
        if cnt >= 10: #열번 돌았으면 break
            break
        
        for k in range(4): # k 방향으로 움직여 보자~!
            nri,nrj,rc = move(ri,rj,di[k],dj[k],0)
            nbi,nbj,bc = move(bi,bj,di[k],dj[k],0)
            if a[nbi][nbj] == 'O': # 파란구술이 빠졌다..!?
                continue
            if a[nri][nrj] == 'O': #빨간구술만 빠졌다..!?
                print(cnt+1)
                return
            
            if nri == nbi and nrj == nbj: #두 구슬이 같은위치
                if rc > bc: #빨간색이 더 많이 움직였다?
                    nri -= di[k]
                    nrj -= dj[k]
                else:       #파란색이 더 많이 움직였다?
                    nbi -= di[k]
                    nbj -= dj[k]
            
            if not check[nri][nrj][nbi][nbj] == True:
                check[nri][nrj][nbi][nbj] = True
                q.append((nri,nrj,nbi,nbj,cnt+1))
    
    print("-1")

bfs()