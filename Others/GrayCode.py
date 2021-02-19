def gray_code(n):
    res = [0]*(1<<n)
    for i in range(1, 1<<n):
        res[i] = res[i-1] ^ (i&-i)
    return res
