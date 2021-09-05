def calculateFloorCeilSum(n):
    # sum(sum(floor(a / b) + ceil(a / b) for b in range(1, n+1)) for a in range(1, n+1))
    res = n * n
    for b in range(1, n+1):
        res += n // b
    for b in range(1, n+1):
        t = n // b
        res += b * t * (t - 1)
        res += 2 * t * (n % b)
    return res
