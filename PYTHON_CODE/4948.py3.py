MAXI = 123456 * 2
prime = [True for _ in range(MAXI+1)]
prime[1] = False

#  step 1

#  i 의 배수는 다 false
for i in range(2, MAXI+1):
    if i*i > MAXI:
        break
    if prime[i] == True: #is prime?
        #yeah
        for j in range(i*i, MAXI+1, i): # 2,4,6 -> 4,8,12 -> 배수 제거
            prime[j] = False

# step 2
while(True):

    n = int(input())
    if n == 0:
        break

    n2 = n*2
    cnt = 0

    # print(n,n2)

    # num_prime gt n and elt 2n
    for _ in range(n+1,n2+1):
        if prime[_]:
            cnt += 1

    print(cnt)