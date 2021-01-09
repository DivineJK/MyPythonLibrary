def manacher(s):
    n = len(s)
    if n == 0:
        return [0]
    v = [0]*(2*n-1)
    v[0] = ord(s[0])
    m = ord(s[0])
    for i in range(1, n):
        v[2*i] = ord(s[i])
        m = max(m, v[2*i])
    m += 1
    for i in range(n-1):
        v[2*i+1] = m
    i, j = 0, 0
    n = 2*n-1
    R = [0]*n
    while i < n:
        # i: center of palindrome index, j: radius of parindrome
        while j <= i and j < n - i and v[i-j] == v[i+j]:
            j += 1
        R[i] = j
        k = 1
        while i >= k and k + R[i-k] < j:
            R[i+k] = R[i-k]
            k += 1
        i += k
        j -= k
    for t in range(n):
        if R[t] <= t and R[t] < n - t:
            R[t] -= 1
    return R
