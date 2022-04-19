import sys
input = sys.stdin.readline

s = input().rstrip()

ans = []
num = 0
for i in s:
    if i.isalpha():
        ans.append(i)
    else :
        num += int(i)

ans.sort()
str = []
for i in ans:
    print(i, end = '')
print(num)
