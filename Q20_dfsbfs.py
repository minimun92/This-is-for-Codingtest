#https://www.acmicpc.net/problem/18428
import sys
input = sys.stdin.readline

n = int(input())
graph = []
teachers = []

for i in range(n):
    graph.append(list(input().rstrip().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i,j))

# 방향별로 
def watch(x,y,dir):
    # 왼쪽 방향으로 감시
    if dir == 0:
        while y >= 0:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if dir == 1:
        while y < n:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            y += 1
    # 위쪽 방향으로 감시
    if dir == 2:
        while x >= 0:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if dir == 3:
        while x < n:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            x += 1
    return False

# T 전파 하는데 
# S 만나면 True
# O 만나면 False
# 방향 4개 살펴보기
def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
    return False

ans = False
def make_wall(wall):
    global ans
    # 장애물이 3개면 T전파 시작
    if wall == 3:
        # 학생 안 만나면 감시를 피할 수 있다 False -> 피하게 할 수 있음 : ans = True
        # 만나면 감시를 못피한다 True -> 피하게 할 수 없음 : ans = False
        if not process():
            ans = True
        return
    
    # 장애물이 아직 3개가 아니면 또세워
    else :
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    make_wall(wall+1)
                    graph[i][j] = 'X'

# O 3개 세우기
make_wall(0)

if ans:
    print('YES')
else :
    print('NO')
