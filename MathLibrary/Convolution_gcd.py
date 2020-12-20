# A: array of length N
# B: array of length M
# C: array of length L
# C[k] = sum(A[i]*B[j] for {i, j | gcd(i, j) = k})

for i in range(N):
    for j in range(2*(i+1), N+1, i+1):
        A[i] += A[j-1]
for i in range(M):
    for j in range(2*(i+1), M+1, i+1):
        B[i] += B[j-1]
if N < L:
    A = A[:] + [0]*(L-N)
if M < L:
    B = B[:] + [0]*(L-M)
C = [A[i]*B[i] for i in range(L)]
for i in range(L, 0, -1):
    for j in range(2*i, L+1, i):
        C[i-1] -= C[j-1]
