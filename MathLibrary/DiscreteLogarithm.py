class discrete_log:
    def __init__(self):
        self.prev_num = -1
        self.prev_mod = -1
        self.prev_sqrt = -1
        self.prev_inv = -1
        self.baby_dict = {}
    def inved(self, a, modulo):
        x, y, u, v, k, l = 1, 0, 0, 1, a, modulo
        while l:
            x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
        return x % modulo
    def babystep_giantstep(self, n, x, y):
        # Note: gcd(x, n) = 1
        b = self.prev_inv
        m = self.prev_sqrt
        if n != self.prev_mod or x != self.prev_num:
            self.baby_dict = {}
            self.prev_num = x
            self.prev_mod = n
            l, r = 0, n
            m = (l + r) // 2
            while r - l > 1:
                if m * m <= n:
                    l = m
                else:
                    r = m
                m = (l + r) // 2
            if m * m < n:
                m += 1
            self.prev_sqrt = m
            b = pow(self.inved(x, n), m, n)
            self.prev_inv = b
            f = 1
            for i in range(m):
                if f not in self.baby_dict:
                    self.baby_dict[f] = i
                f *= x
                f %= n
        g = y
        for i in range(m):
            if g in self.baby_dict:
                return i * m + self.baby_dict[g]
            g *= b
            g %= n
        return -1
