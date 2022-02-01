#https://www.acmicpc.net/problem/14502
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n, m = map(int, input().split())

# 빈칸 0 -- 벽 1 -- 바이러스 2
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

temp = [[0] * m for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         print(temp[i][j], end = ' ')
#     print()

def get_zero():
    zero = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                zero += 1
    return zero

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if temp[nx][ny] == 0:
            #순서 중요
            temp[nx][ny] = 2
            virus(nx,ny)
            # graph[nx][ny] = 2

ans = 0
def dfs(wall):
    global ans
    # 벽 세우기
    if wall != 3:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    dfs(wall+1)
                    graph[i][j] = 0

    # 벽 다 세웠으면 바이러스 전파 시작
    else :
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if graph[i][j] == 2:
                    virus(i,j)

        ans = max(ans, get_zero())
        return

dfs(0)
print(ans)
