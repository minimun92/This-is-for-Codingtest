import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
build_frame = []
for i in range(m):
    build_frame.append(list(map(int, input().split())))

def possible(graph):
    for x,y,stuff in graph:
        if stuff == 0:
            if y == 0 or [x-1,y,1] in graph or [x,y,1] in graph or [x,y-1,0] in graph:
                continue
            return False
        elif stuff == 1:
            if [x,y-1,0] in graph or [x+1,y-1,0] in graph or ([x-1,y,1] in graph and [x+1,y,1] in graph):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0: # 삭제
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        if operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    
    return sorted(answer)



print(solution(n, build_frame))


'''
input#1
5
8
1 0 0 1
1 1 1 1
2 1 0 1
2 2 1 1
5 0 0 1
5 1 0 1
4 2 1 1
3 2 1 1

input#2
5
10
0 0 0 1
2 0 0 1
4 0 0 1
0 1 1 1
1 1 1 1
2 1 1 1
3 1 1 1
2 0 0 0
1 1 1 0
2 2 0 1
'''
