#brute force..!


def check(r, c, size):
    global arr
    for i in range(size):
        for j in range(size):
            if arr[r+i][c+j] == 0:
                return False
    return True
def coloring(r, c, size, color):
    global arr
    for i in range(size):
        for j in range(size):
            arr[r + i][c + j] = color

def dfs(r, s):
    global arr, min_r, papers
    if s > min_r:
        return
    # print(r,s)
    for i in range(r, 10):
        for j in range(10):
            if arr[i][j] == 1: #색칠해보자
                for k in range(5, 0, -1): #5개 짜리부터 확인
                    if papers[k] and check(i, j, k): #해당 사이즈 종이가 남아있고, 칠할수 있다면
                        papers[k] -= 1
                        coloring(i, j, k, 0) #해당크기로 색칠해버리기

                        # print('-')
                        # for iii in range(10):
                        #     print(arr[iii])

                        dfs(i, s+1)
                        papers[k] += 1
                        coloring(i, j, k, 1)

                #색칠할 것이 없다면 밑으로가~
                return

    if min_r > s:
        min_r = s












arr = [0]*11
for i in range(10):
    arr[i] = list(map(int, input().split()))+[0]
arr[10] = [0 for _ in range(11)]
min_r = 987654321

papers = [0, 5, 5, 5, 5, 5]
dfs(0, 0)
if min_r == 987654321:
    min_r = -1
print(min_r)