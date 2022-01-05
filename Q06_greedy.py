import heapq
import sys
input = sys.stdin.readline

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    length = len(food_times)
    q = []  # 음식시간, 음식번호 순
    for i in range(length):
        heapq.heappush(q, (food_times[i],i+1))

    sum_time, prev_time = 0, 0
    # sum_time : 여태까지 먹은 음식 시간
    # prev_time : 이전에 먹은 음식 시간
    while sum_time + ((q[0][0] - prev_time) * length) <= k:
        now_time = heapq.heappop(q)[0]
        sum_time += (now_time - prev_time) * length
        prev_time = now_time
        length -= 1
    
    # 우선순위큐 -> 음식번호순 
    result = sorted(q, key = lambda x:x[1])
    return result[(k - sum_time) % length][1]

food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times,k))
