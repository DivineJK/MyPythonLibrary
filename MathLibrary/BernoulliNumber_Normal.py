class bernoulli_normal:
    def __init__(self):
        self.prev_mod = 0
        self.fact_cnt = 0
        self.fact = [1]
        self.invf = [1]
        self.bernoulli_cnt = 0
        self.bernoulli = [1]
    def inved(self, a, modulo):
        x, y, u, v, k, l = 1, 0, 0, 1, a, modulo
        while l:
            x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
        return x%modulo
    def make_fact(self, n, modulo):
        if modulo != self.prev_mod:
            self.fact_cnt = 0
            self.fact = [1]
            self.invf = [1]
            self.bernoulli_cnt = 0
            self.bernoulli = [1]
        self.prev_mod = modulo
        if n > self.fact_cnt:
            self.fact = self.fact[:] + [0]*(n-self.fact_cnt)
            self.invf = self.invf[:] + [0]*(n-self.fact_cnt)
            for i in range(self.fact_cnt, n):
                self.fact[i+1] = self.fact[i] * (i + 1)
                if modulo:
                    self.fact[i+1] %= modulo
            if modulo:
                self.invf[-1] = self.inved(self.fact[-1], modulo)
                for i in range(n, self.fact_cnt, -1):
                    self.invf[i-1] = self.invf[i] * i
                    self.invf[i-1] %= modulo
            self.fact_cnt = n
    def get_bernoulli(self, n, modulo):
        if n+1 > self.fact_cnt:
            self.make_fact(n+1, modulo)
        if n > self.bernoulli_cnt:
            for i in range(self.bernoulli_cnt, n):
                self.bernoulli.append(0)
            for i in range(self.bernoulli_cnt+1, n+1):
                if i % 2 == 0 or i == 1:
                    for j in range(i):
                        if j == 1 or j % 2 == 0:
                            tmp = self.invf[i-j+1]*self.invf[j] % modulo
                            self.bernoulli[i] += self.bernoulli[j]*tmp%modulo
                            self.bernoulli[i] %= modulo
                    self.bernoulli[i] *= -self.fact[i]
                    self.bernoulli[i] %= modulo
            self.bernoulli_cnt = n
        return self.bernoulli[n]
    def power_sum(self, n, m, modulo):
        bas = n
        S = 0
        sign = 1 - 2 * (m % 2)
        for i in range(m+1):
            if m-i > self.bernoulli_cnt:
                B = self.get_bernoulli(m-i, modulo)
            else:
                B = self.bernoulli[m-i]
            S += (self.invf[i+1]*self.invf[m-i]%modulo)*(sign*B*bas%modulo)%modulo
            S %= modulo
            bas *= n
            bas %= modulo
            sign *= -1
        return S * self.fact[m] % modulo
