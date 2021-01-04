class fenwick_tree:
    def __init__(self, n, initial=[]):
        self.n = n
        self.ft = [0]*(n+1)
        if initial != []:
            for i in range(n):
                x = i + 1
                while x <= n:
                    self.ft[x] += initial[i]
                    x += x - (x & (x - 1))
    def ft_add(self, p, v):
        x = p + 1
        while x <= self.n:
            self.ft[x] += v
            x += x - (x & (x - 1))
    def ft_sum(self, x):
        S = 0
        while x:
            S += self.ft[x]
            x = x & (x - 1)
        return S
    def get_segment(self, l, r):
        if l > r:
            return 0
        return self.ft_sum(r) - self.ft_sum(l)

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

def inversion(a):
    n = len(a)
    x = [a[i]*n+i for i in range(n)]
    y = coordinate_compression(x)
    fent = fenwick_tree(n)
    cnt = 0
    for i in range(n):
        fent.ft_add(y[i], 1)
        cnt += fent.get_segment(y[i]+1, n)
    return cnt
