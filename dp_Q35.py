import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
dp[1] = 1

ugly = 2  
for i in range(2,n+1):
    if ugly%2==0 or ugly%3==0 or ugly%5==0:
        dp[i] = ugly
    else :
        ugly += 1
        dp[i] = ugly

    ugly += 1
print(dp[n])
