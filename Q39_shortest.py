import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n = int(input())
distance = [[INF] * (n) for _ in range(n)]

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dijkstra(x,y):
    q = []
    heapq.heappush(q,(graph[x][y],x,y))
    distance[x][y] = graph[x][y]

    while q:
        dist,x,y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,(cost,nx,ny))

dijkstra(0,0)
print(distance[n-1][n-1])
