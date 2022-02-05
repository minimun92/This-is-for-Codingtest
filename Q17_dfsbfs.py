#https://www.acmicpc.net/problem/18405
from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())

graph = []
virus = []
for i in range(n):
    graph.append(list(map(int, input().split())))

target_s,target_x,target_y = map(int, input().split())


for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            #바이러스 종류, 시간, 좌표
            virus.append((graph[i][j],0,i,j))

# for i in range(n):
#     for j in range(n):
#         print(graph[i][j], end = ' ')
#     print()

dx = [0,1,0,-1]
dy = [1,0,-1,0]

virus.sort()
q = deque(virus)
# 이거 차이 잘 모르겠다
# q = deque()
# q.append(virus)
# print(q.popleft())


while q:
    now_virus, now_s, now_x, now_y = q.popleft()

    if now_s == target_s:
        break
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = now_virus
            q.append((graph[nx][ny],now_s+1,nx,ny))
    # print(q)
# for i in range(n):
#     for j in range(n):
#         print(graph[i][j], end = ' ')
#     print()
print(graph[target_x-1][target_y-1])
