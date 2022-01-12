import sys
input = sys.stdin.readline

n = int(input())
stages = list(map(int, input().split()))

length = len(stages)
result = [] * (n+1)

for i in range(1,n+1):
    ja = stages.count(i)
    if length == 0:
        result.append((i,0))
    else :
        result.append((i, ja / length))
    length -= ja

result = sorted(result, key=lambda x: x[1], reverse=True)

for i in result:
    print(i[0], end = ' ')
