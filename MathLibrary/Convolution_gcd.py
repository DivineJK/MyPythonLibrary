# A: array of length N
# B: array of length M
# C: array of length L
# C[k] = sum(A[i]*B[j] for {i, j | gcd(i, j) = k})

for i in range(N):
    for j in range(2*(i+1), M+1, i+1):
        A[i] += A[j-1]
for i in range(M):
    for j in range(2*(i+1), M+1, i+1):
        B[i] += B[j-1]
C = [A[i]*B[i]%mod for i in range(M)]
for i in range(M, 0, -1):
    for j in range(2*i, M+1, i):
        C[i-1] -= C[j-1]
        C[i-1] %= mod
