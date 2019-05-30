MAX = 1000000
prime = [True for _ in range(MAX+1)]


#  step 1

#  i 의 배수는 다 false
for i in range(2, MAX+1):
    if i*i > MAX:
        break
    if prime[i]:
        for j in range(i*i, MAX+1, i):
            prime[j] = False



while True:
    num = int(input()) # 입력조건 4 <= n and n % 2 == 0

    if num == 0:
        break

    for i in range(2, MAX+1):
        if prime[i]:            # 작은 소수 하나 찾고~
            j = num - i         # 큰 소수 찾기
            if prime[j]:
                print(num, "=", i, "+", j)
                break