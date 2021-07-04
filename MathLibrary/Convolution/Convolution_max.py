# A: array of length N
# B: array of length M
# C: array of length max(N, M)
# C[k] = sum(A[i]*B[j] for 0 <= i < N, 0 <= j < M| max(i, j) == k)

SA = [0]*(N+1)
SB = [0]*(M+1)
for i in range(N):
    SA[i+1] = SA[i] + A[i]
for i in range(M):
    SB[i+1] = SB[i] + B[i]
for i in range(max(N, M)):
    if i < min(N, M):
        C[i] = A[i]*B[i]
    if i < N:
        C[i] += A[i]*SB[min(i, M)]
    if i < M:
        C[i] += B[i]*SA[min(i, N)]
print(*C)
