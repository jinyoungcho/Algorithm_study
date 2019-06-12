# N보다 작고 4와 7로만 이루어진 숫자중 가장 큰것

N_str = input()

N = int(N_str)

len_N = len(N_str)

a = ['4','7']
MAXI = 0
def dfs(cnt,num_str):
    global MAXI

    if cnt == len_N:
        if N >= int(num_str):
            MAXI = max(MAXI,int(num_str))
        return
    if num_str !='':
        if N >= int(num_str):
            MAXI = max(MAXI, int(num_str))

    # print(num_str)
    for _ in range(2):

        choosen_str = a[_]

        dfs(cnt+1,num_str+choosen_str)
dfs(0,'')
print(MAXI)