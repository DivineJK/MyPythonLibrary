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
        return self.ft_sum(r) - self.ft_sum(l)
