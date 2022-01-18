from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline

n,x = map(int, input().split())
data = list(map(int, input().split()))

left = bisect_left(data,x)
right = bisect_right(data,x)

ans = right - left

if ans == 0:
    print(-1)
else :
    print(ans)
