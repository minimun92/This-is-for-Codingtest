#https://www.acmicpc.net/problem/16234
from collections import deque
import sys
input = sys.stdin.readline

n,L,R = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y):
    people_sum = 0
    people_sum += graph[x][y]

    q = deque([(x,y)])
    union = [(x,y)]
    visit[x][y] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= n or 0 > ny or ny >= n or visit[nx][ny] == True:
                continue

            if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                q.append((nx,ny))
                union.append((nx,ny))
                people_sum += graph[nx][ny]
                visit[nx][ny] = True

    people_new = people_sum // len(union)
    for x,y in union:
        graph[x][y] = people_new

    return len(union)

ans = 0
# 인구이동 없을 때 까지 반복
while True:
    visit = [[False] * n for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            # 방문한 적이 없는 곳을 bfs 돌릴거임
            if not visit[i][j]:
                # bfs 결과값(연합국 수)가 1개면 연합국 이동이 없었다는 거임
                if bfs(i,j) > 1:
                    flag = True
    # 연합국 인구 이동이 없으면 바로 끝내라
    if not flag:
        break
        
    ans += 1
    
print(ans)
