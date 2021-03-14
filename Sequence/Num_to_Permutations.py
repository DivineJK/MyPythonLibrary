def num_to_perm(n, k):
    perm = [i for i in range(n)]
    L = [0]*n
    for i in range(n):
        L[i] = k % (n - i)
        k //= (n - i)
    LL = [0]*n
    for i in range(n):
        LL[i] = perm[L[i]]
        for j in range(L[i], n-i-1):
            perm[j] = perm[j+1]
    return LL
