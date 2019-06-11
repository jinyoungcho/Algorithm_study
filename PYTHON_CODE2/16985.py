MAP = [[[0]*5 for _ in range(5)] for __ in range(5)]

for _ in range(5):
    for __ in range(5):
        MAP[_].append(list(int(input().split())))

for _ in range(5):
    print(MAP[_])