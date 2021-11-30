import sys
input = sys.stdin.readline

#ValueError: invalid literal for int() with base 10: '\n'
data = input().rstrip()

ans = int(data[0])
length = len(data)

for i in range(1,length):
    if ans <= 1 or int(data[i]) <= 1:
        ans += int(data[i])
    else :
        ans *= int(data[i])

print(ans)
