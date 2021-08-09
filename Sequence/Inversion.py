def coordinate_compression(nums, rev=False):
    n = len(nums)
    tmp = sorted(nums, reverse=rev)
    d = [tmp[0]]
    prev = tmp[0]
    for i in range(1, n):
        if prev != tmp[i]:
            d.append(tmp[i])
        prev = tmp[i]
    D = {k: i for i, k in enumerate(d)}
    res = [D[nums[i]] for i in range(n)]
    return res

def Inversion(a):
    n = len(a)
    x = [a[i]*n+i for i in range(n)]
    y = coordinate_compression(x)
    fent = [0]*(n+1)
    cnt = 0
    for i in range(n):
        p = y[i] + 1
        while p <= n:
            fent[p] += 1
            p += p - (p & (p - 1))
        p = y[i] + 1
        cnt += i + 1
        while p:
            cnt -= fent[p]
            p &= p - 1
    return cnt
