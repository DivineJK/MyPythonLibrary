def convolution_prod(f, g):
    n = len(f)
    res = [0]*n
    for i in range(n):
        for j in range(n//(i+1)):
            res[(i+1)*(j+1)-1] += f[i] * g[j]
        print(n-(i+1)*(n//(i+1)) < i+1)
    return res
