import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

ans = 1
for coin in data:
    if ans < coin :
        break
    ans += coin

print(ans)
