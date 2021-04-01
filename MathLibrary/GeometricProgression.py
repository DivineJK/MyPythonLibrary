def geometric_prog(r, n, modulo=0): # sum(r^i for i in range(n)) % modulo
    if n <= 0:
        return 0
    if n == 1:
        return 1
    S = 0
    left = 0
    if n % 2:
        if modulo:
            S = pow(r, n-1, modulo)
        else:
            S = pow(r, n-1)
    if modulo:
        left = (pow(r, n//2, modulo) + 1) % modulo
    else:
        left = pow(r, n//2) + 1
    S = (S + left * geometric_prog(r, n//2, modulo))
    if modulo:
        S %= modulo
    return S
def geometric_expect(r, n, modulo=0): # sum(i*r^i for i in range(n)) % modulo
    if n <= 1:
        return 0
    S = (n//2)*geometric_prog(r, n//2, modulo)
    if modulo:
        S = S * pow(r, n//2, modulo) % modulo
    else:
        S = S * pow(r, n//2)
    left = 0
    if n % 2:
        if modulo:
            S = (S + (n - 1) * pow(r, n-1, modulo)) % modulo
        else:
            S += (n - 1) * pow(r, n-1)
    if modulo:
        left = (pow(r, n//2, modulo) + 1) % modulo
    else:
        left = pow(r, n//2) + 1
    S = (S + left * geometric_expect(r, n//2, modulo))
    if modulo:
        S %= modulo
    return S
