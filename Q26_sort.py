import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
for i in range(n):
    heapq.heappush(q, int(input()))

result = 0

while len(q) != 1:
    first = heapq.heappop(q)
    second = heapq.heappop(q)

    sum = first + second
    result += sum

    heapq.heappush(q, sum)

print(result)
