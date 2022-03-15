import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())

distance = [INF] * (n+1)
distance[0] = -1
graph = [[] * n for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now_node = heapq.heappop(q)
        if distance[now_node] < dist:
            continue
        for i in graph[now_node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
                
dijkstra(1)

ans_num = 0
ans_dist = max(distance)
ans_cnt = 0
for i in range(n+1):
    if distance[i] == ans_dist:
        ans_num = i
        break
        
ans_cnt = distance.count(ans_dist)
print(ans_num,ans_dist,ans_cnt)
