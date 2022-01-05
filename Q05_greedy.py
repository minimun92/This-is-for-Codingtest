# page 452
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

total = len(list(combinations(data,2)))

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if data[i] == data[j]:
            cnt += 1

print(total - cnt)
