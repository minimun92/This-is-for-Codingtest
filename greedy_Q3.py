import sys
input = sys.stdin.readline

data = input().rstrip()
ans = 1
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        ans += 1

print(ans//2)
