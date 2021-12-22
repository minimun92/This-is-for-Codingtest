import sys
input = sys.stdin.readline

n = int(input())
T,P = [0]*n, [0]*n
for i in range(n):
    T[i],P[i] = map(int, input().split())


dp = [0] * 20

for i in range(n):
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    if dp[i+T[i]] < dp[i] + P[i]:
        dp[i+T[i]] = dp[i] + P[i]


print(dp[n])
