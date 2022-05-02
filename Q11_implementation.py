from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * (n) for _ in range(n)]

k = int(input()) # 사과 위치
for i in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1

    
# L = 방향 변환 횟수
l = int(input())
# x : 시간 c : 방향
time_info = []
dir_info = []
for i in range(l):
    a,b = input().split()
    time_info.append(int(a))
    dir_info.append(b)
    
# 방향 0 : →  1 : ↓  2 : ←  3 : ↑
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def change_dir(dir, c):
    if c == 'L': # 왼쪽
        dir -= 1
    else : # 'D' : 오른쪽
        dir += 1
    return dir % 4

dir = 0
info_index = 0
ans = 0 # 시간
x,y = 0,0
graph[0][0] = 2 # 자기 몸은 2
q = deque([(0,0)])

while True:
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 계속 진행되는 조건 : 그래프 범위 내이고 자기 몸이 아니면 진행
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 2:
        # 사과가 있으면
        if graph[nx][ny] == 1:
            graph[nx][ny] = 2
            q.append((nx,ny))

        # 사과가 없으면
        else :
            graph[nx][ny] = 2
            q.append((nx,ny))
            _x,_y = q.popleft()
            graph[_x][_y] = 0

        ans += 1
        x,y = nx,ny
    # 끝나는 조건
    else :
        ans += 1
        break

    # 시간지나면 방향 변경. and 조건 순서가 바뀌면 loop가 안돌아감.....?
    if info_index < l and ans == time_info[info_index]:
        dir = change_dir(dir,dir_info[info_index])
        info_index += 1

print(ans)
