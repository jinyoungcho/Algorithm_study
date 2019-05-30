a = ["C","A","M","B","R","I","D","G","E"]
str_ = input()
ans = ""
for _ in str_:
    if _ in a:
        continue
    else:
        print(_,end="")