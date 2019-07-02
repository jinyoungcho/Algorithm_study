for t in range(1,11):

    N,li = input().split()
    N=int(N)
    li = list(li)


    idx,jdx =0,1

    while(jdx<len(li)):
        # print(li)
        if li[idx] == li[jdx]:
            li.pop(idx)
            li.pop(idx)

            idx-=1
            jdx-=1
        else:
            idx+=1
            jdx+=1
    print("#",end='')
    print(t,''.join(li))
