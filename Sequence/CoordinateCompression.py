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
