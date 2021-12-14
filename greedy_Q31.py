import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    data = list(map(int, input().split()))
    dp = []
    index = 0
    for _ in range(n):
        dp.append(data[index:index+m])
        index += m
    
    for j in range(1, m):
        for i in range(n):
            # 상단
            if i == 0: 
                dp[i][j] = max(dp[i][j-1] + dp[i][j], dp[i+1][j-1] + dp[i][j])
            # 하단
            elif i == n-1: 
                dp[i][j] = max(dp[i-1][j-1] + dp[i][j], dp[i][j-1] + dp[i][j])
            # 중단
            else: 
                dp[i][j] = max(dp[i-1][j-1] + dp[i][j], dp[i][j-1] + dp[i][j], dp[i+1][j-1] + dp[i][j])
        
    ans = 0
    for i in range(n):
        ans = max(ans,dp[i][m-1])
    print(ans)
