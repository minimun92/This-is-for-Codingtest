import sys
input = sys.stdin.readline
from itertools import combinations
INF = int(1e9)

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 집: 1 | 치킨집: 2
house = []
chicken = []
ans = INF

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i,j))

for selected in combinations(chicken, m):
    dist = 0
    for i in house:
        chicken_len = INF
        for j in range(m):
            chicken_len = min(chicken_len, abs(i[0]-selected[j][0]) + abs(i[1]-selected[j][1]))
        dist += chicken_len
    ans = min(ans, dist)

print(ans)
