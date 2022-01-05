#https://www.acmicpc.net/problem/15483
import sys
input = sys.stdin.readline

str1 = input()  # source - 가로
str2 = input()  # destination - 세로

m = len(str1) # 가로
n = len(str2) # 세로

dp = [[0]*(m+1) for _ in range(n+1)]

for j in range(1,m+1):
    dp[0][j] = j
for i in range(1,n+1):
    dp[i][0] = i

# for i in range(n+1):
#     for j in range(m+1):
#         print(dp[i][j], end = ' ')
#     print()


for i in range(1,n+1):
    for j in range(1,m+1):
        if str1[j-1] == str2[i-1]:
            dp[i][j] = dp[i-1][j-1]
        else :
            dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

print(dp[i][j])

# for i in range(n+1):
#     for j in range(m+1):
#         print(dp[i][j], end = ' ')
#     print()
