def RLE(s):
    L = []
    n = len(s)
    cnt = 1
    now = s[0]
    for i in range(1, n):
        if s[i] != now:
            L.append((now, cnt))
            cnt = 1
            now = s[i]
        else:
            cnt += 1
    L.append((now, cnt))
    return L
