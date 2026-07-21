def fibRecurBrute(n):
    if n <= 2:
        return 1
    return fibRecurBrute(n - 1) + fibRecurBrute(n - 2)

def fibRecurDP(n, dp):
    if n <= 2:
        return 1
    dp[n] = fibRecurDP(n - 1, dp) + fibRecurDP(n - 2, dp)
    return dp[n]

def fibIterDP(n):
    if n == 1:
        return 1
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]



for i in range(int(input())):
    n = int(input())
    dp = [-1] * (n + 1)
    print(fibRecurBrute(n))
    print(*dp)
    print(fibRecurDP(n, dp))
    print(*dp)
    print(fibIterDP(n))
    print(*dp)