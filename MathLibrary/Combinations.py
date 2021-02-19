class combinations:
    def __init__(self):
        self.comb_num = 0
        self.comb_list = [1]
        self.prev_mod = 0
        self.max_fact = 0
        self.fact = [1]
        self.invf = [1]
        self.invn = [1]
    def factorial_factorization(self, n):
        flg = [False]*(n+1)
        flg[0] = True
        flg[1] = True
        res = {}
        for i in range(2, n+1):
            if flg[i]:
                continue
            for j in range(i, n+1, i):
                flg[j] = True
            p = i
            cnt = 0
            while p <= n:
                cnt += n // p
                p *= i
            res[i] = cnt
        return res
    def comb_arbitary_mod(self, n, k, modulo=0):
        if k > n or k < 0:
            return 0
        if k == 0 or k == n:
            return 1
        f = self.factorial_factorization(n)
        g = self.factorial_factorization(k)
        h = self.factorial_factorization(n-k)
        for i in g:
            f[i] -= g[i]
        for i in h:
            f[i] -= h[i]
        S = 1
        for i in f:
            if modulo:
                S *= pow(i, f[i], modulo)
                S %= modulo
            else:
                S *= pow(i, f[i])
        return S
    def comb_naive(self, n, modulo=0):
        if modulo != self.prev_mod:
            self.prev_mod = modulo
            self.comb_num = 0
            self.comb_list = [1]
        if n <= self.comb_num:
            return None
        for i in range(self.comb_num, n):
            self.comb_list.append(1)
            for j in range(i):
                self.comb_list.append(self.comb_list[-i-1] + self.comb_list[-i-2])
                if modulo:
                    self.comb_list.append[-1] %= modulo
            self.comb_list.append(1)
        self.comb_num = n
        return None
    def comb_naive_get(self, n, k, modulo=0):
        if modulo != self.prev_mod or self.comb_num < n:
            self.comb_naive(n, modulo)
        return self.comb_list[n*(n+1)//2+k]
    def comb_prime_mod_n_large(self, n, k, modulo):
        res = 1
        invn = [1]*(k+2)
        for i in range(k):
            res *= n - i
            res %= modulo
            res *= invn[i+1]
            res %= modulo
            invn[i+2] = (modulo - invn[modulo%(i+2)] * (modulo//(i+2))) % modulo
        return res
    def perm_small_k(self, n, k, modulo=0):
        res = 1
        for i in range(k):
            res *= n - i
            if modulo:
                res %= modulo
        return res
    def make_fact(self, n, modulo):
        if self.prev_mod == modulo:
            self.prev_mod = modulo
            self.max_fact = 0
            self.fact = [1]
            self.invf = [1]
            self.invn = [1]
        if n > self.max_fact:
            for i in range(self.max_fact, n):
                self.fact.append(1)
                self.invn.append(1)
                self.invf.append(1)
                self.fact[i+1] = self.fact[i]*(i+1)%modulo
                if i:
                    self.invn[i+1] = (modulo - self.invn[modulo%(i+1)]*(modulo//(i+1))) % modulo
                    self.invf[i+1] = self.invf[i] * self.invn[i+1] % modulo
            self.max_fact = n
    def comb_prime_mod_n_small(self, n, k, modulo):
        if n < 0 or n < k or k < 0:
            return 0
        if n < self.max_fact or self.prev_mod != modulo:
            self.make_fact(n, modulo)
        return (self.fact[n]*self.invf[k]%modulo)*self.invf[n-k]%modulo
