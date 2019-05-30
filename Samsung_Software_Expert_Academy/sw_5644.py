T = int(input())
di = [0, -1, 0, 1, 0]
dj = [0, 0, 1, 0, -1]

for t in range(1,T+1):

    M, A = list(map(int,input().split()))

    person_A = [0]+list(map(int, input().split()))
    person_B = [0]+list(map(int, input().split()))

    AP = [list(map(int,input().split()))+[_] for _ in range(A)]

    p1=[0,0]
    p2=[9,9]


    def get_ap(p):

        ap_for = []

        pi = p[0]
        pj = p[1]

        for ap in AP:
            aj=ap[0]-1
            ai=ap[1]-1

            if abs(pi-ai) + abs(pj-aj) <= ap[2]:
                ap_for.append(ap)

        return ap_for

    get_max = 0

    for _ in range(M+1):

        p1[0] += di[person_A[_]]
        p1[1] += dj[person_A[_]]

        p2[0] += di[person_B[_]]
        p2[1] += dj[person_B[_]]

        ap_for_p1 = get_ap(p1)
        ap_for_p2 = get_ap(p2)
        # print(_)
        # print(ap_for_p1, ap_for_p2)

        if len(ap_for_p1) != 0 and len(ap_for_p2) == 0:
            MAXI = 0
            for ap_p1 in ap_for_p1:
                MAXI = max(ap_p1[3], MAXI)
            get_max += MAXI
        elif len(ap_for_p1) == 0 and len(ap_for_p2) != 0:
            MAXI = 0
            for ap_p2 in ap_for_p2:
                MAXI = max(ap_p2[3], MAXI)
            get_max += MAXI
        else:
            MAXI = 0
            for ap_p1 in ap_for_p1:
                for ap_p2 in ap_for_p2:

                    if ap_p1 == ap_p2:
                        MAXI = max(MAXI, ap_p1[3])
                    else:
                        MAXI = max(MAXI, ap_p1[3] + ap_p2[3])

            get_max += MAXI

    print("#",end="")
    print(t,get_max)