def common_subsequence(s, t, modulo=0):
    n, m = len(s), len(t)
    dp = [[1]*(m+1) for _ in range(n+1)]
    res = 1
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j]
            if s[i] == t[j]:
                dp[i+1][j+1] += dp[i][j]
                res += dp[i][j]
            if modulo:
                dp[i+1][j+1] %= modulo
                res %= modulo
    return res
