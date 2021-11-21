def gcd(a, b):
    while b:
        a, b = b, a % b
    if a < 0: return -a
    return a
