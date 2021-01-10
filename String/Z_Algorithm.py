def z_algorithm(s):
    n = len(s)
    z = [0]*n
    c = 0
    for i in range(1, n):
        if i + z[i-c] < c + z[c]:
            # reusing results
            # 
            z[i] = z[i-c]
        else:
            j = max(0, c + z[c] - i)
            while i + j < n and s[j] == s[i+j]:
                j += 1
            z[i] = j
            c = i
    z[0] = n
    return z
