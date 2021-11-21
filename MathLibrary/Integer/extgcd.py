# extgcd: 二元一次整数方程式ax + by = cを満たすような整数の組(x, y)を求める。存在しなければ(-1, -1)で、存在すれば0≤x<|b|を満たすようなもの。
def extgcd(a, b, c):
    if b == 0:
        if a == 0:
            if c == 0:
                return 0, 0
            return -1, -1
        if c % a == 0:
            return c // a, 0
        return -1, -1
    x, y, u, v, k, l = 1, 0, 0, 1, a, b
    while l:
        x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
        k, l = l, k % l
    if k < 0: k = -k
    if c % k: return -1, -1
    a, b, c = a // k, b // k, c // k
    if b < 0: a, b, c = -a, -b, -c
    x *= c
    y *= c
    u = (b - x - 1) // b
    return x+u*b, y-u*a
