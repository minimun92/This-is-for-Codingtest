#https://www.acmicpc.net/problem/18352

from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
dist = [(-1) for _ in range(n+1)]
dist[x] = 0

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

# print(graph)
# print(dist)

q = deque()
q.append(x) # x에서 시작

while q:
    now = q.popleft()
    for next in graph[now]:
        # 거리가 갱신되지 않았을때만 
        if dist[next] == -1:
            dist[next] = dist[now] + 1
            q.append(next)

# print(dist)

flag = False
for i in range(len(dist)):
    if dist[i] == k:
        print(i)
        flag = True
    
if flag == False:
    print(-1)
