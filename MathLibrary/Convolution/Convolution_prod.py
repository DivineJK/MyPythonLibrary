for i in range(1, 100001):
    for j in range(1, 100000//i+1):
        C[i*j-1] += A[i-1]*B[j-1]
