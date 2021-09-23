# cond[i] == 1  => p[i] > p[i+1]
# cond[i] == 0  => Don't care for p[i], p[i+1]
# cond[i] == -1 => p[i] < p[i+1]
def countRestrictedPermutation(cond, m = int(1e9)+7):
    n = len(cond) + 1
    dp = [1]*(n+1)
    dp[0] = 0
    dp_prev = [1]*(n+1)
    dp_prev[0] = 0
    for i in range(2, n+1):
        for j in range(1, i+1):
            if cond[i-2] == -1:
                dp[j] = (dp[j-1] + dp_prev[j-1]) % m
            elif cond[i-2] == 1:
                dp[j] = (dp[j-1] + dp_prev[i-1] - dp_prev[j-1]) % m
            else:
                dp[j] = (dp[j-1] + dp_prev[i-1]) % m
            dp_prev[j-1] = dp[j-1]
        dp_prev[i] = dp[i]
        for j in range(i+1, n+1):
            dp[j] = dp[j-1]
            dp_prev[j] = dp[j]
    return dp[n]
def countRestrictedPermutationString(s, m = int(1e9) + 7):
    n = len(s)
    cond = [0]*n
    for i in range(n):
        if s[i] == '<':
            cond[i] = -1
        elif s[i] == '=':
            cond[i] = 0
        else:
            cond[i] = 1
    return countRestrictedPermutation(cond, m)
