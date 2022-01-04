import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

# median
print(data[(n-1)//2])
