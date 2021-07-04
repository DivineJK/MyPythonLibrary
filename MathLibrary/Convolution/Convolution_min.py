# A: array of length N
# B: array of length M
# C: array of length min(N, M)
# C[k] = sum(A[i]*B[j] for 0 <= i <= N-1, 0 <= j <= M-1| min(i, j) == k)

SA = [0]*(N+1)
SB = [0]*(M+1)
for i in range(N):
    SA[i+1] = SA[i] + A[i]
for i in range(M):
    SB[i+1] = SB[i] + B[i]
for i in range(min(N, M)):
    C[i] = A[i]*B[i] + A[i]*(SB[M] - SB[i+1]) + B[i]*(SA[N] - SA[i+1])
print(*C)
