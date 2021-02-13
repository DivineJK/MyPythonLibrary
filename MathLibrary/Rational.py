class Rational:
    def __init__(self):
        self.prev_mod = 0
        self.fact_cnt = 0
        self.fact = [1]
        self.bernouill_cnt = 1
        self.bernouill = [[1, 1], [-1, 2]]
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    def make_fact(self, n):
        if n > self.fact_cnt:
            self.fact = self.fact[:] + [0]*(n-self.fact_cnt)
            for i in range(self.fact_cnt, n):
                self.fact[i+1] = self.fact[i] * (i + 1)
            self.fact_cnt = n
    def frac_sum(self, f1, f2, weight=1):
        f = [f1[0]*f2[1]+weight*f2[0]*f1[1], f1[1]*f2[1]]
        g = gcd(f[0], f[1])
        f[0] //= g
        f[1] //= g
        if f[1] < 0:
            f[0] = -f[0]
            f[1] = -f[1]
        return f
    def frac_prod(self, f1, f2, inverse=False):
        if inverse:
            f = [f1[0]*f2[1], f1[1]*f2[0]]
        else:
            f = [f1[0]*f2[0], f1[1]*f2[1]]
        g = self.gcd(f[0], f[1])
        f[0] //= g
        f[1] //= g
        if f[1] < 0:
            f[0] = -f[0]
            f[1] = -f[1]
        return f
    def get_bernouill(self, n):
        self.make_fact(n+1)
        if n > self.bernouill_cnt:
            for i in range(self.bernouill_cnt, n):
                self.bernouill.append([0, 1])
            for i in range(self.bernouill_cnt+1, n+1):
                if i % 2 == 0:
                    for j in range(i):
                        if j == 1 or j % 2 == 0:
                            tmp = self.frac_sum([0, 1], [-self.fact[i], self.fact[i-j+1]*self.fact[j]])
                            print(tmp, j)
                            self.bernouill[i] = self.frac_sum(self.bernouill[i], self.frac_prod(self.bernouill[j], tmp))
            self.bernouill_cnt = n
        return self.bernouill[n]
