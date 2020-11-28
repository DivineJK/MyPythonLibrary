class lazy_segment_tree:
    def __init__(self, n, op, identity, upd, upd_id, renew, initial=[]):
        self.n = n
        self.op = op
        self.identity = identity
        self.upd = upd
        self.upd_id = upd_id
        self.renew = renew
        tmp = n - 1
        self.cnt = 0
        while tmp:
            self.cnt += 1
            tmp >>= 1
        self.bin_top = 1 << self.cnt
        self.segtree = [identity]*(self.bin_top<<1)
        self.subtree = [upd_id]*(self.bin_top<<1)
        if initial != []:
            for i in range(n):
                self.segtree[i+self.bin_top] = initial[i]
                tmp = i + self.bin_top
                while tmp:
                    x = tmp >> 1
                    self.segtree[x] = self.op(upd_id, self.segtree[x<<1], self.segtree[1+(x<<1)])
                    tmp >> 1
    def get_lower(self, l, r):
        L, R = l + self.bin_top, r + self.bin_top
        F = []
        while L < R:
            if L & 1:
                F.append(L)
                L += 1
            if R & 1:
                F.append(R-1)
                R -= 1
            L >>= 1
            R >>= 1
        return F
    def update(self, l, r, x):
        lazy_d = self.get_lower(l, r)
        path_d = []
        L, R = l + self.bin_top, r + self.bin_top
        while L % 2 == 0:
            L >>= 1
        while R % 2 == 0:
            R >>= 1
        tmp = L >> 1
        while tmp:
            path_d.append(tmp)
            tmp >>= 1
        tmp = R >> 1
        while tmp:
            if tmp in path_d:
                break
            path_d.append(tmp)
            tmp >>= 1
        lazy_d.sort()
        path_d.sort()
        for i, k in enumerate(path_d):
            cc = len(bin(k))-3
            self.segtree[k] = self.renew(1<<(self.cnt-cc), self.subtree[k])
