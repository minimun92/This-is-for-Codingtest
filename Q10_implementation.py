import sys
input = sys.stdin.readline

key = []
key_len = int(input())
for i in range(key_len):
    key.append(list(map(int, input().split())))
lock = []
lock_len = int(input())
for i in range(lock_len):
    lock.append(list(map(int, input().split())))


def rotate(graph):
    n = len(graph)
    ret = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = graph[i][j]

    return ret

def check(start_x, start_y, key,lock, expend_size, start,end):
    expend_list = [[0] * expend_size for _ in range(expend_size)]

    for i in range(len(key)):
        for j in range(len(key)):
            expend_list[start_x + i][start_y + j] += key[i][j]

    for i in range(start,end):
        for j in range(start,end):
            expend_list[i][j] += lock[i-start][j-start]
            if expend_list[i][j] != 1:
                return False

    return True

def solution(key, lock):
    start = len(key) - 1
    end = start + len(lock)
    expend_size = len(lock) + start * 2
    
    for _ in range(4):
        for i in range(end):
            for j in range(end):
                if check(i,j,key,lock,expend_size,start,end):
                    return True
        key = rotate(key)

    return False

print(solution(key,lock))
