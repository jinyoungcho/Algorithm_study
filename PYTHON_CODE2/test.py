
# 11 & 1<<2

wall = 1

k = 0 #서

print(bool(~wall & (1<<k)))

k = 1 # 북

print(bool(~wall & (1<<k)))

k = 2 # 동

print(bool(~wall & (1<<k)))

k = 3 # 남

print(bool(~wall & (1<<k)))