import sys
input = sys.stdin.readline

n = int(input())
T,P = [0]*n, [0]*n
for i in range(n):
    T[i],P[i] = map(int, input().split())


dp = [0] * 20

for i in range(n):
    # i일까지의 보상이 다음날까지의 보상보다 크면 갱신
    if dp[i+1] < dp[i]:
        dp[i+1] = dp[i]
    # T일 후에 받을 금액이 현재 보상보다 크면 갱신
    if dp[i+T[i]] < dp[i] + P[i]:
        dp[i+T[i]] = dp[i] + P[i]


print(dp[n])
