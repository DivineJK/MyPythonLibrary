class fenwick_tree:
    def __init__(self, n, identity=0, initial=[]):
        self.n = n
        self.identity = identity
        self.op = lambda a, b: a + b
        self.iv = lambda a: -a
        self.ft = [identity]*(n+1)
        if initial != []:
            for i in range(n):
                x = i + 1
                while x <= n:
                    self.ft[x] = self.op(self.ft[x], initial[i])
                    x += x - (x & (x - 1))
    def ft_add(self, p, v):
        x = p + 1
        while x <= self.n:
            self.ft[x] = self.op(self.ft[x], v)
            x += x - (x & (x - 1))
    def ft_sum(self, x):
        S = self.identity
        if x <= 0:
            return S
        while x:
            S = self.op(S, self.ft[x])
            x = x & (x - 1)
        return S
    def get_segment(self, l, r):
        if l > r:
            return self.identity
        return self.op(self.ft_sum(r), self.iv(self.ft_sum(l)))
    def leftside(self, rank, l, r):
        ls = self.ft_sum(r)
        if ls < rank:
            return -1
        d = (l + r) // 2
        while r - l > 1:
            if self.ft_sum(d) + rank <= ls:
                l = d
            else:
                r = d
            d = (l + r) // 2
        return d
    def rightside(self, rank, l, r):
        rs = self.get_segment(l, r)
        c = l
        if rs <= rank:
            return self.n
        d = (l + r) // 2
        while r - l > 1:
            if self.get_segment(c, d) <= rank:
                l = d
            else:
                r = d
            d = (l + r) // 2
        return d
