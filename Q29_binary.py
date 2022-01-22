import sys
input = sys.stdin.readline

n, c = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))
data.sort()

left = 1
right = data[n-1]-data[0]

while left <= right :
    mid = (left + right) //2
    
    start = data[0] # 설치 거리 이전 간격(~부터)
    cnt = 1 # 공유기 개수
    # 공유기 설치
    for i in range(1, n):
        dist = data[i] - start  # 공유기 설치 간격
        if mid <= dist:
            cnt += 1
            start = data[i]
    
    # 설치 거리가 좁으면 거리 증가
    if cnt >= c:
        left = mid + 1
        ans = mid
    # 넓으면 거리 감소
    else :
        right  = mid - 1


print(ans)
