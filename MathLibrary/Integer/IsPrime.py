def IsPrime(num):
    p = 2
    if num <= 1:
        return False
    while p * p <= num:
        if num % p == 0:
            return False
        p += 1
    return True
