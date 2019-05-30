N = int(input())

MAP = [input() for _ in range(N)]

# print(MAP)


def dfs(y,x,size):

    if size == 0:
        return


    c = True
    asdf = MAP[y][x]

    for i in range(y,y+size):
        for j in range(x,x+size):
            if asdf != MAP[i][j]:
                c = False
    # print(c)
    if c:
        print(asdf,end="")
    else:
        print("(",end="")
        dfs(y, x, size // 2)
        dfs(y, x + (size//2), size // 2)
        dfs(y + (size//2), x, size // 2)
        dfs(y + (size//2) , x + (size//2), size // 2)
        print(")",end="")

dfs(0,0,N)