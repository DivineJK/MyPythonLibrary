def enumerateIncreaseSequence(n, minNum, maxNum, leastInc):
    if n <= 0 or minNum > maxNum or minNum + (n - 1) * leastInc > maxNum:
        return []
    inc = leastInc
    if inc < 0:
        inc = 0
    lim = maxNum - (n - 1) * inc
    cur = [minNum + i * inc for i in range(n)]
    res = []
    while cur[0] <= lim:
        res.append([i for i in cur])
        pnt = n - 1
        while cur[pnt] + inc * (n - 1 - pnt) >= maxNum:
            pnt -= 1
            if pnt < 0:
                return res
        cur[pnt] += 1
        for i in range(pnt+1, n):
            cur[i] = cur[i-1] + inc
