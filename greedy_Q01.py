import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

ans = 0
cnt = 0
for man in data:
    cnt += 1
    if cnt >= man:
        ans += 1
        cnt = 1

print(ans)
