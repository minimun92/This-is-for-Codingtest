from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline
data_len = 10001

words = list(map(str, input().split()))
queries = list(map(str, input().split()))

data = [[] for _ in range(data_len)]
reversed_data = [[] for _ in range(data_len)]

def count_by_range(arr,left_value, right_value):
    right_index = bisect_right(arr,right_value)
    left_index = bisect_left(arr,left_value)
    return right_index - left_index

def solution(words, queries):
    answer = []
    for word in words:
        data[len(word)].append(word)
        reversed_data[len(word)].append(word[::-1])

    for i in range(data_len):
        data[i].sort()
        reversed_data[i].sort()
    
    for q in queries :
        if q[0] != '?':
            res = count_by_range(data[len(q)], q.replace('?','a'), q.replace('?', 'z'))
        else :
            res = count_by_range(reversed_data[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?', 'z'))
        answer.append(res)     
    return answer

print(solution(words,queries))
