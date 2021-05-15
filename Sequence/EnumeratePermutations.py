N = 7
f = 1
for i in range(N):
    f *= i + 1
for i in range(f):
    L = [0]*N
    LL = [0]*N
    tmp = i
    for j in range(N):
        LL[N-j-1] = tmp % (j + 1)
        tmp //= j + 1
        L[j] = j
    perm = [0]*N
    for j in range(N):
        perm[j] = L[LL[j]]
        for k in range(LL[j], N-j-1):
            L[k] = L[k+1]
