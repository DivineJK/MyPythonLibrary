def proceedLinearSieve(n):
    primes = []
    lpf = [-1]*(n+1)
    for i in range(2, n+1):
        if lpf[i] == -1:
            primes.append(i)
            lpf[i] = i
        for p in primes:
            if p * i > n or p > lpf[i]:
                break
            lpf[p * i] = i
    return primes
