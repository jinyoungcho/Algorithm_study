n = 10

visited = set()

for _ in range(n):

    num = int(input())

    remain = num % 42

    visited.add(remain)

print(len(visited))