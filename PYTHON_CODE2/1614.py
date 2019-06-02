# Simulation

finger = int(input())
cnt = int(input())

if finger == 1:
    ans = 8 * cnt
elif finger == 5:
    ans = 8 * cnt + 4
else:
    temp = 4*cnt+1
    temp2 = 4-finger if cnt%2 == 1 else finger-2

    ans = temp+temp2

print(ans)


