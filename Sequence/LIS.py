def LIS(n, a):
    longest = [n]*(n+1)
    longest[0] = -1
    m = min(a)
    L = 0
    prev = [m-1]*n
    for i in range(n):
        if L == 0:
            longest[1] = i
            L = 1
        else:
            l, r = 1, L+1
            d = (l + r) // 2
            if a[longest[l]] > a[i]:
                d = 0
            else:
                while r - l > 1:
                    if a[longest[d]] <= a[i]:
                        l = d
                    else:
                        r = d
                    d = (l + r) // 2
            newL = d + 1
            prev[i] = longest[newL-1]
            longest[newL] = i
            if newL > L:
                L = newL
    return L, longest, prev
