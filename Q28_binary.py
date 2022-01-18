import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

start = 0
end = n-1
ans = -1

while (start <= end):
    mid = (start+end)//2

    if data[mid] < mid:
        start = mid + 1
    elif data[mid] > mid:
        end = mid - 1
    else:
        ans = mid
        break
print(ans)
