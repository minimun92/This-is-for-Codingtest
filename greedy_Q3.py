import sys
input = sys.stdin.readline

data = input().rstrip()

cnt = 0
for i in range(1, len(data)):
    if data[i-1] != data[i]:
        cnt += 1

if cnt%2 == 0:
    print(cnt//2)
else :
    print(cnt//2 + 1)
