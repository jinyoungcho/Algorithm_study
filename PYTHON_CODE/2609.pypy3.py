# 1. set

# n = 10
# visited = set()
# for _ in range(n):
#     num = int(input())
#     remain = num % 42
#     visited.add(remain)
# print(len(visited))

# 2. bool-array
# n = 10                              # 총 입력 갯수 10개
# check = [False] * 42              # input%42 나머지값범위 (0~41)
# ans = 0                             # 정답
# for _ in range(n):                  # n번 돌기
#     input_number = int(input())     # 39 << 40 << 41 .. 순서대로 입력
#     remain = input_number % 42      # 42로 나눈 나머지값
#     if not check[remain]:         # 방문하지 않았다면
#         check[remain] = True        # 방문처리
#         ans += 1                    # count 해주기
#     else:                         # 이미 방문했었으면 넘어가기
#         continue
#
# print(ans)

in1, in2 = list(map(int,input().split()))

# 최대공약수


def gcd(a,b):
    a, b = min(a, b), max(a, b)
    while a % b > 0:
        a, b = b, a % b
    return b


def lcm(a,b):
    return a*b//gcd(a, b)


print(gcd(in1, in2))
print(lcm(in1, in2))