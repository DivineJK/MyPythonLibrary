class segment_tree:
    #        n: length of array
    #       op: monoid (a op (b op c) == (a op b) op c)
    # identity: identity of operation (ex. min -> INF, + -> 0, gcd -> 0, ...)
    #  initial: initial state of bottom of segment tree
    #      upd: update function
    def __init__(self, n, op, identity, upd, initial=[]):
        self.n = n
        self.op = op
        self.identity = identity
        self.upd = upd
        tmp = n - 1
        self.cnt = 0
        while tmp:
            self.cnt += 1
            tmp >>= 1
        self.bin_top = 1 << self.cnt
        self.segtree = [self.identity]*(self.bin_top<<1)
        if initial != []:
            for i in range(n):
                self.segtree[i+self.bin_top] = initial[i]
                tmp = (i + self.bin_top) >> 1
                for j in range(self.cnt):
                    self.segtree[tmp] = self.op(self.segtree[2*tmp], self.segtree[2*tmp+1])
                    tmp >>= 1
    def update(self, p, x):
        tmp = p + self.bin_top
        self.segtree[tmp] = self.upd(self.segtree[tmp], x)
        tmp >>= 1
        for i in range(self.cnt):
            self.segtree[tmp] = self.op(self.segtree[2*tmp], self.segtree[2*tmp+1])
            tmp >>= 1
    def get_segment(self, l, r): # interval == [l, r)
        res = self.identity
        L, R = l + self.bin_top, r + self.bin_top
        lseg = []
        rseg = []
        while L < R:
            if L & 1:
                lseg.append(L)
                L += 1
            if R & 1:
                rseg.append(R-1)
                R -= 1
            L >>= 1
            R >>= 1
        rseg.reverse()
        for i in lseg:
            res = self.op(res, self.segtree[i])
        for i in rseg:
            res = self.op(res, self.segtree[i])
        return res
    def st_bisect(self, lower, upper, val):
        if self.get_segment(lower, upper) < val:
            return self.n
        if self.segtree[lower+self.bin_top] >= val:
            return lower
        l, r = lower, upper
        d = (l + r) // 2
        while r - l > 1:
            s = self.get_segment(lower, d+1)
            if s < val:
                l = d
            else:
                r = d
            d = (l + r) // 2
        return d + 1
