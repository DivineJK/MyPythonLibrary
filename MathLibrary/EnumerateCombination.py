def enumComb(n, k):
    if n < k:
        return []
    l = [i for i in range(k)]
    res = []
    while True:
        res.append([i for i in l])
        ptr = k - 1
        while l[ptr] + k - 1 - ptr >= n - 1:
            ptr -= 1
            if ptr < 0:
                break
        if ptr < 0:
            break
        l[ptr] += 1
        for i in range(ptr + 1, k):
            l[i] = l[i - 1] + 1
    return res
