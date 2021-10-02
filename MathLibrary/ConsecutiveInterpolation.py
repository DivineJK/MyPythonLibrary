def getConsecutiveInterpolation(y, left, target, mod = 998244353):
    n = len(y)
    target %= mod
    if left <= target and target < left + n:
        return y[target-left]
    fact = [1]*(n+1)
    invf = [1]*(n+1)
    for i in range(n):
        fact[i+1] = fact[i] * (i + 1) % mod
    invf[-1] = pow(fact[-1], mod-2, mod)
    for i in range(n, 0, -1):
        invf[i-1] = invf[i] * i % mod
    r = [1]*(n+1)
    for i in range(n):
        r[n-i-1] = r[n-i] * (target+i-left-n+1) % mod
    f = 0
    sign = 1
    if n & 1:
        sign = 1
    else:
        sign = mod-1
    l = 1
    for i in range(n):
        t = l*r[i+1]%mod*invf[i]%mod*invf[n-1-i]%mod
        f = (f + t*sign%mod*y[i])%mod
        sign = sign * (mod - 1) % mod
        l = l * (target - i - left) % mod
    return f
